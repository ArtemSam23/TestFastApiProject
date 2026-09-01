import json

from app import llm
from app.tools import TOOLS, TOOLS_SCHEMA


async def run(task: str) -> str:
    messages = [{"role": "user", "content": task}]
    while True:
        answer = await llm.chat(messages, tools=TOOLS_SCHEMA)
        messages.append(answer)
        if not answer.get("tool_calls"):
            return answer["content"]
        for call in answer["tool_calls"]:
            args = json.loads(call["function"]["arguments"])
            result = await TOOLS[call["function"]["name"]](**args)
            messages.append({
                "role": "tool",
                "tool_call_id": call["id"],
                "content": str(result),
            })

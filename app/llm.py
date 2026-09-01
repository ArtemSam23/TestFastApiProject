import json
import os

from dotenv import load_dotenv
from openai import NOT_GIVEN, AsyncOpenAI

load_dotenv()

_client = AsyncOpenAI(
    base_url=os.environ["LLM_BASE_URL"],
    api_key=os.environ["LLM_API_KEY"],
    timeout=float(os.getenv("LLM_TIMEOUT", "30")),
)
_model = os.environ["LLM_MODEL"]


async def chat(messages: list[dict], tools: list[dict] | None = None) -> dict:
    _log("запрос", messages)
    response = await _client.chat.completions.create(
        model=_model,
        messages=messages,
        tools=tools or NOT_GIVEN,
    )
    # оставляем только поля, которые можно вернуть в диалог: лишние ломают часть провайдеров
    answer = response.choices[0].message.model_dump(
        include={"role", "content", "tool_calls"}, exclude_none=True
    )
    _log("ответ", answer)
    return answer


def _log(label: str, payload: object) -> None:
    # весь обмен с моделью виден в stdout, чтобы было понятно, что происходит внутри
    print(f"--- {label} ---")
    print(json.dumps(payload, ensure_ascii=False, indent=2))

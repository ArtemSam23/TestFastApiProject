import asyncio

from app import llm


def test_model_answers():
    # проверяет только доступ: ключ рабочий и эндпоинт отвечает
    answer = asyncio.run(llm.chat([{"role": "user", "content": "Ответь одним словом: ты на связи?"}]))
    assert answer.get("content")

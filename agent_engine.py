import asyncio


# Стара функція залишається для звичайного ендпоінту
async def run_agent_logic(query: str):
    await asyncio.sleep(1)
    return {
        "output": f"Analysis complete for: {query}",
        "steps": ["Parsed query", "Retrieved context from ChromaDB", "Generated CoT reasoning"],
        "score": 0.95
    }


# НОВА ФУНКЦІЯ: Імітація потокової роботи агента (Streaming)
async def stream_agent_steps(query: str):
    steps = [
        "🧠 [Agent]: Розпізнавання наміру користувача...\n",
        "🔍 [RAG]: Пошук релевантного контексту у векторній базі (ChromaDB)...\n",
        "⚙️ [LLM]: Побудова ланцюжка міркувань (Chain-of-Thought)...\n",
        "⚖️ [Reviewer]: Перевірка результату на галюцинації...\n",
        f"✅ [Final]: Готово! Ось ваш результат для запиту: '{query}'.\n"
    ]

    for step in steps:
        await asyncio.sleep(1.5)  # Імітація довгої роботи ШІ
        yield step
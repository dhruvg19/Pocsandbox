import openai

conversation_history = []

def run_prompt_with_memory(prompt, docs, config, is_followup=False):
    global conversation_history
    openai.api_key = config["llm"]["api_key"]
    model = config["llm"]["model"]

    if not is_followup:
        conversation_history = []
        context = "\n\n".join(docs)
        prompt = prompt.replace("[RESEARCH_REPORT]", context[:4000])

    conversation_history.append({"role": "user", "content": prompt})

    response = openai.ChatCompletion.create(
        model=model,
        messages=conversation_history,
        temperature=config["llm"]["temperature"]
    )

    reply = response["choices"][0]["message"]["content"]
    conversation_history.append({"role": "assistant", "content": reply})
    return reply

def reset_history():
    global conversation_history
    conversation_history = []
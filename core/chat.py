from langchain_core.messages import HumanMessage, AIMessage


from core.config import MAX_CHAT_HISTORY


def build_langchain_messages(
    history: list[dict],
    user_message: str
):
    """
    Convert Gradio chat history into LangChain messages.

    Returns:
        messages: LangChain message list
        llm_calls: Number of assistant responses
    """

    history = history[-MAX_CHAT_HISTORY:]

    messages = []
    llm_calls = 0

    for msg in history:

        if msg["role"] == "user":
            messages.append(
                HumanMessage(content=msg["content"])
            )

        elif msg["role"] == "assistant":
            messages.append(
                AIMessage(content=msg["content"])
            )
            llm_calls += 1

    messages.append(
        HumanMessage(content=user_message)
    )

    return messages, llm_calls



def extract_final_output(messages) -> str:
    """
    Extract the final user-visible response
    from a LangGraph message list.
    """

    for message in reversed(messages):

        if getattr(message, "type", None) == "ai":
            return message.content

    return "Sorry, I couldn't generate a response."
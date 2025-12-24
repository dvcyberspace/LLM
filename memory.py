from langchain.memory import ConversationBufferMemory

def get_memory():
    """
    Creates a shared memory object.
    This acts as the 'Short-Term Memory' for our agent collaboration.
    """
    memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True
    )
    return memory
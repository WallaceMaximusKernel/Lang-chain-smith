
from langchain_openai import ChatOpenAI

# Initialize the LLM
llm = ChatOpenAI(model="gpt-4o-mini")

# Define three different prompts
prompts = [
    "Explain LangChain in simple terms with an example.",

    "Explain how APIs work using a real-world banking example.",

    """Design an AI-powered fraud detection solution for a bank.
    Explain the architecture, key components, transaction workflow,
    and business benefits in detail."""
]

# Execute all three prompts
for i, prompt in enumerate(prompts, start=1):

    print(f"\n{'=' * 50}")
    print(f"RUN {i}")
    print(f"{'=' * 50}")

    response = llm.invoke(prompt)

    print(response.content)

import argparse
import base64
import os
from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, AgentType
from tools import run_analysis

# Load your OpenAI API key from the environment
openai_api_key = os.environ.get("OPENAI_API_KEY")

# Set up argument parsing for the data from n8n
parser = argparse.ArgumentParser(description="Run the AI agent.")
parser.add_argument("--question", required=True)
parser.add_argument("--fileData", required=True)
parser.add_argument("--fileName", required=True)
args = parser.parse_args()

# Decode the Base64 string and save it as a file
try:
    decoded_data = base64.b64decode(args.fileData)
    with open(args.fileName, "wb") as f:
        f.write(decoded_data)
    print(f"File saved as {args.fileName}")
except Exception as e:
    print(f"Error decoding file: {e}")
    exit()

# Initialize the LLM
llm = ChatOpenAI(temperature=0, api_key=openai_api_key)

# Initialize the agent with the tool
agent = initialize_agent(
    tools=[analyze_sales_data],
    llm=llm,
    agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    handle_parsing_errors=True
)

# Pass the correct arguments to the tool
question = args.question
file_path = args.fileName

print(f"Asking the AI employee: {question}")
agent.run(f"Analyze the data in the file located at {file_path} to answer this question: {question}")

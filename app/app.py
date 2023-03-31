import os

from llama_index import LLMPredictor, GPTSimpleVectorIndex, PromptHelper, ServiceContext,  SimpleDirectoryReader
from langchain import OpenAI
from langchain.document_loaders import UnstructuredURLLoader
from langchain.chains.summarize import load_summarize_chain
from openai import Completion

from pathlib import Path
from decouple import Config, RepositoryEnv

directory_project = Path(__file__).resolve().parent.parent
directory_data = directory_project/"data"
directory_index = directory_project/"index"
index_file_name = "index.json"
config_file = directory_project/".env"


def training_with_data():
    # set maximum input size
    max_input_size = 4096
    # set number of output tokens
    num_output = 2000
    # set maximum chunk overlap
    max_chunk_overlap = 20

    chunk_size_limit = 600

    # define LLM
    llm_predictor = LLMPredictor(llm=OpenAI(temperature=0.5, model_name="text-davinci-003", max_tokens=num_output))

    prompt_helper = PromptHelper(max_input_size, num_output, max_chunk_overlap, chunk_size_limit=chunk_size_limit)

    service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor, prompt_helper=prompt_helper)

    documents = SimpleDirectoryReader(directory_data).load_data()
    
    index = GPTSimpleVectorIndex.from_documents(documents, service_context=service_context)

    # save to disk
    index.save_to_disk(directory_index/index_file_name)

def ask_ai():
    # load from disk
    index = GPTSimpleVectorIndex.load_from_disk(directory_index/index_file_name)
    while True:
        query = input("What do you want to ask? ")
        response = index.query(query, response_mode="compact")
        print(response.response)

if __name__ == "__main__":
    config = Config(RepositoryEnv(config_file))
    os.environ["OPENAI_API_KEY"] = config("OPENAI_API_KEY")
    # training_with_data()
    # ask_ai()
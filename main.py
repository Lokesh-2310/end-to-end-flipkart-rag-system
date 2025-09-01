from flipkart.data_ingestion import DataIngestor
from flipkart.rag_chain import RAGChainBuilder
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel

load_dotenv()

vector_store = DataIngestor().ingest(load_existing=True)
rag_chain = RAGChainBuilder(vector_store).build_chain()



app = FastAPI()

class UserInput(BaseModel):
    user_input: str

@app.post("/fetch")
def create_item(input: UserInput):
    response = rag_chain.invoke({"input" : input.user_input},
    config={"configurable" : {"session_id" : "user-session"}}
    )["answer"]
    return {"messages": response}




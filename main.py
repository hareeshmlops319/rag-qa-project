from fastapi import FastAPI

app = FastAPI(title="RAG Q&A System", version="1.0.0")

@app.get("/")

async def root():
    return {"message": "Welcome to the RAG Q&A System"}


@app.get("/health")
async def health():
    return {"status": "ok"} 

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="[IP_ADDRESS]", port=8000)




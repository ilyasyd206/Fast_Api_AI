from fastapi import FastAPI, HTTPException, Depends, Security
from fastapi.security.api_key import APIKeyHeader
from fastapi.responses import StreamingResponse
from schemas import AgentTask, AgentResponse
from agent_engine import run_agent_logic, stream_agent_steps

app = FastAPI(
    title="Enterprise AI Agent API",
    description="Enterprise API Gateway for Agentic AI Workflows with Streaming support.",
    version="1.1.0"
)

API_KEY_NAME = "X-API-Key"
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)

def get_api_key(api_key: str = Security(api_key_header)):
    if api_key != "admin-secret-token-2026":
        raise HTTPException(status_code=403, detail="Could not validate credentials")
    return api_key


@app.get("/")
def read_root():
    return {"message": "AI Agent Gateway is online and secured."}

@app.post("/process", response_model=AgentResponse)
async def process_task(task: AgentTask, api_key: str = Depends(get_api_key)):
    try:
        result = await run_agent_logic(task.query)
        return AgentResponse(
            status="success",
            agent_output=result["output"],
            reasoning_steps=result["steps"],
            confidence_score=result["score"]
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/stream")
async def stream_task(query: str):
    return StreamingResponse(stream_agent_steps(query), media_type="text/plain")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
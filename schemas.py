from pydantic import BaseModel, Field
from typing import List, Optional

class AgentTask(BaseModel):
    query: str = Field(..., example="Analyze this Python code for potential bugs")
    context_id: Optional[str] = Field(None, example="repo_123")

class AgentResponse(BaseModel):
    status: str
    agent_output: str
    reasoning_steps: List[str]
    confidence_score: float

    
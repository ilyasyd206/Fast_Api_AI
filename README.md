# 🚀 Enterprise AI Agent API

A high-performance FastAPI microservice designed to act as an API Gateway for Agentic AI workflows and LLM reasoning pipelines. 

## 🌟 Key Features
* **Streaming Responses:** Implemented `StreamingResponse` for Server-Sent Events (SSE) to stream Long-Running AI/LangGraph reasoning steps in real-time.
* **Strict Data Validation:** Utilized `Pydantic` schemas for robust input/output validation.
* **Enterprise Security:** Built-in Dependency Injection for API Key authentication.
* **Interactive Docs:** Auto-generated Swagger UI / OpenAPI documentation.

## 🛠 Tech Stack
* **Python 3.12+**
* **FastAPI** & **Uvicorn**
* **Pydantic**
* **Asyncio**

## 💻 How to run
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Run the server: `python -m uvicorn main:app --reload`
4. Open `http://127.0.0.1:8000/docs` to test the API endpoints.
5. Provide the API key (`admin-secret-token-2026`) in the Authorize section to execute protected routes.
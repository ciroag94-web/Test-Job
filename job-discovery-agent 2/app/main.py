from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from app.agents.job_agent import JobAgent

app = FastAPI(title="Job Discovery Agent")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def home():
    return FileResponse("static/index.html")

@app.get("/api/health")
async def health():
    return {"status": "ok"}

@app.get("/api/jobs")
async def get_jobs():
    agent = JobAgent()
    return await agent.run()

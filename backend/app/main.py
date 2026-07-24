from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Local imports for core components
from .trend_engine import TrendEngine
from .nlp_core import ContentGen
from .dispatcher import SocialDispatcher

app = FastAPI(title="RemixHub API")

# Instantiate core services (could be dependency‑injected in a larger app)
trend_engine = TrendEngine()
content_gen = ContentGen()
social_dispatcher = SocialDispatcher()

class TrendRequest(BaseModel):
    query: str
    # Additional fields like source filters could be added

class GenerationRequest(BaseModel):
    trend: str
    # Placeholder for additional parameters (e.g., brand_id)

class DispatchRequest(BaseModel):
    content_id: str
    platform: str
    # Additional dispatch metadata

@app.post("/trends")
async def get_trends(request: TrendRequest):
    # Integrate Behavior‑Verified Trend Engine
    trends = trend_engine.get_trends(request.query)
    return {"trends": trends}

@app.post("/generate")
async def generate_content(request: GenerationRequest):
    # Call Content‑Gen NLP Core
    generated = content_gen.generate(request.trend)
    return generated

@app.post("/dispatch")
async def dispatch_content(request: DispatchRequest):
    # Integrate Social‑Connect Dispatcher
    result = social_dispatcher.dispatch(request.content_id, request.platform)
    return result

@app.get("/dispatch/logs")
def get_dispatch_logs():
    """Return in‑memory dispatch logs for debugging/monitoring."""
    return {"logs": social_dispatcher.get_logs()}

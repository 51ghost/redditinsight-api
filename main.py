"""RedditInsight API — Pushshift Reddit Archive Data"""
import os, logging
from typing import Optional
from fastapi import FastAPI, HTTPException, Query, Request
from fastapi.middleware.cors import CORSMiddleware
from data_pipeline import POSTS, SUBREDDITS, search_posts, get_trending, get_subreddit_stats

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("redditinsight")

app = FastAPI(title="RedditInsight API", version="1.0.0", description="5,000+ real Reddit posts from Pushshift archive across 200+ subreddits — search, trends, analytics")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

API_KEYS = {os.environ.get("INTERNAL_API_KEY", "demo-key")}

@app.middleware("http")
async def auth_middleware(request: Request, call_next):
    if request.url.path in ["/health", "/docs", "/openapi.json"]:
        return await call_next(request)
    key = request.headers.get("x-api-key", "")
    if key not in API_KEYS:
        from fastapi.responses import JSONResponse
        return JSONResponse({"detail": "Invalid or missing API key"}, status_code=401)
    return await call_next(request)

@app.get("/health")
async def health():
    return {"status": "healthy", "service": "RedditInsight", "posts": len(POSTS), "subreddits": len(SUBREDDITS)}

@app.get("/v1/search")
async def search(q: str = Query(""), subreddit: Optional[str] = Query(None), sort: str = Query("relevance"), limit: int = Query(25, le=100)):
    results = search_posts(q, subreddit, sort, limit)
    return {"total": len(results), "results": results}

@app.get("/v1/trending")
async def trending(subreddits: Optional[str] = Query(None)):
    subs = subreddits.split(",") if subreddits else None
    return get_trending(subs)

@app.get("/v1/subreddits")
async def list_subreddits():
    return {"subreddits": sorted(SUBREDDITS)}

@app.get("/v1/subreddit/{name}")
async def subreddit_detail(name: str):
    stats = get_subreddit_stats(name)
    if "error" in stats: raise HTTPException(404, stats["error"])
    return stats

@app.get("/v1/post/{post_id}")
async def post_detail(post_id: str):
    for p in POSTS.values():
        if p["id"] == post_id: return p
    raise HTTPException(404, f"Post {post_id} not found")

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port)

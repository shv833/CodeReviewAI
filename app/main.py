import logging
from fastapi import FastAPI, HTTPException
from app.models.request_models import ReviewRequest
from app.services.github_service import fetch_repo_contents
from app.services.openai_service import analyze_code


logger = logging.getLogger("uvicorn.error")
app = FastAPI(title="CodeReviewAI")


@app.post("/review")
async def review(request: ReviewRequest):
    try:
        repo_contents = await fetch_repo_contents(request.github_repo_url)
        review_result = await analyze_code(
            repo_contents, request.assignment_description, request.candidate_level
        )
        return review_result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

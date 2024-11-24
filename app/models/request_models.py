from pydantic import BaseModel, HttpUrl, constr
from typing import Literal


class ReviewRequest(BaseModel):
    assignment_description: constr(min_length=10)  # type: ignore
    github_repo_url: HttpUrl
    candidate_level: Literal["Junior", "Middle", "Senior"]

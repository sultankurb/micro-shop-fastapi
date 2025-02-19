from pydantic import BaseModel, Field
from typing import Optional


class ReviewBase(BaseModel):
    review_text: Optional[str] = None
    review_mark: Optional[int] = Field(default=0, max_length=6)
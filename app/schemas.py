from pydantic import BaseModel

class FeedbackSubmission(BaseModel):
    name: str
    email: str
    rating: int
    category: str
    feedback: str

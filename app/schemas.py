from pydantic import BaseModel

class FeedbackSubmission(BaseModel):
    name: str
    email: str
    rating: int
    category: str
    feedback: str

class UserRegister(BaseModel):
    username: str
    email: str
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

class FavoriteToggle(BaseModel):
    model_config = {'protected_namespaces': ()}
    model_id: int

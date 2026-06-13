# =====================================================================
# STEP 3: API INPUT VALIDATION GUIDE
# =====================================================================
# To implement validation for incoming JSON payloads from the client:
#
# 1. Import BaseModel from the pydantic module:
#    from pydantic import BaseModel
#
# 2. Define your payload schema matching the HTML form input fields:
#    - class FeedbackSubmission(BaseModel):
#          name: str
#          email: str
#          rating: int
#          category: str
#          feedback: str
#
# 3. Use this Pydantic schema class as the type hint for the parameters
#    of your POST '/submit_feedback' endpoint in main.py. FastAPI will
#    automatically parse, validate, and serialize incoming JSON payloads
#    into this structure.
# =====================================================================

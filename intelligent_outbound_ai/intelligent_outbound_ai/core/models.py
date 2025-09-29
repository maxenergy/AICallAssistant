from pydantic import BaseModel, Field
from typing import List, Optional, Literal

class CompanyProfile(BaseModel):
    """
    Represents the profile of a target company.
    """
    name: str = Field(..., description="Company's legal name.")
    industry: Optional[str] = Field(None, description="Primary industry of the company.")
    recent_news: Optional[str] = Field(None, description="Latest relevant news about the company.")
    key_personnel: List[str] = Field([], description="List of key decision-makers or contacts.")
    potential_needs: List[str] = Field([], description="Predicted potential needs or pain points.")

class CallScript(BaseModel):
    """
    Represents the generated script for a call.
    """
    opening: str = Field(..., description="The opening line of the call.")
    pain_point_probe: str = Field(..., description="Questions to uncover customer's pain points.")
    objection_handling: str = Field(..., description="Statements to handle common objections.")
    closing_statement: str = Field(..., description="The closing remarks for the call.")

class CallAnalysis(BaseModel):
    """
    Represents the analysis of a completed or in-progress call.
    """
    customer_sentiment: Literal["抗拒", "犹豫", "兴趣", "成功"] = Field(..., description="The detected sentiment of the customer.")
    pain_points_identified: List[str] = Field([], description="List of pain points mentioned by the customer.")
    next_step_suggestion: str = Field(..., description="Suggested next action for the sales agent.")
    follow_up_priority: Literal["高", "中", "低"] = Field(..., description="Priority for following up with the customer.")
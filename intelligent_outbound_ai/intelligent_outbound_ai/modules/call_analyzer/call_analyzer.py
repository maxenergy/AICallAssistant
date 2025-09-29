from typing import List
from intelligent_outbound_ai.core.models import CallAnalysis

def analyze_call(transcript: List[str]) -> CallAnalysis:
    """
    Analyzes a call transcript to provide real-time feedback and scoring.

    This is a stub function that returns a mock analysis.
    """
    return CallAnalysis(
        customer_sentiment="兴趣",
        pain_points_identified=["成本过高", "效率低下"],
        next_step_suggestion="提供一个详细的案例研究，展示我们如何为类似客户解决这些问题。",
        follow_up_priority="高"
    )
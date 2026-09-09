from typing import Any, Dict

from ai.agents.question_parser import parse_question
from ai.tools.semantic_tool import semantic_query


class MetricMindAgent:
    """
    MetricMind AI Agent.

    Flow:
        User Question
            ↓
        Question Parser
            ↓
        Semantic Tool
            ↓
        Structured Result
    """

    def __init__(self):
        self.semantic_tool = semantic_query

    def run(self, question: str) -> Dict[str, Any]:
        """
        Process a business question and return a structured result.
        """

        parsed = parse_question(question)

        if not parsed.get("metric"):
            return {
                "success": False,
                "question": question,
                "error": "Could not identify an approved business metric.",
                "parsed_question": parsed,
            }

        semantic_result = self.semantic_tool.invoke(
            {
                "metric": parsed.get("metric"),
                "dimension": parsed.get("dimension"),
                "filters": parsed.get("filters", {}),
                "time_period": parsed.get("time_period"),
            }
        )

        return {
            "success": semantic_result.get("success", False),
            "question": question,
            "parsed_question": parsed,
            "semantic_result": semantic_result,
        }


def create_metricmind_agent() -> MetricMindAgent:
    """
    Factory function for creating the MetricMind agent.
    """
    return MetricMindAgent()


from ai.agents.question_parser import parse_question
from ai.agents.metricmind_agent import MetricMindAgent
from ai.tools.semantic_tool import semantic_query


def test_question_parser():
    result = parse_question(
        "Why did our European margins drop last quarter?"
    )

    assert result["success"] is True
    assert result["metric"] == "margin"
    assert result["dimension"] == "region"
    assert result["time_period"] == "last quarter"
    assert result["intent"] == "explanation"


def test_semantic_tool():
    result = semantic_query.invoke(
        {
            "metric": "revenue",
            "dimension": "region",
            "filters": {},
            "time_period": "last quarter",
        }
    )

    assert result["success"] is True
    assert result["metric"] == "revenue"
    assert result["dimension"] == "region"


def test_metricmind_agent():
    agent = MetricMindAgent()

    result = agent.run(
        "Why did our European margins drop last quarter?"
    )

    assert result["success"] is True
    assert result["parsed_question"]["metric"] == "margin"
    assert result["semantic_result"]["metric"] == "margin"


def test_missing_metric():
    agent = MetricMindAgent()

    result = agent.run(
        "Show me the performance last quarter."
    )

    assert result["success"] is False


def test_unsupported_metric():
    result = semantic_query.invoke(
        {
            "metric": "unknown_metric",
            "dimension": "region",
            "filters": {},
            "time_period": "last quarter",
        }
    )

    assert result["success"] is False
from agent.metricmind_agent import MetricMindAgent


def main():
    agent = MetricMindAgent()

    question = "What is the difference between revenue and profit?"

    response = agent.ask(question)

    print("\nMetricMind-AI Response:")
    print(response)


if __name__ == "__main__":
    main()
from retrieve import search_runbooks
from prometheus import query_prometheus
from loki import query_loki


def collect_evidence(question):
    runbooks = search_runbooks(question)

    metrics = query_prometheus(
        "100 - (avg(rate(node_cpu_seconds_total{mode=\"idle\"}[5m])) * 100)"
    )

    logs = query_loki('{job="nginx"}')

    return {
        "runbooks": runbooks,
        "metrics": metrics,
        "logs": logs
    }


if __name__ == "__main__":
    question = input("What is happening? ")

    evidence = collect_evidence(question)

    print("\n--- RUNBOOK ---")
    print(evidence["runbooks"])

    print("\n--- METRICS ---")
    print(evidence["metrics"])

    print("\n--- LOGS ---")
    print(evidence["logs"])

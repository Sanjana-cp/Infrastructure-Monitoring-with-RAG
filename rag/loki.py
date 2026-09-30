import requests

LOKI_URL = "http://localhost:3100"


def query_loki(query, limit=20):
    response = requests.get(
        f"{LOKI_URL}/loki/api/v1/query_range",
        params={
            "query": query,
            "limit": limit
        }
    )

    response.raise_for_status()

    data = response.json()

    logs = []

    for stream in data["data"]["result"]:
        for timestamp, line in stream["values"]:
            logs.append(line)

    return logs

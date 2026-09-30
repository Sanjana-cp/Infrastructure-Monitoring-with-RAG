from pathlib import Path

RUNBOOK_DIR = Path("../knowledge/runbooks")


def search_runbooks(query):
    results = []

    query_words = query.lower().split()

    for file in RUNBOOK_DIR.glob("*.md"):
        content = file.read_text().lower()

        score = sum(word in content for word in query_words)

        if score > 0:
            results.append((score, file.name, content))

    results.sort(reverse=True)

    return results[:1]


if __name__ == "__main__":
    results = search_runbooks("high cpu")

    for score, filename, content in results:
        print(f"\nScore: {score} | {filename}")
        print(content)

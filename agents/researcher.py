from tools.web_search import search_web
year = 2026

def research_company(company):
    queries = [
        f"{company} official investor relation annual report",
        f"{company} main competitors",
        f"{company} latest business news",
        f"{company} strategic risks 2026",
        f"{company} growth opportunities 2026"
    ]

    all_results = []

    for query in queries:
        results = search_web(query, max_results=5)

        all_results.append({
            "query": query,
            "results": results
        })

    return all_results
from ddgs import DDGS

def search_web(query, max_results=5):
    try:
        results = []

        with DDGS() as ddgs:
            search_results = ddgs.text(
                query,
                region="us-en",
                safesearch="moderate",
                timelimit="y",
                max_results=max_results
            )

            for result in search_results:
                results.append({
                    "title": result.get("title", "Sin título"),
                    "url": result.get("href", "Sin URL"),
                    "snippet": result.get("body", "Sin descripción")
                })

        return results

    except Exception as e:
        return [
            {
                "title": "Error en búsqueda",
                "url": "",
                "snippet": str(e)
            }
        ]
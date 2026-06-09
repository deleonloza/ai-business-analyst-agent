from agents.llm import ask_llm

def analyze_research(company, research):
    research_text = ""

    for item in research:
        research_text += f"\nQUERY: {item['query']}\n"

        for result in item["results"]:
            research_text += f"""
Title: {result['title']}
Snippet: {result['snippet']}
URL: {result['url']}
"""

    prompt = f"""
Actúa como un Business Analysis Agent especializado en estrategia empresarial.

Empresa analizada: {company}

Información recopilada por el Research Agent:
{research_text}

Genera un análisis ejecutivo en español con estas secciones:

1. Resumen de la empresa
2. Principales competidores
3. Tendencias relevantes del mercado
4. Riesgos principales
5. Oportunidades de crecimiento
6. Recomendaciones estratégicas

Importante:
- Sé concreto y profesional.
- No inventes datos financieros exactos si no aparecen en las fuentes.
- Usa la información disponible.
- Si faltan datos, indícalo claramente.
"""

    return ask_llm(prompt)
from agents.llm import ask_llm

def generate_report(company, analysis):

    prompt = f"""
Actúa como un Executive Report Agent.

Empresa analizada:
{company}

Análisis realizado:
{analysis}

Genera un informe ejecutivo profesional en español.

Incluye:

# Resumen Ejecutivo

# Situación actual

# Competidores

# Riesgos

# Oportunidades

# Recomendaciones Estratégicas

Usa formato markdown y un tono profesional.
"""

    return ask_llm(prompt)
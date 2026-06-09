from agents.llm import ask_llm

def create_plan(company):
    prompt = f"""
    Actúa como un Planner Agent especializado en análisis de negocio.
    
    Empresa a analizar: {company}
    
    Genera un plan breve y estructurado para analizar esta empresa
    Incluye entre 5 y 7 pasos.
    """
    
    return ask_llm(prompt)
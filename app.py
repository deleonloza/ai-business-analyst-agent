import streamlit as st
from agents.planner import create_plan
from agents.researcher import research_company
from agents.analyst import analyze_research
from agents.reporter import generate_report

st.set_page_config(
    page_title="AI Business Analyst Agent",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Business Analyst Agent")
st.write("Agente que analiza una empresa y genera un informe ejecutivo.")

company = st.text_input("Introduce el nombre de una empresa", 
                        placeholder ="Ej: Tesla, Nvidia, Mercado Libre")

if st.button("Analizar empresa"):
    if not company:
        st.warning("Introduce una empresa primero.")
    else:
        with st.spinner("Planner Agent generando plan..."):
            plan = create_plan(company)
            
        st.subheader("Plan generado por el Planner Agent")
        st.write(plan)
        
        with st.spinner("Research Agent buscando información"):
            research = research_company(company)
            
        st.subheader("Resultados del Research Agent")
        
        for item in research:
            st.markdown(f"### Query: {item['query']}")

            if not item["results"]:
                st.warning("No se encontraron resultados para esta búsqueda.")

            for result in item["results"]:
                st.markdown(f"**{result['title']}**")
                st.write(result["snippet"])
                st.write(result["url"])
                st.divider()
        
        with st.spinner("Analysis Agent generando insights..."):
            analysis = analyze_research(company, research)

        st.subheader("Análisis del Business Analysis Agent")
        st.write(analysis)
        
        with st.spinner("Report Agent generando informe..."):
            report = generate_report(company, analysis)

        st.subheader("Informe Ejecutivo Final")
        st.markdown(report)
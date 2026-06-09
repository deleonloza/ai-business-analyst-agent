\# AI Business Analyst Agent



Mini proyecto de IA Agéntica desarrollado para demostrar un flujo modular de agentes especializados aplicado al análisis empresarial.



\## Objetivo



El objetivo de este proyecto es automatizar el proceso inicial de investigación y análisis de una empresa.



El sistema recibe el nombre de una empresa y genera un informe ejecutivo que incluye:



\* Resumen de la empresa

\* Competidores

\* Riesgos

\* Oportunidades

\* Recomendaciones estratégicas



\## Arquitectura



El sistema sigue una arquitectura modular basada en agentes:



```text

Usuario

↓

Interfaz Streamlit

↓

Planner Agent

↓

Research Agent

↓

DuckDuckGo Search Tool

↓

Analysis Agent

↓

Report Agent

↓

Informe Ejecutivo

```



Una representación gráfica de la arquitectura se encuentra en `Arquitectura.pdf`.



\## Agentes



El proyecto está compuesto por cuatro agentes:



\### Planner Agent



Genera un plan de análisis para la empresa seleccionada.



\### Research Agent



Obtiene información externa utilizando DuckDuckGo Search.



\### Analysis Agent



Sintetiza la información recopilada y genera insights de negocio.



\### Report Agent



Transforma el análisis en un informe ejecutivo profesional.



\## Tecnologías



\* Python

\* Streamlit

\* Groq API

\* DuckDuckGo Search

\* python-dotenv



\## ¿Por qué Streamlit?



Streamlit fue elegido porque permite desarrollar aplicaciones interactivas de forma rápida utilizando únicamente Python.



Esto permite centrar el proyecto en la arquitectura agéntica en lugar del desarrollo del frontend.



\## ¿Por qué DuckDuckGo Search?



DuckDuckGo Search fue elegido porque proporciona una herramienta de búsqueda ligera y gratuita que puede integrarse fácilmente en el Research Agent.



La arquitectura es modular, lo que permite sustituir la herramienta de búsqueda por otras alternativas como Tavily, SerpAPI, Bing Search API u otros proveedores.



\## Estructura del Proyecto



```text

ai-business-analyst-agent/

│

├── app.py

├── requirements.txt

├── .env.example

├── README.md

├── README\_es.md

├── Arquitectura.pdf

│

├── screenshots/

│   ├── 01\_home.png

│   ├── 02\_planner\_agent.png

│   ├── 03\_research\_agent.png

│   ├── 04\_analyst\_agent.png

│   └── 05\_executive\_report.png

│

├── agents/

│   ├── \_\_init\_\_.py

│   ├── llm.py

│   ├── planner.py

│   ├── researcher.py

│   ├── analyst.py

│   └── reporter.py

│

└── tools/

&#x20;   ├── \_\_init\_\_.py

&#x20;   └── web\_search.py

```



\## Capacidades de IA Agéntica Demostradas



\* Planificación

\* Uso de herramientas

\* Razonamiento multi-paso

\* Arquitectura modular

\* Generación de informes ejecutivos

\* Separación de responsabilidades



\## Capturas de Pantalla



Las siguientes imágenes muestran extractos de las salidas generadas por cada agente. Los resultados completos son más extensos y se han truncado para facilitar su visualización.



\### Pantalla Principal



!\[Pantalla Principal](screenshots/01\_home.png)



\### Planner Agent



Ejemplo del plan de análisis generado para la empresa seleccionada.



\*La imagen muestra un extracto del plan generado.\*



!\[Planner Agent](screenshots/02\_planner\_agent.png)



\### Research Agent



Ejemplo de información externa obtenida mediante DuckDuckGo Search.



\*La imagen muestra un extracto de los resultados obtenidos.\*



!\[Research Agent](screenshots/03\_research\_agent.png)



\### Analysis Agent



Ejemplo de los insights de negocio generados a partir de la información recopilada.



\*La imagen muestra un extracto del análisis generado.\*



!\[Analysis Agent](screenshots/04\_analyst\_agent.png)



\### Informe Ejecutivo



Ejemplo del informe ejecutivo final entregado al usuario.



\*La imagen muestra un extracto del informe generado.\*



!\[Informe Ejecutivo](screenshots/05\_executive\_report.png)



\## Instalación (Windows)



Crear un entorno virtual:



```bash

python -m venv venv

```



Activar el entorno virtual:



```bash

venv\\Scripts\\activate

```



Instalar las dependencias:



```bash

pip install -r requirements.txt

```



Variables de entorno:



Crear un archivo `.env` a partir de `.env.example`:



```env

GROQ\_API\_KEY=your\_api\_key\_here

```



\## Ejecución



```bash

streamlit run app.py

```



\## Ejemplo de Uso



Entrada:



```text

Tesla

```



Salida:



```text

Informe ejecutivo con resumen de la empresa, competidores, riesgos, oportunidades y recomendaciones estratégicas.

```



\## Conceptos de IA Agéntica Demostrados



\* Planificación

\* Uso de herramientas externas

\* Flujo multiagente

\* Separación de responsabilidades

\* Razonamiento multi-paso

\* Generación de salidas accionables



\## Limitaciones



\* DuckDuckGo Search puede devolver resultados repetidos o incompletos.

\* El análisis depende de la calidad de las fuentes recuperadas.

\* Actualmente no se dispone de memoria persistente.

\* Los datos financieros no se validan automáticamente con fuentes oficiales.

\* La implementación actual está optimizada para generar informes en español.



\## Mejoras Futuras



\* Migrar el flujo de trabajo a LangGraph.

\* Incorporar memoria persistente.

\* Mejorar el ranking y filtrado de fuentes.

\* Exportar los informes a PDF.

\* Incorporar validación Human-in-the-loop.

\* Sustituir DuckDuckGo Search por Tavily u otro motor de búsqueda optimizado para aplicaciones de IA Agéntica.

\* Añadir soporte multilingüe.



\## Autor



David E. León Loza – B.Eng. Ingeniería Mecatrónica


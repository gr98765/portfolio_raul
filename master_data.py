"""
Central store of Gaurangi's bio/resume content.
Edit this file to update what the chatbot knows — nothing else needs to change.
"""

NAME = "Gaurangi Raul"
TAGLINE = "I build systems that retrieve, reason, and report."
LOCATION = "Tucson, AZ"
EMAIL = "gauraul22@gmail.com"
LINKEDIN = "https://www.linkedin.com/in/gaurangi-raul-548694324/"
GITHUB = "https://github.com/gr98765"
GOOGLE_SCHOLAR = "https://scholar.google.com/citations?user=t1gyq8IAAAAJ&hl=en"

ABOUT = """
I hold an MS in Machine Learning from the University of Arizona and work across
four overlapping domains: RAG and LLM systems, data science and analytics,
software and backend engineering, and applied research. At Right Skale, I've worked on both sides of a
production document-intelligence platform: building RAG pipeline components
(ingestion, chunking, Qdrant semantic search, FastAPI on AWS Lambda) and
running the statistical analysis that keeps it reliable, cutting inference
costs 40-50% along the way. My NSF-funded research on adaptive cybersecurity
tutoring was an IEEE FIE'25 Finalist. Outside of work, I build full-stack
and backend projects — a multi-tenant SaaS platform, an event-driven fintech
pipeline — because I like seeing a system go from design to something that
actually runs in production. I use AI-assisted tools like Cursor and Claude
Code in my own workflow. The throughline across everything: instrument it,
measure it, then make it better.
"""

EDUCATION = """
- MS, Machine Learning — University of Arizona, GPA 3.83, NSF-funded, IEEE FIE'25 Finalist (May 2026)
- BE, Computer Science (AI & ML) — Mumbai University, GPA 8.71 (May 2024)
"""

EXPERIENCE = """
1. AI Engineer Intern - Strategy & Analytics, Right Skale Inc. (Jan 2026 - May 2026, Remote)
   Project: Multi-Tenant Document Intelligence Platform
   - Instrumented every step of a production RAG pipeline serving 3+ enterprise clients using
     Langfuse; tracked token usage, inference cost, and latency per LLM call and workflow stage,
     exposing bottlenecks invisible to standard application logging.
   - Optimized prompt templates and model-routing logic through Langfuse trace analysis,
     reducing LLM inference costs by ~40-50% and improving end-to-end response latency while
     preserving retrieval and generation quality across enterprise tenants.
   - Integrated a DeepEval framework leveraging RAGAS metrics across the RAG pipeline for
     systematic evaluation; incorporated observability across S3-backed processing stages to
     identify failure patterns, validate model improvements, and ensure consistent response
     quality.
   - Enhanced multi-tenant RAG workflows by supporting API migration to FastAPI across
     PostgreSQL, Docker, and AWS services; collaborated with engineering teams to validate
     pipeline reliability and maintain consistent performance across client environments.

2. Research Assistant, University of Arizona (Jan 2025 - Jul 2025, Tucson, AZ)
   Project: RAG-PRISM - NSF-Funded Adaptive Cybersecurity Tutoring
   - Designed and led development of an end-to-end RAG pipeline spanning ingestion, chunking,
     embeddings, vector retrieval, and GPT-powered generation for cybersecurity workforce;
     evaluated LangChain and Hugging Face during prototyping before implementing retrieval with
     LlamaIndex.
   - Engineered a hybrid evaluation framework combining synthetic QA generation and manual query
     testing across 15 queries, achieving a perfect retrieval hit rate and MRR of 1.00; GPT-4
     delivered 100% faithfulness and 93.3% relevancy, outperforming all other model variants
     including GPT-3.5 Turbo, GPT-3.5-16k, and GPT-4 Turbo.
   - Integrated zero-shot LLM-based sentiment analysis on VR Digital Twin learner interactions to
     dynamically adjust retrieval queries and instructional content based on emotional and
     cognitive state, improving contextual relevance by 25% over baseline.
   - Spearheaded cross-functional collaboration with electrical engineers, compliance
     stakeholders, and instructional designers to align system output.

3. Machine Learning Engineer, Internshala (Oct 2023 - Apr 2024, Remote)
   Project: Enrolment Probability Forecasting - Recommendation System
   - Designed and built SQL data pipelines for ingestion and A/B testing, collaborating within
     an Agile framework (sprint planning, technical sequence diagrams) to deliver testable,
     production-ready features.
   - Built and validated backend feature-engineering services in Python (Pandas), imputing
     missing values, normalizing engagement features, and engineering interaction-based
     features to ensure clean, reliable inputs for downstream production systems.
   - Evaluated logistic regression, decision tree, and random forest models using
     cross-validation F1 and precision-recall trade-offs; integrated the optimal model into the
     product pipeline, improving recommendation accuracy by 18% and revenue by 10%.

4. Software Developer Intern, Softscribble (May 2023 - Aug 2023, Mumbai, India)
   - Engineered a data ingestion API to process 100k+ data points monthly, improving integration
     efficiency and scalability.
"""

PROJECTS = """
1. Relay.io - Multi-Tenant SaaS Platform (Incident & Release Management)
   - Full-stack multi-tenant SaaS app (FastAPI, PostgreSQL, React) with CRUD REST APIs, JWT
     auth, and role-based access control (Owner/Member), enforcing data isolation between
     organizations — verified by an automated pytest suite.
   - CI/CD pipeline (GitHub Actions) running lint + tests on every push, containerized with
     Docker and deployed to production (Render, Vercel, Supabase Postgres); SQL analytics
     endpoint (joins, aggregates, time-window filtering) powering a live reliability dashboard
     with severity breakdowns and incident assignment.

2. Fintech Transaction Pipeline (kafka_CI-CD) - event-driven backend
   - Event-driven transaction-processing service: transactions POST to a FastAPI endpoint,
     publish to a Kafka topic, get picked up by a background consumer, run through a risk rule,
     and land in Postgres; a small dashboard polls and shows live results.
   - Fully tested and built automatically on every push via GitHub Actions (lint with ruff,
     pytest suite with mocked Kafka/Postgres, Docker image build); containerized with
     docker-compose for one-command local setup.

3. Semantic Hybrid Retrieval for Funding Discovery (Oct 2025) - FAISS, Weaviate
   - Hybrid retrieval pipeline combining lexical, semantic embedding, and keyword search
     (FAISS for dense vector indexing, Weaviate for semantic search + knowledge graph),
     achieving a 20% precision gain over single-strategy retrieval.
   - Documented tradeoffs across FAISS, Weaviate, and Qdrant to inform enterprise
     knowledge-retrieval architecture decisions.

4. ResumeOS - AI Resume Intelligence Platform (agentic RAG architecture)
   - Multi-prompt agentic pipeline using Groq's Llama 3.3 70B to parse resume PDFs into
     validated JSON and score bullets across 7 evaluation dimensions, with under 2% parse
     failure rate at scale.
   - Zero-cost serverless deployment on Firebase and Vercel, routing LLM inference through
     client-side API keys (no server infra costs, unlimited concurrent users); D3.js
     force-directed skill graph and anonymous Firebase auth.

5. Customer Churn Prediction - Risk Segmentation (CI/CD automated ML pipeline)
   - EDA and feature engineering on customer behavioral/transactional data with
     Python/Pandas/SQL, applying inferential statistics to surface at-risk patterns.
   - Trained and validated classifiers in Scikit-Learn and TensorFlow with CI/CD workflows for
     automated batch processing and drift monitoring; Power BI dashboards for real-time
     retention reporting.

6. RAG-PRISM (NSF-funded research, IEEE FIE'25 Finalist)
   - RAG pipeline for domain-specific tutoring (cybersecurity education): indexes documents
     with LlamaIndex and answers with GPT-3.5/GPT-4, grounded in retrieved context.
   - Evaluated with MRR, Hit@k, faithfulness, and precision/recall; achieved a perfect
     retrieval hit rate and MRR of 1.00 across 15 test queries.
   - Repo: https://github.com/gr98765/RAG-PRISM

7. Multi-Agent Market Research (MCP server + LangGraph)
   - Agent team (Coordinator, Researcher, Analyst, Writer, Reviewer) that researches public
     companies and writes reports where every number is verified against official SEC filings,
     not pulled from the model's memory.
   - Built a 5-tool MCP server (resolve_company, get_financials, list_filings, search_news,
     get_price_performance) as the single source of truth for the agents; math is done in
     code, never by the LLM. A Reviewer agent checks every cited number against its source
     before a report is shown.
   - Stack: Python, MCP, FastAPI, LangGraph, React, TypeScript, SEC EDGAR, Tavily, yfinance.

8. Clinical Document Recommendation System
   - End-to-end ML pipeline recommending clinical guidelines from unstructured text -
     Sentence-BERT (all-MiniLM-L6-v2) embeddings, with TF-IDF + Logistic Regression baselines
     and an XGBoost ranker.
   - Results served via a REST API with a React UI.

9. Production Document Intelligence Platform (Right Skale - proprietary, not open source)
   - Contributed to a Python service built with FastAPI for ingestion, retrieval, and
     inference, deployed across AWS and Azure to support a production RAG pipeline serving
     3+ enterprise clients.
   - Instrumented every step of the pipeline with Langfuse - tracking token usage, cost, and
     latency per call and workflow stage - reducing inference cost and latency by ~40-50%
     through trace-driven prompt and routing optimization.
   - This is proprietary Right Skale work; no public repo. Direct people to contact Gaurangi
     for details rather than a code link.

10. Algorithmic Trading Bot (Kotak Neo API) - published research, BE final-year project
   - Built an RSI-based algorithmic trading system on the Kotak Neo Trade API: live market
     data, token-based auth, automated buy/sell signal generation from overbought/oversold
     RSI thresholds, and stop-loss orders for risk management.
   - Backtested the strategy against historical data pulled via yfinance to evaluate
     profitability and win rate before any live deployment.
   - Published as first author: "Algorithmic Trading with an API," IRJET Vol. 11 Issue 10
     (Mar 2024), peer-reviewed, Impact Factor 8.315. Co-authored with Riya Jadhav, Tejas
     Kamble, and Kshitija Satpute.
"""

SKILLS = """
- Languages: Python, SQL, R, TypeScript, JavaScript, HTML, CSS
- Backend/Frontend: FastAPI, React, RESTful APIs, CRUD services, JWT authentication
- Data analysis: Pandas, NumPy, EDA, feature engineering, statistical analysis, probability,
  A/B testing, anomaly detection
- Machine learning: Scikit-Learn, TensorFlow, PyTorch, XGBoost, supervised/unsupervised learning,
  classification, regression, clustering, cross-validation
- AI/RAG frameworks: LangChain, LangGraph, LlamaIndex, Hugging Face, DeepEval, RAGAS,
  Semantic Kernel (familiar), Agentic RAG, Multi-Agent Orchestration, MCP (Model Context Protocol)
- Vector databases: Qdrant, FAISS, Weaviate, ChromaDB, pgvector, Pinecone (familiar)
- Visualization: Matplotlib, Seaborn, Plotly, Power BI, Tableau
- MLOps/Observability: Langfuse, Pytest, CI/CD (GitHub Actions), Git/GitHub, Docker,
  experiment tracking
- Cloud/Infra: AWS (Lambda, EC2, S3), Azure, Google Cloud Platform, PostgreSQL, MySQL, MongoDB,
  Kafka, ETL pipelines, Render, Vercel, Supabase
- Methodology: Agile/Scrum, sprint planning, code review, SDLC
- AI-assisted dev tools: Cursor, Claude Code
"""

CERTIFICATIONS = """
- Mastering Databricks Spark Pipelines - Udemy (2026)
- Machine Learning Specialization - DeepLearning.AI (in progress)
"""

PUBLICATIONS = """
- RAG-PRISM: A Personalized, Rapid, and Immersive Skill Mastery Framework with Adaptive
  Retrieval-Augmented Tutoring - IEEE FIE 2025 Finalist, NSF grant #2335046, 9 authors.
  Paper: https://ieeexplore.ieee.org/abstract/document/11328742
  Code: https://github.com/gr98765/RAG-PRISM
- Algorithmic Trading with an API - IRJET, Vol. 11 Issue 10 (Mar 2024), peer-reviewed,
  Impact Factor 8.315. First author, with Riya Jadhav, Tejas Kamble, and Kshitija Satpute.
  Paper: https://www.irjet.net/archives/V11/i10/IRJET-V11I1070.pdf
  Code: https://github.com/gr98765/Algorithm-trading-bot-using-API
"""

# This is the single block injected into the LLM's system prompt.
FULL_CONTEXT = f"""
Name: {NAME}
Tagline: {TAGLINE}
Location: {LOCATION}
Contact: {EMAIL}, LinkedIn: {LINKEDIN}, GitHub: {GITHUB}, Google Scholar: {GOOGLE_SCHOLAR}

About:
{ABOUT}

Education:
{EDUCATION}

Experience:
{EXPERIENCE}

Projects:
{PROJECTS}

Skills:
{SKILLS}

Certifications:
{CERTIFICATIONS}

Publications:
{PUBLICATIONS}
"""

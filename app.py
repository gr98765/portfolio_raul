"""
Portfolio chatbot for Gaurangi Raul — no persona name, just a plain chat.

Architecture (mirrors the VijBot pattern):
  1. Try to match the user's message against a set of canned Q&A pairs
     using TF-IDF (character n-grams) + cosine similarity. Cheap, fast,
     no API call — handles greetings, small talk, off-topic/troll input,
     and common FAQs with specific, pre-written answers.
  2. If nothing matches well enough, fall back to an LLM, given a system
     prompt built from Gaurangi's resume data, instructed to answer with
     real specifics (names, numbers, project details) rather than vague
     generalities, and to say when it doesn't know something.
"""

import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from openai import OpenAI

from master_data import NAME, EMAIL, FULL_CONTEXT
from stored_questions import CANNED_RESPONSES

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

SIMILARITY_THRESHOLD = 0.75  # high on purpose: only near-exact greetings/junk hit canned answers; everything else goes to the LLM

# Any OpenAI-SDK-compatible provider works here (OpenAI, DeepSeek, Groq, etc.)
# Set these in .streamlit/secrets.toml (see README) — never hardcode a key.
LLM_BASE_URL = st.secrets.get("LLM_BASE_URL", "https://api.openai.com/v1")
LLM_MODEL = st.secrets.get("LLM_MODEL", "gpt-4o-mini")
LLM_API_KEY = st.secrets.get("LLM_API_KEY", "")

SYSTEM_PROMPT = f"""
You are a chat assistant embedded in {NAME}'s portfolio site. Recruiters and
engineers ask you about her work. Answer ONLY from the resume/portfolio data
below.

How to answer:
- Give a real answer in your own words, not a list of keywords. Explain what she
  actually built or did, why it mattered, and the result, using the specific
  project, company, tools, and numbers from the data.
- If a question is broad ("what's her strongest project?"), pick one or two
  relevant items, say why, and offer to go deeper.
- Match the question's angle. Backend question: lead with Relay.io, the Kafka
  fintech pipeline, and the FastAPI work. AI/RAG question: lead with the
  multi-agent MCP project, RAG-PRISM, and the Right Skale platform.
  Research question: lead with the IEEE FIE'25 paper and the IRJET paper.
- Keep it to 2-5 sentences unless asked for more. Be warm and direct.
- Never invent facts, numbers, employers, dates, or links. If the data does not
  cover something (availability, salary, visa status, opinions), say you don't
  have that and suggest emailing {NAME} at {EMAIL}.
- The Right Skale platform is proprietary client work: there is no public code
  for it. Say so if asked, and point to her open-source projects instead.
- If asked something unrelated to {NAME}'s background, politely say you only
  cover her work and steer back.

Resume and portfolio data:
{FULL_CONTEXT}
"""

# ---------------------------------------------------------------------------
# TF-IDF pre-filter
# ---------------------------------------------------------------------------

@st.cache_resource
def build_matcher():
    keys = list(CANNED_RESPONSES.keys())
    vectorizer = TfidfVectorizer(analyzer="char_wb", ngram_range=(2, 4))
    matrix = vectorizer.fit_transform(keys)
    return vectorizer, matrix, keys


def match_canned_response(user_input: str):
    vectorizer, matrix, keys = build_matcher()
    user_vec = vectorizer.transform([user_input.lower().strip()])
    sims = cosine_similarity(user_vec, matrix)[0]
    best_idx = sims.argmax()
    if sims[best_idx] >= SIMILARITY_THRESHOLD:
        return CANNED_RESPONSES[keys[best_idx]]
    return None


# ---------------------------------------------------------------------------
# LLM fallback
# ---------------------------------------------------------------------------

def call_llm(history):
    if not LLM_API_KEY:
        return (
            "The chatbot's LLM key isn't configured yet, so I can only answer "
            "questions that match my built-in FAQ. Try asking about Gaurangi's "
            "experience, projects, or skills — or reach her at " + EMAIL + "."
        )

    client = OpenAI(base_url=LLM_BASE_URL, api_key=LLM_API_KEY)
    messages = [{"role": "system", "content": SYSTEM_PROMPT}] + history

    response = client.chat.completions.create(
        model=LLM_MODEL,
        messages=messages,
        max_tokens=300,
        temperature=0.4,
    )
    return response.choices[0].message.content


# ---------------------------------------------------------------------------
# UI
# ---------------------------------------------------------------------------

st.set_page_config(page_title=f"Chat — {NAME}", page_icon="💬", layout="centered")

st.markdown(
    """
    <style>
    .stApp { background-color: #14171C; color: #ECEAE4; }
    .chat-bubble-user {
        background-color: #1C2027; color: #ECEAE4;
        padding: 10px 14px; border-radius: 12px; margin: 6px 0;
        max-width: 80%; margin-left: auto; text-align: right;
    }
    .chat-bubble-bot {
        background-color: #6FE7C3; color: #0B1210;
        padding: 10px 14px; border-radius: 12px; margin: 6px 0;
        max-width: 80%; margin-right: auto; text-align: left;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("💬 Ask me anything")
st.caption(f"An assistant trained on {NAME}'s resume — ask about her experience, projects, or skills.")

if "history" not in st.session_state:
    st.session_state.history = []  # list of {"role": "user"/"assistant", "content": str}

for msg in st.session_state.history:
    css_class = "chat-bubble-user" if msg["role"] == "user" else "chat-bubble-bot"
    st.markdown(f'<div class="{css_class}">{msg["content"]}</div>', unsafe_allow_html=True)

user_input = st.chat_input("Ask something about Gaurangi...")

if user_input:
    st.session_state.history.append({"role": "user", "content": user_input})

    canned = match_canned_response(user_input)
    if canned:
        reply = canned
    else:
        reply = call_llm(st.session_state.history)

    st.session_state.history.append({"role": "assistant", "content": reply})
    st.rerun()

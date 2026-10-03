# Portfolio chatbot

Same architecture as VijBot: a TF-IDF similarity filter catches greetings,
small talk, off-topic questions, and common FAQs without calling an LLM —
with specific, pre-written answers (not generic filler) for the questions
recruiters actually ask (backend work? data science work? AI/ML work?).
Anything else falls back to an LLM that only answers from Gaurangi's resume
data, instructed to cite real project names and numbers instead of vague
generalities.

## Fastest path to live (you need ~10 minutes of this)

1. Get a free Groq API key: https://console.groq.com/keys (fastest free option)
2. `pip install -r requirements.txt`
3. Create `.streamlit/secrets.toml`:
   ```toml
   LLM_API_KEY = "gsk_..."
   LLM_BASE_URL = "https://api.groq.com/openai/v1"
   LLM_MODEL = "llama-3.3-70b-versatile"
   ```
4. `streamlit run app.py` to test locally
5. Push to GitHub, deploy on https://share.streamlit.io (free), paste the same
   secrets into Settings → Secrets on the deployed app
6. Copy the resulting `https://xxx.streamlit.app` URL into your portfolio's
   "Chat" button (search `REPLACE_WITH_YOUR_STREAMLIT_URL` in `index.html`)

Without an API key configured, the bot still runs and answers anything in
`stored_questions.py` — so you can deploy now and add the key in the next
10 minutes without redeploying your portfolio.

## Files

- `app.py` — Streamlit UI + matching + LLM call logic
- `master_data.py` — all resume content (edit this to update what the bot knows)
- `stored_questions.py` — canned Q&A pairs for the TF-IDF pre-filter
- `requirements.txt` — dependencies

## Other LLM providers

| Provider | LLM_BASE_URL | Example model |
|---|---|---|
| Groq (free tier) | `https://api.groq.com/openai/v1` | `llama-3.3-70b-versatile` |
| OpenAI | `https://api.openai.com/v1` | `gpt-4o-mini` |
| DeepSeek | `https://api.deepseek.com` | `deepseek-chat` |

## Tune the pre-filter

- `stored_questions.py` only holds greetings, thanks, off-topic and troll replies. Real questions about you go to the LLM, which answers from `master_data.py`.
  LLM handling that could be a specific canned answer instead.
- If the bot is matching canned answers too aggressively for real questions,
  raise `SIMILARITY_THRESHOLD` in `app.py` (currently `0.75`, deliberately high so only near-exact greetings and junk get canned replies).

## Update your info

Everything the bot knows lives in `master_data.py` — no other file needs
to change when your resume does.

# Week 12 – Intelligence (Optional) and Deployment – Programming Problems

Tasks 1–7 (the OpenAI assistant) are optional. Install the libraries with `pip install openai python-dotenv` and never commit your API key.

## Task 1: Your First API Call
Load the API key with `python-dotenv`, create an `OpenAI` client and call `client.chat.completions.create` with model `gpt-4o-mini`, a system message ("You are a helpful assistant.") and the user question "In one sentence, what is SQL injection?". Print the reply and the total tokens used.

## Task 2: Understanding the Messages Structure
Build a `messages` list containing a `system`, a `user`, an `assistant` and a second `user` message (e.g. a cybersecurity expert discussing phishing). Print the message count and each role with the first 60 characters of its content. Explain why the full list is sent on every call.

## Task 3: Multi-Turn Console Chat
Write `run_console_chat(system_prompt, client)` that:
- Starts with the system message in a `messages` list.
- Loops, reading user input until the user types `quit`.
- Appends each user message and each assistant reply to the list so the conversation keeps its history.

## Task 4: Prompt Engineering
Write system prompts for all three project domains: **cybersecurity** (incident response analyst), **data science** (data scientist / ML engineer) and **IT operations** (IT operations lead). Each prompt should set the role, the response structure and the priorities of the assistant. Print the length of each prompt.

## Task 5: Combining Database Data with AI
1. Create a sample incident dictionary with `id`, `severity`, `category`, `status` and `description`.
2. Write `build_incident_prompt(incident)` that injects the data into a prompt asking for: root cause analysis, immediate containment actions (bullet points), long-term prevention measures, and a risk assessment (Low / Medium / High / Critical).
3. Print the generated prompt and send it to the API using the cybersecurity system prompt.

## Task 6: Streamlit Chat Page (`pages/4_AI_Assistant.py`)
Build a Streamlit chat page that:
- Has an authentication guard (redirects to `Home.py` if not logged in).
- Reads the API key from `st.secrets["OPENAI_API_KEY"]` (`.streamlit/secrets.toml`).
- Has a sidebar with a domain selector (Cybersecurity / Data Science / IT Operations), a message counter and a **Clear Chat** button.
- Keeps the conversation in `st.session_state.ai_messages` and displays the history with `st.chat_message`.
- Takes new input with `st.chat_input` and streams the reply (`stream=True`) into a placeholder.

## Task 7: Reflection Questions
1. Why must the assistant reply be added to the messages list after each turn?
2. What is the practical difference between `stream=True` and `stream=False`?
3. Why should you NEVER send real user passwords or sensitive data to the OpenAI API?
4. What is LLM hallucination, and why must outputs be validated?

## Task 8: Dependencies

Create a `requirements.txt` listing every package your project needs (e.g. `streamlit`, `pandas`, `bcrypt`, `requests`, `openai`). Check it works by installing from it in a fresh virtual environment.

## Task 9: Keeping Secrets Out of the Repository

Move your API keys into `.streamlit/secrets.toml` (and/or `.env`) and add them to `.gitignore`. Check with `git status` that no secret file is staged.

## Task 10: README

Write a `README.md` with: project description, how to install, how to run, and how to set up the secrets.

## Task 11: Push to GitHub

Create a GitHub repository for your project, commit your work with meaningful messages and push it. Check that the repository contains no passwords, keys or database files with real data.

## Task 12: Deploy to Streamlit Community Cloud

Deploy your app from the GitHub repository to Streamlit Community Cloud, add your secrets in the app settings, and test the public URL (including login and a protected page). Submit the URL.

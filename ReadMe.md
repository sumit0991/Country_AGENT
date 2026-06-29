# 🌍 Country Info AI Agent

An AI-powered Country Information Assistant built using **Python**, **OpenRouter API**, and the **REST Countries API**.

The agent answers country-related questions such as capital, currency, population, languages, continent, and other basic information. It also maintains simple conversation memory so previous interactions can be stored.

---
# LIVE LINK

 - https://countryagent-nxtinzhetkkprhyapzwvpe.streamlit.app/

---
 

# 🚀 Features

- 🌎 Get information about any country
- 🏛️ Capital city
- 💰 Currency
- 👥 Population
- 🗣️ Official language(s)
- 🌍 Continent
- 🧠 Conversation memory
- 🤖 OpenRouter LLM integration
- 🔧 REST Countries API integration

---

# 🛠️ Tech Stack

- Python
- OpenRouter API
- Requests Library
- Python Dotenv
- REST Countries API
- JSON Memory Storage

---


# ⚙️ Installation

## . Clone the Repository

```bash
git clone https://github.com/sumit0991/Country_AGENT.git
cd Country-Info-Agent
```

---

## . Install Dependencies

```bash
pip install -r requirements.txt
```

or

```bash
pip install requests python-dotenv
```

---

# 🔑 OpenRouter API Setup

## Step 1

Visit

https://openrouter.ai

---

## Step 2

Create an account.

---

## Step 3

Generate a free API key.

---

## Step 4

Create a `.env` file in the project folder.

```env
OPENROUTER_API_KEY=your_api_key_here
```

---

# ▶️ Run the Project

```bash
streamlit run app.py
```


---

# 💬 Example Queries

```
Nepal

India

Tell me about Japan

Capital of France

Currency of Canada

Population of Brazil

Languages spoken in Switzerland

Which continent is Australia in?

Tell me about Germany

Capital of Sri Lanka
```

---

# 🧠 How It Works

1. User enters a country-related question.
2. The agent checks whether the question is about a country.
3. The REST Countries API retrieves country information.
4. The retrieved data is sent to the OpenRouter LLM.
5. The LLM generates a clear, natural-language response.
6. The conversation is saved to memory for future interactions.

---

# 📌 APIs Used

## OpenRouter API

Used for generating AI responses.

Documentation:

https://openrouter.ai/docs

---

## REST Countries API

Used for retrieving country information.

Website:

https://restcountries.com/


---


# 📦 Requirements

- Python 3.9+
- requests
- python-dotenv

---

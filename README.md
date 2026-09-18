# 🤖 AI Interviewer

An AI-powered interview application built with **Python, Streamlit, and an open-source LLM**.

The application uses **Llama 3.2** through **Ollama** to generate AI-powered interview interactions.

## 🛠️ Tech Stack

* **Python**
* **Streamlit** — User interface
* **langchain_ollama** — Connects the application to Ollama
* **Llama 3.2** — Open-source LLM
* **Ollama** — Runs the LLM locally
* **uv** — Fast Python package and environment management

## ⚙️ Setup

### 1. Clone the repository

```bash
git clone https://github.com/Tharunluckys/Ai-Interviewer.git
cd Ai-Interviewer
```

### 2. Install dependencies

This project uses **uv** for package management.

```bash
uv sync
```

### 3. Install and run Ollama

Make sure Ollama is installed and running on your system.

Pull the Llama 3.2 model:

```bash
ollama pull llama3.2
```

### 4. Run the application

```bash
uv run streamlit run app.py
```

## 🧠 Model

This project uses **Llama 3.2**, an open-source LLM, through Ollama.

The model runs locally, so the application does not require an external LLM API key.

## 🎯 Project Goal

The goal of this project is to build a simple AI interviewer while learning how to integrate a local open-source LLM with a Streamlit application.

## 👨‍💻 Author

**Tharun Luckys**

GitHub: https://github.com/Tharunluckys

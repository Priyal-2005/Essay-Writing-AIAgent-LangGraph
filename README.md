

# 🧠 Essay Writing AI Agent

An intelligent multi-step AI system that generates high-quality essays using reasoning, research, critique, and refinement.

---

## 🚀 Features

- ✨ Generates structured essays from any topic
- 🔍 Performs web-based research using DuckDuckGo
- 🧠 Breaks down topics into key terms (Planner)
- 📝 Writes a first draft (Drafter)
- 🔍 Critically reviews the draft (Reviewer)
- ✨ Improves and rewrites the essay (Rewriter)
- 📥 Download final essay as a file
- 🎨 Interactive UI using Streamlit

---

## 🏗️ Architecture

```
User Input
   ↓
Planner (Key Terms)
   ↓
Researcher (Web Search)
   ↓
Drafter (First Essay)
   ↓
Reviewer (Critique)
   ↓
Rewriter (Final Essay)
```

---

## 🧰 Tech Stack

- Python
- LangChain
- LangGraph
- Groq API (LLM)
- DuckDuckGo Search
- Streamlit

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone <your-repo-link>
cd essay-ai-agent
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Add your API key

Create a `.env` file and add:

```env
GROQ_API_KEY=your_api_key_here
```

### 4. Run the app

```bash
streamlit run app.py
```

---

## 🖥️ UI Preview

The app includes:
- Topic input field
- Generate button
- Tabs for:
  - 📝 Draft
  - 🔍 Review
  - ✨ Final Essay
- Download option for final essay

---

## 🎯 Use Cases

- Academic essay writing
- Content generation
- Idea structuring
- Learning writing techniques

---

## 📌 Future Improvements

- Add citations and references
- Export as PDF
- Save essay history
- Deploy online

---

## 💡 Author

Built with ❤️ using LangGraph and Groq
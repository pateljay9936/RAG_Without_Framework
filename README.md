# 🧠 Framework-Free RAG: Build a Retrieval-Augmented Generation App from Scratch

By **Jay Patel** — Software Developer | AI Enthusiast

This project demonstrates how to build a fully functioning Retrieval-Augmented Generation (RAG) application **without** using LangChain or LlamaIndex. It leverages:

- 🧾 Local documents (.pdf, .docx, .txt)
- 💬 OpenAI API (GPT-4 or GPT-3.5)
- 🔍 ChromaDB as a vector store
- 🧠 Conversational memory for multi-turn dialogue

---

## 📁 Project Structure

```
rag-from-scratch/
│
├── docs/                # Sample documents (.pdf, .docx, .txt)
├── main.py             # One-file full RAG implementation
├── requirements.txt    # Python dependencies
└── README.md          # You're here!
```

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/pateljay9936/RAG_Without_Framework.git
cd RAG_Without_Framework
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 📄 Supported File Formats

This app processes:

- `.txt` → plain text summaries
- `.pdf` → scanned reports and whitepapers
- `.docx` → internal documentation and company histories

---

## 🚀 How to Use

### 1. Prepare Documents

Add your `.txt`, `.pdf`, and `.docx` files into the `docs/` directory.

### 2. Run the Application

```bash
python main.py
```

### 3. Ask Questions!

You'll be prompted to enter a query like:

```
> When was GreenGrow Innovations founded?
```

And get a response like:

```
Answer: GreenGrow Innovations was founded in 2010.
Sources: GreenGrow Innovations_Company History.docx (chunk 0)
```

---

## ⚙️ Key Features

✅ Document ingestion from local files  
✂️ Smart text chunking (~500 characters)  
🔍 Semantic search with sentence-transformers + ChromaDB  
💬 GPT-4 or GPT-3.5 responses via OpenAI API  
🧠 Conversational memory to handle follow-ups  

---

## 🧪 Sample Queries

- **Q:** When was GreenGrow Innovations founded?
- **Q:** Where is it headquartered?
- **Q:** What is EcoHarvest?
- **Q:** Which companies focus on biotech research?

---

## 🧠 Powered By

- [ChromaDB](https://www.trychroma.com/)
- [Sentence Transformers](https://www.sbert.net/)
- [OpenAI API](https://openai.com/api/)
- Python 3.8+

---

## 🧰 Want to Extend It?

You can plug in:

- Your company's internal documentation
- Custom OpenAI prompts
- LangGraph/agentic memory if you want to scale up later

---

## 📬 Contact

Made with ❤️ by **Jay Patel**

---

*Let me know if you'd like this in a downloadable `.md` file or published to GitHub!*
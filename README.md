# 📄 Intelligent Tax Document Processing System with N8N, Supabase, and AI

This project automates the processing, extraction, classification, and intelligent validation of tax documents using OCR, generative AI, and vector databases, integrating tools like Supabase, N8N, and APIs such as OpenAI.

---

## ✅ Features Implemented

### 1. **File Collection**
- Integration with **Google Drive** to receive documents automatically.
- Supports multiple formats: PDF, image, and audio.

### 2. **Content Extraction**
- **OCR** for PDFs and images (PNG, JPG).
- **Audio transcription** via Whisper (OpenAI).
- **Structured text extraction** using OpenAI models.

### 3. **Storage and Indexing**
- Stores transcripts, raw text, and extracted data in:
  - `documents`
  - `audio_transcripts`
  - `text_inputs`
- Added `embedding` column using **semantic vectors (pgvector)**.
- **Indexing in Supabase** to speed up search and retrieval.

### 4. **RAG (Retrieval-Augmented Generation)**
- Embedding generation using `text-embedding-3-small`.
- Vector similarity search with `embedding <-> $1` SQL.
- Triggers alerts for semantically inconsistent documents.

### 5. **Error Handling & Resilience**
- Implemented:
  - **Exponential backoff** for API retries.
  - **Dead Letter Queue (DLQ)** storing failed attempts in `error_logs`.
  - **Automated alerts** via Slack or Email for critical failures.
- Full error log includes workflow name, node, message, and payload.

### 6. **Security and Compliance**
- Supabase Edge Functions with authentication.
- Planned **rate limiting** and abuse prevention.
- Sensitive data (e.g., SSNs, tax IDs) are masked and treated carefully.

---

## 🚧 Key Challenges Faced

### 1. **N8N Error Trigger Limitations**
- Inconsistent capturing of errors depending on flow path.
- Solution: Use custom `IF` nodes and direct Supabase logging.

### 2. **Pgvector Query Errors**
- Example: `operator does not exist: vector <-> numeric`.
- Solved by using correct vector type and parameterized SQL queries.

### 3. **Dynamic Filename Resolution**
- Confusion when determining which path (audio/text/image) produced the file.
- Solution: Conditional logic or merge nodes with null checks.

---

## 🚀 How to Run
1. Create your database in Supabase and run the SQL queries to create the tables
2. Configure your Supabase Edge Functions as the Supabase API that I've uploaded .
3. Connect N8N to Supabase,OpenAI and Google Drive.
4. Deploy the N8N workflows:
   - OCR + Transcription Extraction + Embeddings + Similarity Search
   - Error Logging & Alerts

---

## 🤖 Where did I use AI
1. To create some shortcodes to improve my time efficiency
2. Solve some errors
3. Edit json data

---

## 📌 Next Steps

- Implement AI-based document classification (e.g., metadata-based).
- Role-based access control (RBAC) for secure APIs.
- Public API rate limiting.
- Add performance dashboards (e.g., Supabase charts).
- Divide the Main Workflow in sub-workflows

---

## 📞 Contact

Developed by: **Lucas Gonzaga**
Linkedin : https://www.linkedin.com/in/devlucasgonz/

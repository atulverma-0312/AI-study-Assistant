# 📚 AI Study Assistant

A Python-based AI Study Assistant built with Streamlit that helps students read, search, summarize, and understand PDF documents using NVIDIA AI.

The project includes a local PDF Document Reader with optional AI-powered summaries and question answering. AI responses are grounded in extracted PDF text, with page citations for factual claims.

## ✨ Features

### PDF Document Reader
- Read PDF documents with selectable text.
- Search for words and phrases inside PDF files.
- Select and read individual PDF pages.
- Upload PDF documents directly through the application.
- Load local PDF files placed beside `project.py`.

### NVIDIA AI Assistant
- Generate summaries of PDF documents.
- Ask questions about uploaded or selected PDF documents.
- Get clear and simple answers suitable for college students.
- AI responses are based on extracted document text.
- Page citations are included for factual claims when using the document reader.

### Additional Features
- Local Streamlit web interface.
- NVIDIA API integration.
- Configurable NVIDIA AI model.
- Support for Windows development environment.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Application development |
| Streamlit | Web application interface |
| NVIDIA AI API | AI summaries and question answering |
| OpenAI Python SDK | NVIDIA-compatible API client |
| Requests | API communication |
| PyPDF | PDF text extraction |
| Python-dotenv | Environment variable configuration |

## 📂 Project Structure

```text
AI-study-Assistant/
│
├── app.py
├── project.py
├── ai.py
├── pdf_reader.py
├── document_reader.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── document_loader/
│   └── PDF files
│
├── .env                 # Local API configuration
└── venv/                # Python virtual environment
```

## ⚙️ Installation on Windows

### 1. Clone the repository

```powershell
git clone https://github.com/atulverma-0312/AI-study-Assistant.git
cd AI-study-Assistant
```

### 2. Activate the virtual environment

If you already have a virtual environment:

```powershell
.\venv\Scripts\Activate.ps1
```

If you need to create one:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```powershell
python -m pip install -r requirements.txt
```

## 🔑 NVIDIA API Configuration

The project uses NVIDIA AI models for document summarization and question answering.

1. Visit the [NVIDIA API Catalog](https://build.nvidia.com/).
2. Generate an NVIDIA API key.
3. Create a `.env` file in the project folder.
4. Add your API key.

```dotenv
NVIDIA_API_KEY=your_nvidia_api_key
```

The PDF Document Reader also accepts `API_KEY` as an alternative environment variable.

### Model Configuration

The PDF Document Reader uses the following default model:

```text
meta/llama-3.3-70b-instruct
```

To customize the document reader model, add the following to `.env`:

```dotenv
NVIDIA_MODEL=your_model_name
```

The NVIDIA API endpoint can also be customized using:

```dotenv
NVIDIA_BASE_URL=https://integrate.api.nvidia.com/v1
```

For the AI Study Assistant, configure the model using the `MODEL` environment variable if supported by your `ai.py` implementation.

**Security:** Never upload `.env` to GitHub. Keep your NVIDIA API key private and revoke any key that has been exposed.

## ▶️ Run the Applications

### AI Study Assistant

```powershell
streamlit run app.py
```

### PDF Document Reader

```powershell
streamlit run project.py
```

After starting Streamlit, open the local URL displayed in your terminal, usually:

```text
http://localhost:8501
```

## 📄 Using the PDF Document Reader

1. Start the document reader.
2. Choose a PDF from the document selector or upload a PDF.
3. Open the Read tab to view extracted page text.
4. Use the Search tab to find words or phrases.
5. Open the Ask AI tab to summarize the document or ask questions.
6. Read the AI response with page references.

PDF files placed beside `project.py` appear in the document selector.

### PDF Limitations

- The maximum supported upload size is 25 MB.
- The reader supports PDFs containing selectable text.
- Scanned-image PDFs require OCR.
- OCR functionality is not included in the current document reader.

## 🧪 Tests

Run the project tests using:

```powershell
python -m unittest
```

## 🔒 Security and Privacy

- Store API keys in `.env`.
- Do not commit `.env` to GitHub.
- Keep virtual environments out of version control.
- Avoid uploading confidential documents to external AI services.
- AI requests send extracted document text to NVIDIA.

## 🚀 Future Improvements

- OCR support for scanned PDFs.
- Improved semantic search.
- Retrieval-Augmented Generation (RAG).
- Automatic quiz and MCQ generation.
- Flashcards for revision.
- Support for multiple documents and study sessions.

## 👨‍💻 Author

**Atul Verma**

GitHub: [atulverma-0312](https://github.com/atulverma-0312)

Repository: [AI-study-Assistant](https://github.com/atulverma-0312/AI-study-Assistant)

---

⭐ If you find this project useful, consider giving it a star on GitHub.



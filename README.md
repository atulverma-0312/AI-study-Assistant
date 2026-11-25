# AI Document Reader

A local Streamlit app for reading and searching PDF files, with optional NVIDIA-powered summaries and question answering. AI responses are grounded in extracted PDF text and include page citations.

## Run on Windows

1. Open a terminal in this folder.
2. Activate the existing virtual environment:

   ```powershell
   .\venv\Scripts\Activate.ps1
   ```

3. Install the project dependencies:

   ```powershell
   python -m pip install -r requirements.txt
   ```

4. Ensure the `.env` file in this folder contains your NVIDIA API key:

   ```text
   API_KEY=your_nvidia_api_key
   ```

   The reader loads `API_KEY` automatically. It also accepts `NVIDIA_API_KEY`.
   The key is not displayed in the interface or written to application logs.

5. Start the app:

   ```powershell
   streamlit run project.py
   ```

PDF files placed beside `project.py` appear in the document selector. You can also upload a PDF in the app (up to 25 MB). The reader supports selectable PDF text; scanned-image PDFs need OCR, which is not included.

The default NVIDIA model is `meta/llama-3.3-70b-instruct`. To customize it, set `NVIDIA_MODEL` in `.env`. Set `NVIDIA_BASE_URL` only when using a compatible alternative endpoint.

## Tests

```powershell
python -m unittest
```

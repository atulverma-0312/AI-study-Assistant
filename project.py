import streamlit as st

from pdf_reader import extract_text_from_pdf
from ai import ask_ai


st.set_page_config(
    page_title="AI Study Assistant",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 AI Study Assistant")
st.write("Your personal AI-powered learning assistant")

st.divider()

st.header("📄 Ask Questions From PDF")

uploaded_file = st.file_uploader(
    "Upload your PDF",
    type=["pdf"]
)

if uploaded_file is not None:

    st.success("PDF uploaded successfully! ✅")

    st.write(
        f"**File:** {uploaded_file.name}"
    )

    # READ PDF
    try:

        pdf_text = extract_text_from_pdf(uploaded_file)

        if not pdf_text.strip():

            st.error(
                "❌ No readable text found in this PDF."
            )

        else:

            st.info(
                f"PDF contains approximately {len(pdf_text)} characters."
            )

            # Optional: show extracted text
            with st.expander("📖 View Extracted PDF Text"):

                st.text(
                    pdf_text[:10000]
                )

            st.divider()

            # QUESTION
            question = st.text_input(
                "❓ Ask a question from your PDF",
                placeholder="Example: What is Data Science?"
            )

            if st.button("🤖 Get Answer"):

                if not question.strip():

                    st.warning(
                        "Please enter a question."
                    )

                else:

                    with st.spinner(
                        "NVIDIA AI is generating the answer..."
                    ):

                        try:

                            # IMPORTANT:
                            # Pass BOTH question and PDF text
                            answer = ask_ai(
                                question,
                                pdf_text
                            )

                            st.subheader(
                                "🤖 AI Answer"
                            )

                            st.markdown(
                                answer
                            )

                        except Exception as e:

                            st.error(
                                f"PDF Error: {e}"
                            )

    except Exception as e:

        st.error(
            f"PDF Reading Error: {e}"
        )


st.divider()

st.caption(
    "AI Study Assistant | Python + Streamlit + PyPDF + NVIDIA NIM"
)
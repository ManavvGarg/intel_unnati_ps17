import streamlit as st

def app():
    st.title("Contract Analysis Results")

    if "analysis_result" not in st.session_state:
        st.warning("No analysis results available. Please upload and analyze documents first.")
        return

    result = st.session_state.analysis_result

    st.header("Classified Clauses")
    for clause, classification in result["classified_clauses"]:
        st.subheader(f"Classification: {classification}")
        st.write(clause)

    st.header("Named Entities")
    for entity, label in result["entities"]:
        st.write(f"{entity}: {label}")

    st.header("Template Similarity")
    st.write(f"Similarity score: {result['template_similarity']:.2f}")

    st.header("Differences Highlighted")
    st.write(result["differences"])

    st.header("Summary")
    st.write(result["summary"])
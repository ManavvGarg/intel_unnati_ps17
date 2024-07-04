import streamlit as st
import requests

def app():
    st.title("Upload Documents")

    contract_file = st.file_uploader("Upload Contract", type=["pdf", "docx"])
    template_file = st.file_uploader("Upload Template", type=["pdf", "docx"])

    if st.button("Analyze") and contract_file and template_file:
        files = {
            "contract": contract_file,
            "template": template_file
        }
        response = requests.post("http://localhost:8000/api/analyze_contract", files=files)
        
        if response.status_code == 200:
            st.session_state.analysis_result = response.json()
            st.success("Analysis complete! Go to the Contract Analysis page to view results.")
        else:
            st.error("An error occurred during analysis.")
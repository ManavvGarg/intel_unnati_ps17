import streamlit as st
import requests
from components.visualizations import show_visualizations

st.set_page_config(page_title="Contract Validation", page_icon=":memo:")

st.title("Contract Validation System")

menu = ["Home", "Upload Documents", "Analysis", "Comparison"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Home":
    st.subheader("Home")
    st.write("Welcome to the Contract Validation System.")

elif choice == "Upload Documents":
    st.subheader("Upload Documents")

    original_file = st.file_uploader("Upload Original Document", type=["pdf", "docx", "txt"])
    modified_file = st.file_uploader("Upload Modified Document", type=["pdf", "docx", "txt"])
    use_template = st.checkbox("Use Predefined Template")
    template_file = None
    if not use_template:
        template_file = st.file_uploader("Upload Template Document", type=["pdf", "docx", "txt"])

    if st.button("Compare Documents"):
        if original_file and modified_file:
            files = {
                "original_file": original_file.getvalue(),
                "modified_file": modified_file.getvalue(),
            }
            if template_file:
                files["template_file"] = template_file.getvalue()

            response = requests.post("http://localhost:8000/compare/", files=files)
            if response.status_code == 200:
                result = response.json()
                st.session_state["result"] = result
                st.success("Documents compared successfully. Check Analysis and Comparison sections for results.")
            else:
                st.error("Failed to compare documents.")

elif choice == "Analysis":
    st.subheader("Analysis")
    result = st.session_state.get("result", None)
    if result:
        deviations = result.get("deviations", {})
        show_visualizations(deviations)

        st.subheader("Named Entity Recognition")
        st.write("### Original Document Entities")
        st.json(result.get("original_entities", []))
        st.write("### Modified Document Entities")
        st.json(result.get("modified_entities", []))

        st.subheader("Summarization")
        st.write("### Original Document Summary")
        st.write(result.get("original_summary", ""))
        st.write("### Modified Document Summary")
        st.write(result.get("modified_summary", ""))

        st.subheader("Sentiment Analysis")
        st.write("### Original Document Sentiment")
        st.json(result.get("original_classification", {}))
        st.write("### Modified Document Sentiment")
        st.json(result.get("modified_classification", {}))
    else:
        st.warning("Please upload and compare documents first.")

elif choice == "Comparison":
    st.subheader("Comparison")
    result = st.session_state.get("result", None)
    if result:
        deviations = result.get("deviations", {})
        st.write("### Detailed Comparison")
        for key, value in deviations.items():
            if value["original"] != value["modified"]:
                st.write(f"#### Clause: {key}")
                st.write(f"**Original:** {value['original']}")
                st.write(f"**Modified:** {value['modified']}")
                if value["template"]:
                    st.write(f"**Template:** {value['template']}")
                st.write("---")
    else:
        st.warning("Please upload and compare documents first.")

# Business Contract Validation

## Project Overview

This project focuses on classifying content within contract clauses and identifying deviations from a template. It utilizes NLP techniques including Named Entity Recognition (NER), semantic analysis, and sentiment classification to achieve contract validation. The system highlights discrepancies between contract clauses and predefined templates, aiding in efficient contract management and compliance.

## Run Instructions

### Backend:

1. **Navigate to the backend directory:**
   ```
   cd backend/
   ```

2. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

3. **Run the FastAPI server:**
   ```
   uvicorn app.main:app --reload
   ```

### Frontend:

1. **Navigate to the frontend directory:**
   ```
   cd frontend/
   ```

2. **Run the Streamlit app:**
   ```
   streamlit run app.py
   ```

   - The Streamlit application will start running in your default browser.

## Usage

- **Backend**: Handles backend processes including NLP-based contract clause analysis, deviation checking, and API endpoints for frontend interaction.
  
- **Frontend**: Provides a user-friendly interface via Streamlit for visualizing contract deviations, highlighting clauses, and facilitating manual review and validation.

## Dependencies

- Python 3.x
- FastAPI
- Streamlit
- Transformers (for NLP tasks)
- Other dependencies as listed in `requirements.txt`

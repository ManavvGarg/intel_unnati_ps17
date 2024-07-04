import streamlit as st
import plotly.graph_objs as go

def show_deviations_chart(deviations):
    keys = list(deviations.keys())
    original_values = [deviations[key]["original"] for key in keys]
    modified_values = [deviations[key]["modified"] for key in keys]
    template_values = [deviations[key]["template"] for key in keys if deviations[key]["template"]]

    fig = go.Figure(data=[
        go.Bar(name='Original', x=keys, y=original_values, marker_color='blue'),
        go.Bar(name='Modified', x=keys, y=modified_values, marker_color='red'),
    ])

    if template_values:
        fig.add_trace(go.Bar(name='Template', x=keys, y=template_values, marker_color='green'))

    fig.update_layout(barmode='group', title="Document Clause Deviations")
    st.plotly_chart(fig)

def show_deviations_summary(deviations):
    total_clauses = len(deviations)
    total_deviations = sum(1 for key, value in deviations.items() if value["original"] != value["modified"])

    st.write(f"Total Clauses: {total_clauses}")
    st.write(f"Total Deviations: {total_deviations}")

    st.subheader("Detailed Deviations")
    for key, value in deviations.items():
        if value["original"] != value["modified"]:
            st.write(f"Clause: {key}")
            st.write(f"Original: {value['original']}")
            st.write(f"Modified: {value['modified']}")
            if value["template"]:
                st.write(f"Template: {value['template']}")
            st.write("---")

def show_visualizations(deviations):
    show_deviations_summary(deviations)
    show_deviations_chart(deviations)

import streamlit as st
from dash_pages.multipage import MultiPage

# load pages scripts
from dash_pages.page_1_project_summary import project_summary_body
from dash_pages.page_2_study_findings import study_findings
from dash_pages.page_3_mildew_detector import page_mildew_detector_body
from dash_pages.page_4_project_hypothesis import page_project_hypothesis_body
from dash_pages.page_5_ml_performance import page_ml_performance_metrics

app = MultiPage(app_name="Mildew detector")  # Create an instance of the app

# Add your app pages here using .add_page()
app.add_page("Project Summary", project_summary_body)
app.add_page("Study Findings", study_findings)
app.add_page("Mildew Detection", page_mildew_detector_body)
app.add_page("Project Hypothesis", page_project_hypothesis_body)
app.add_page("ML Performance Metrics", page_ml_performance_metrics)

app.run()  # Run the app
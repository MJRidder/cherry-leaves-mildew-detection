import streamlit as st
import matplotlib.pyplot as plt

def page_project_hypothesis_body():
    st.write("### Project Hypothesis and Validation")

    st.success(
        f"**Hypothesis 1:**\n\n"
        f"It is visibly possible to differintiate a healthy leave, from a leave containing powdery mildew.\n\n"
        
        f"*Validation:*\n"
        f"review images and determine whether there are specific indicators that can be viewed, "
        f"determining if a leave is healthy or containing powdery mildew.\n\n"
        )
    st.success(
        f"**Hypothesis 2:**\n\n"
        f"Based on visible indicators, it can be predicted with a 97% accuracy if a leave is healthy, "
        f"or containing powdery mildew.\n\n"
        
        f"*Valitation:*\n"
        f"A CNN model will be trained, tested and used on a validation set of images to determine "
        f"if this is possible.\n\n"
        )
    st.success(        
        f"**Hypothesis 3:**\n\n"
        f"By using a trained CNN model, time spend & costs for cherry leaves health checks can be "
        f"drastically reduced.\n\n"
        
        f"*Validation:*\n"
        f"Taking in account the time/cost needed to make pictures, upload them and have the CNN model "
        f"run over them, a comparison can be made between these actions and the 30 minutes per tree "
        f"that it costs today to verify if a Cherry tree is healthy, or infected with Mildew."
        )
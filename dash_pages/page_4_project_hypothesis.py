import streamlit as st
import matplotlib.pyplot as plt


def page_project_hypothesis_body():
    st.write("### Project Hypothesis and Validation")

    st.success(
        f"**Hypothesis 1:**\n\n"
        f"It is visibly possible to differintiate a healthy leave, from a "
        f"leave containing powdery mildew.\n\n"

        f"*Validation:*\n"
        f"review images and determine whether there are specific indicators "
        f"that can be viewed, determining if a leave is healthy or "
        f"containing powdery mildew.\n\n"
        )
    st.warning(
        f"This hypothesis can be considered validated. It is indeed possible "
        f"to use visual cues to indicate whether a cherry leave is healthy "
        f"or if it contains the powdery mildew. The study shows that: \n\n"

        f"* Healthy leaves are of a consistant and brighter green color, "
        f"with strong lines (veines) and texture.\n"
        f"* Leaves with mildew do not have a consistant green color "
        f"(irregular), have unclear lines and have visually white collored "
        f"textures, covering the leaves. This is also more prudent in the "
        f"veins of the leaves.\n"

        f"These visual cues can be seen by the human eye and can be used "
        f"for training ML models."
    )

    st.success(
        f"**Hypothesis 2:**\n\n"
        f"Based on visible indicators, it can be predicted with a 97% "
        f"accuracy if a leave is healthy, or containing powdery mildew.\n\n"

        f"*Valitation:*\n"
        f"A CNN model will be trained, tested and used on a validation set "
        f"of images to determine if this is possible.\n\n"
        )
    st.warning(
        f"This hypothesis can be considered validated. The tool that was "
        f"created can predict, when using images of cherry leaves,  with a "
        f"degree of 99% accuracy whether the leave in the image is healthy "
        f"or if it was infected with the mildew fungus."
    )

    st.success(
        f"**Hypothesis 3:**\n\n"
        f"By using a trained CNN model, time spend & costs for cherry leaves "
        f"health checks can be drastically reduced.\n\n"

        f"*Validation:*\n"
        f"Taking in account the time/cost needed to make pictures, upload "
        f"them and have the CNN model run over them, a comparison can be made "
        f"between these actions and the 30 minutes per tree that it costs "
        f"today to verify if a Cherry tree is healthy, or infected with "
        f"Mildew."
        )
    st.warning(
        f"This hypothesis can not yet be considered fully validated. But it "
        f"is still the expectation that it will be. Looking at the time spend "
        f"when using the tool (and the ability to review batches of images at "
        f"the same time), it would require only an economical beneficial way "
        f"to collect and upload the images to make this approach financially "
        f"more beneficial, than the current manual way of working. "
    )

    st.write(
        f"* For additional information, please visit and **read** the "
        f"[Project README file](https://github.com/MJRidder/cherry-leaves-mildew-detection/blob/main/README.md).\n\n")  #noqa

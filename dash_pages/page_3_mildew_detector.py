import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd

from src.data_management import download_dataframe_as_csv
from src.machine_learning.predictive_analysis import (
                                                    load_model_and_predict,
                                                    resize_input_image,
                                                    plot_predictions_proba
                                                    )


def page_mildew_detector_body():
    st.info(
        f"The client is interested in predicting if a cherry leaf is healthy "
        f"or contains powdery mildew. This page allows you to upload images "
        f"of cherry leaves to have the model predict whether the leaves in "
        f"the image are healthy or contain powdery mildew."
        )

    st.write(
        f"* You can download a set of leaves that are healthy, or that "
        f"contain powdery mildew for live prediction. \n"
        f"You can download the images from [here]"
        F"(https://www.kaggle.com/datasets/codeinstitute/cherry-leaves/data)."
        )

    st.write(
        f"* For additional information, please visit and **read** the "
        f"[Project README file]"
        f"(https://github.com/MJRidder/cherry-leaves-mildew-detection/blob/main/README.md).\n\n")  #noqa

    st.write("---")

    images_buffer = st.file_uploader(
        'Upload cherry leaves. You may select more than one.',
        type='png', accept_multiple_files=True)

    if images_buffer is not None:
        df_report = pd.DataFrame([])
        for idx, image in enumerate(images_buffer):

            img_pil = (Image.open(image))
            st.info(f"Cherry leave: **{image.name}**")
            img_array = np.array(img_pil)
            st.image(
                img_pil, caption=(
                    f"Image Size: {img_array.shape[1]}"
                    f"px width x {img_array.shape[0]}px height"))

            version = 'v1'
            resized_img = resize_input_image(img=img_pil, version=version)
            pred_proba, pred_class = load_model_and_predict(
                resized_img, version=version)
            plot_predictions_proba(pred_proba, pred_class, key=idx)

            df_report = df_report._append(
                {"Name": image.name, 'Result': pred_class}, ignore_index=True)

        if not df_report.empty:
            st.success("Analysis Report")
            st.table(df_report)
            st.markdown(
                download_dataframe_as_csv(df_report), unsafe_allow_html=True)

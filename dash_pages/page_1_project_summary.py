import streamlit as st
import matplotlib.pyplot as plt


def project_summary_body():

    st.write("### Project Summary")

    st.info(
        f"**General Information**\n\n"
        f"Powdery mildew on cherry trees is a fungal disease characterized by"
        f"a white, powdery coating on leaves, shoots, and sometimes fruit. It"
        f"can cause leaf distortion, stunted growth, and blemishes on the "
        f"fruit. The fungus thrives in warm, humid conditions and can "
        f"overwinter on the tree or in fallen leaves.\n\n"

        f"*Symptoms include:*\n\n"
        f"*- Leaves:* White, powdery or felt-like fungal growth, often "
        f"appearing on the underside of leaves. Severely affected leaves may "
        f"become distorted, curled, or yellowed.\n\n"
        f"*- Shoots:* New shoots may be shorter than normal and covered in "
        f"white powdery mildew.\n\n"
        f"*- Fruit:* White powdery bloom on ripening fruit or slightly "
        f"depressed, circular areas on the fruit surface.\n\n"

        f"**Project Dataset**\n"
        f"* The available dataset contains a total of 4208 images, equally "
        f"split into two classes: **healthy** and **powdery_mildew**. "
        f"Each class contains 2104 images.\n"
        f"* The images are of cherry leaves, taken in various conditions, "
        f"and are stored in a folder structure that separates the two "
        f"classes.\n")

    st.success(
        f"The project has 2 business requirements:\n"
        f"* The client is interested in conducting a study to visually "
        f"differentiate a cherry leaf that is healthy from one that contains "
        f"white powdery mildew.\n"
        f"* The client is interested in predicting if a cherry leaf is "
        f"healthy or contains powdery mildew.")

    st.write(
        f"* For additional information, please visit and **read** the "
        f"[Project README file](https://github.com/MJRidder/cherry-leaves-mildew-detection/blob/main/README.md).\n\n")  #noqa

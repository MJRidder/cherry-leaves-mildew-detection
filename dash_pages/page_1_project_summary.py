import streamlit as st
import matplotlib.pyplot as plt

def project_summary_body():

    st.write("### Project Summary")

    st.info(
        f"**General Information**\n\n"
        f"Powdery mildew on cherry trees is a fungal disease characterized by a white, "
        f"powdery coating on leaves, shoots, and sometimes fruit. It can cause leaf "
        f"distortion, stunted growth, and blemishes on the fruit. The fungus thrives in "
        f"warm, humid conditions and can overwinter on the tree or in fallen leaves.\n\n"

        f"*Symptoms include:*\n\n"
        f"*- Leaves:* White, powdery or felt-like fungal growth, often appearing on the "
        f"underside of leaves. Severely affected leaves may be puckered or distorted.\n\n" 
        f"*- Shoots:* New shoots may be shorter than normal and covered in the white mildew.\n\n" 
        f"*- Fruit:* White powdery bloom on ripening fruit or slightly depressed, circular "
        f"areas on the fruit surface.\n\n"

        f"**Project Dataset**\n"
        f"* The available dataset contains a total of 4208 images, equally split into "
        f"two classes: **healthy** and **powdery_mildew**. each class containing "
        f"2104 images.\n"
        f"* The images are of cherry leaves, taken in various conditions, and are "
        f"stored in a folder structure that separates the two classes.\n")
        

    st.write(
        f"* For additional information, please visit and **read** the "
        f"[Project README file](https://github.com/MJRidder/cherry-leaves-mildew-detection/blob/main/README.md).\n\n")
    

    st.success(
        f"The project has 2 business requirements:\n"
        f"* The client is interested in conducting a study to visually differentiate "
        f"a cherry leaf that is healthy from one that contains powdery mildew.\n"
        f"* The client is interested in predicting if a cherry leaf is healthy or "
        f"contains powdery mildew.")
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.image import imread
from src.machine_learning.evaluate_clf import load_test_evaluation

def page_ml_performance_metrics():
    version = 'v1'

    st.write("### Train, Validation and Test Set: Labels Frequencies")

    labels_distribution = plt.imread(f"outputs/{version}/labels_distribution.png")
    st.image(labels_distribution, caption='Labels Distribution on Train, Validation and Test Sets')

    st.warning(
    "The data was prepared and divided as follows:\n"
    "- Train: 70%\n"
    "- Test: 20%\n"
    "- Validation: 10%"
    )
    st.write("---")


    st.write("### Model History")
    col1, col2 = st.columns(2)
    with col1: 
        model_acc = plt.imread(f"outputs/{version}/model_training_acc.png")
        st.image(model_acc, caption='Model Training Accuracy')
    with col2:
        model_loss = plt.imread(f"outputs/{version}/model_training_losses.png")
        st.image(model_loss, caption='Model Training Losses')

    st.warning(
    "The model was trained various times with different combinations of with loss functions and "
    "optimizers. Finally getting the best results with the following settings:\n"
    "- Loss: binary_crossentropy\n"
    "- Optimizer: Adam\n"
    "- Activation function: relu & sigmoid\n\n"
    "Other settings that were reviewed, but did not provide better results:\n"
    "- *Loss functions:* categorical_crossentropy\n"
    "- *Optimizers:* Adagrad, RMSprop, Adelta\n"
    "- *Activation functions:* Softmax\n"
    )
    st.write("---")

    st.write("### Generalised Performance on Test Set")
    st.dataframe(pd.DataFrame(load_test_evaluation(version), index=['Loss', 'Accuracy']))
    st.warning(
    "The model shows an accuracy of over 99%, which is well above the "
    "requested 97% by the client."
    )
    st.write("### Confusion Matrix")
    model_clf = plt.imread(f"outputs/{version}/confusion_matrix.png")
    st.image(model_clf, caption='Classification Report')  

    st.warning(
        "The confusion matrix shows a good accuracy in predicting status. "
    )
    st.write("---")

    st.write(
    f"For additional information, please visit and **read** the "
    f"[Project README file](https://github.com/MJRidder/cherry-leaves-mildew-detection/blob/main/README.md).")
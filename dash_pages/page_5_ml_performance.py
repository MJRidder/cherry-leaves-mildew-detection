import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.image import imread
from src.machine_learning.evaluate_clf import load_test_evaluation


def page_ml_performance_metrics():
    version = 'v1'

    st.write(
        f"### Train, Validation and Test Set: Labels Frequencies")

    labels_distribution = plt.imread(
        f"outputs/{version}/labels_distribution.png")
    st.image(
        labels_distribution,
        caption='Labels Distribution on Train, Validation and Test Sets')

    st.warning(
        f"The data was prepared and divided as follows:\n"
        f"- Train: 70%\n"
        f"- Test: 20%\n"
        f"- Validation: 10%"
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
        f"The model was trained various times with different combinations of "
        f"with loss functions and optimizers. Finally getting the best "
        f"results with the following settings:\n"
        f"- Loss: binary_crossentropy\n"
        f"- Optimizer: Adam\n"
        f"- Activation function: relu & sigmoid\n\n"
        f"Other settings that were reviewed, "
        f"but did not provide better results:\n"
        f"- *Loss functions:* categorical_crossentropy\n"
        f"- *Optimizers:* Adagrad, RMSprop, Adelta\n"
        f"- *Activation functions:* Softmax\n"
    )
    st.write("---")

    st.write("### Generalised Performance on Test Set")
    st.dataframe(pd.DataFrame(
        load_test_evaluation(version), index=['Loss', 'Accuracy']))
    st.warning(
        f"The model shows an accuracy of over 99%, which is well above the "
        f"requested 97% by the client."
    )
    st.write("### Confusion Matrix")
    model_clf = plt.imread(f"outputs/{version}/confusion_matrix.png")
    st.image(model_clf, caption='Classification Report')

    st.warning(
        f"The confusion matrix shows a good accuracy in predicting status. "
    )
    st.write("---")

    st.write(
        f"For additional information, please visit and **read** the "
        f"[Project README file]"
        f"(https://github.com/MJRidder/cherry-leaves-mildew-detection/blob/main/README.md).")  # noqa

import streamlit as st
import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.image import imread

import itertools
import random

def leaves_visualizer_body():
    st.write("### Leaves Visualizer")
    st.info(
        f"**ASK:** Provide the insights to visually differentiate "
        f"a cherry leaf that is healthy from one that contains powdery mildew.\n")
    
    st.write(
        f"* For additional information, please visit and **read** the "
        f"[Project README file](https://github.com/MJRidder/cherry-leaves-mildew-detection/blob/main/README.md).\n\n")
    
    st.success("The first business requirement was to establish a visual difference "
               "between a healthy leaf and one that contains powdery mildew. To put "
               "this into practices, 4208 images were collected and reviewed, 50% "
               "of which were confirmed healthy leaves and 50% of which contained "
               "powdery mildew.\n\n"
               "Data analysis has been carried out based on these images to determine "
               "the difference between average and variability images, as well as "
               "to create a montage.")

    version = 'v1'
    if st.checkbox("Difference between average and variability image"):
      
      avg_healthy = plt.imread(f"outputs/{version}/avg_var_healthy.png")
      avg_powdery_mildew = plt.imread(f"outputs/{version}/avg_var_powdery_mildew.png")

      st.warning(
        "* Healthy leaves are of a consistant and brighter green color, with strong "
        "lines and texture.\n"
        "* Leaves with mildew do not have a consistant green color (irregular), have "
        "unclear lines and have visually white collored textures, covering the leaves. "
        "This is also more prudent in the veins of the leaves.")

      st.image(avg_healthy, caption='Healthy leaf - Average and Variability')
      st.image(avg_powdery_mildew, caption='Leaf with powdery mildew - Average and Variability')
      
      st.write("---")

    if st.checkbox("Differences between an average leaf that is healthy and one that contains powdery mildew"):
          diff_between_avgs = plt.imread(f"outputs/{version}/avg_diff.png")

          st.warning(
            f"* We notice this study didn't show "
            f"patterns where we could intuitively differentiate one from another.")
          st.image(diff_between_avgs, caption='Difference between average images')

    if st.checkbox("Image Montage"): 
      st.write("* To refresh the montage, click on the 'Create Montage' button")
      my_data_dir = 'inputs/cherry-leaf-dataset/cherry-leaves'
      labels = os.listdir(my_data_dir+ '/validation')
      label_to_display = st.selectbox(label="Select label", options=labels, index=0)
      if st.button("Create Montage"):      
        image_montage(dir_path= my_data_dir + '/validation',
                      label_to_display=label_to_display,
                      nrows=8, ncols=3, figsize=(10,25))
      st.write("---")



def image_montage(dir_path, label_to_display, nrows, ncols, figsize=(15,10)):
  sns.set_style("white")
  labels = os.listdir(dir_path)

  # subset the class
  if label_to_display in labels:

    images_list = os.listdir(dir_path+'/'+ label_to_display)
    if nrows * ncols < len(images_list):
      img_idx = random.sample(images_list, nrows * ncols)
    else:
      print(
          f"Decrease nrows or ncols to create your montage. \n"
          f"There are {len(images_list)} in your subset. "
          f"You requested a montage with {nrows * ncols} spaces")
      return
    

    # create list of axes indices based on nrows and ncols
    list_rows= range(0,nrows)
    list_cols= range(0,ncols)
    plot_idx = list(itertools.product(list_rows,list_cols))


    # create a Figure and display images
    fig, axes = plt.subplots(nrows=nrows,ncols=ncols, figsize=figsize)
    for x in range(0,nrows*ncols):
      img = imread(dir_path + '/' + label_to_display + '/' + img_idx[x])
      img_shape = img.shape
      axes[plot_idx[x][0], plot_idx[x][1]].imshow(img)
      axes[plot_idx[x][0], plot_idx[x][1]].set_title(f"Width {img_shape[1]}px x Height {img_shape[0]}px")
      axes[plot_idx[x][0], plot_idx[x][1]].set_xticks([])
      axes[plot_idx[x][0], plot_idx[x][1]].set_yticks([])
    plt.tight_layout()
    
    st.pyplot(fig=fig)

  else:
    print("The label you selected doesn't exist.")
    print(f"The existing options are: {labels}")

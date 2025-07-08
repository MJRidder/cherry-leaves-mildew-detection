![header_image](/images/readme/readme-cherry-leaves-banner.png)

# Mildew detection tool for cherry leaves

# Introduction
The cherry plantation crop from Farmy & Foods is facing a challenge where their cherry plantations have been presenting powdery mildew. Currently, the process is manual verification if a given cherry tree contains powdery mildew. An employee spends around 30 minutes in each tree, taking a few samples of tree leaves and verifying visually if the leaf tree is healthy or has powdery mildew. If there is powdery mildew, the employee applies a specific compound to kill the fungus. The time spent applying this compound is 1 minute. The company has thousands of cherry trees located on multiple farms across the country. As a result, this manual process is not scalable due to the time spent in the manual process inspection.

To save time in this process, the IT team suggested an ML system that detects instantly, using a leaf tree image, if it is healthy or has powdery mildew. A similar manual process is in place for other crops for detecting pests, and if this initiative is successful, there is a realistic chance to replicate this project for all other crops. The dataset is a collection of cherry leaf images provided by Farmy & Foods, taken from their crops.

### Deployed version at https://cherry-leaves-mildew-detection.onrender.com/


# Table of Contents
- [Mildew detection tool for cherry leaves](#mildew-detection-tool-for-cherry-leaves)
- [Introduction](#introduction)
    - [Deployed version at https://cherry-leaves-mildew-detection.onrender.com/](#deployed-version-at-httpscherry-leaves-mildew-detectiononrendercom)
- [Table of Contents](#table-of-contents)
  - [Dataset Content](#dataset-content)
  - [Business Requirements](#business-requirements)
  - [Hypothesis and validation](#hypothesis-and-validation)
  - [Rationale for ML model](#rationale-for-ml-model)
  - [Implementation of the Business Requirements](#implementation-of-the-business-requirements)
  - [ML Business case](#ml-business-case)
  - [Dashboard design](#dashboard-design)
  - [(Un)fixed Bugs](#unfixed-bugs)
  - [Deployment](#deployment)
    - [Render](#render)
    - [](#)
    - [Making a local clone](#making-a-local-clone)
  - [Technologies used](#technologies-used)
    - [Main Data Analysis and Machine Learning Libraries](#main-data-analysis-and-machine-learning-libraries)
  - [Testing](#testing)
    - [Manual testing](#manual-testing)
    - [PEP](#pep)
  - [Credits](#credits)
    - [Content](#content)
    - [Media](#media)
  - [Acknowledgements (optional)](#acknowledgements-optional)
- [NOTES AND OTHERS](#notes-and-others)
    - [Business Case understanding and ML validation](#business-case-understanding-and-ml-validation)
  - [ML Business Case](#ml-business-case-1)
  - [The rationale to map the business requirements to the Data Visualisations and ML tasks](#the-rationale-to-map-the-business-requirements-to-the-data-visualisations-and-ml-tasks)

## Dataset Content

- The dataset is sourced from [Kaggle](https://www.kaggle.com/datasets/codeinstitute/cherry-leaves/) and contains 4208 images of cherry leaves images. The images are split into two classes: healthy leaves and leaves that contain Mildew, a generally white powdery substance which can be found on the leaves. This type of fungal disease can affect many plant species, which makes this project valuable across the agricultural sector.

Overall the images are of a good quality and have normal (RGB) colors. The dataset was collected to train a machine learning model which could be used to predict whether the leaf on the image is healthy or would contain the powdery mildew.

The cherry plantation crop is one of the finest products in their portfolio, and the company is concerned about supplying the market with a compromised quality product.


- The dataset contains +4 thousand images taken from the client's crop fields. The images show healthy cherry leaves and cherry leaves that have powdery mildew, a fungal disease that affects many plant species. 

[Back to top ⇧](#table-of-contents)

## Business Requirements

Marianne McGuineys, the head of IT and Innovation at Farmy & Foods, a company in the agricultural sector that produces and harvests different types of food. Is facing a challenge where their cherry plantations have been presenting powdery mildew, which is a fungal disease that affects a wide range of plants.

The IT team first of all is interested in completing a study that can clearly show the differences between a Healthy cherry leave and one that contains powdery mildew. For this they are hoping to find visual indicators. They are also looking to create a realable tool that is capable of detecting instantly, using a tree leaf image, if it is healthy or has powdery mildew (Business Requirement 2). This tool needs to have a degree of accuracy of at least 97% for it to be relevant to the client.

The client already has done the work and assembled 4208 images of cherry leaves, of which 2104 are images of healthy leaves and 2104 images are of images containing powdery mildew. To make the tool useable for real life application, they require an online dashboard that provides information and allows them to upload images of leaves, predicting whether these leaves are healthy or infected. As part of their NDA, this dashboard and its content will only be made accessable to Farmy & Foods.

This project is essential to Farmy & Foods as it will allow them to ensure that they do not compromise the quality of their main product and continue to supply the market with high quality product.

Summarized:
1. Create an understanding of the visual differences between healty leaves and leaves containing the mildew fungus.
2. Create a tool that can predict with at least a 97% accuracy whether a leave is healthy or infected.
3. Make this information avaialbe in an easy to use dashboard.

[Back to top ⇧](#table-of-contents)

## Hypothesis and validation

**Hypothesis 1:**
It is possible through visual cues to differintiate a healthy cherry leave, from a cherry leave containing powdery mildew.

Valitation:
review images and determine whether there are specific indicators that can be viewed, determining if a leave is healthy or containing powdery mildew.

This hypothesis can be considered validated. It is indeed possible to use visual cues to indicate whether a cherry leave is healty or if it contains the powdery mildew. The study shows that: 

* Healthy leaves are of a consistant and brighter green color, with strong lines (veines) and texture.
* Leaves with mildew do not have a consistant green color (irregular), have unclear lines and have visually white collored textures, covering the leaves. This is also more prudent in the veins of the leaves.

These visual cues can be seen by the human eye and can be used for training ML models.

Healthy cherry leaves
![healthy_cherry_leaves](./images/readme/readme-images-cherry-leaves-healthy.png)

Cherry leaves containing Mildew
![infected_cherry_leaves](./images/readme/readme-images-cherry-leaves-powdery-mildew.png)

As part of the first business requirement, it was also requested to provide average images and variability images for each class (healthy or powdery mildew).

Average and Variability images for healthy leaves

![infected_cherry_leaves](./images/readme/readme-images-avg-and-variability-healthy-leaves.png) 

Average and Variability images for infected leaves (containing powdery mildew)

![infected_cherry_leaves](./images/readme/readme-images-avg-and-variability-infected-leaves.png) 

**Hypothesis 2**
Based on visible indicators, it can be predicted with a 97% accuracy if a leave is healthy, or containing powdery mildew.

Valitation:
A CNN model will be trained, tested and used on a validation set of images to determine if this is possible.

This hypothesis can be considered validated. The tool that was created can predict, when using images of cherry leaves,  with a degree of 99% accuracy whether the leave in the image is healthy or if it was infected with the mildew fungus.

**Hypothesis 3**
By using a trained CNN model, time spend & costs for cherry leaves health checks can be drastically reduced.

Validation:
Taking in account the time/cost needed to make pictures, upload them and have the CNN model run over them, a comparison can be made between these actions and the 30 minutes per tree that it costs today to verify if a Cherry tree is healthy, or infected with Mildew.

This hypothesis can not yet be considered fully validated. But it is still the expectation that it will be. Looking at the time spend when using the tool (and the ability to review batches of images at the same time), it would require only an economical beneficial way to collect and upload the images to make this approach financially more beneficial, than the current manual way of working. 

[Back to top ⇧](#table-of-contents)

## Rationale for ML model

The client has a very valid rationale for using a machine learning model to help their need for quality control. The current time spend on each tree, is 30 minutes. This is done manually by a specialist. A specialty that needs to be taugt to the individual and needs to be taught to several as this can not be done by one person. They are reliant on wheather, time and the required skills. By training a model to detect the mildew fungus on leaves, the work can be done by many, also without extensive training. Pictures would need to be collected, documented correctly and uploaded. But this can be done at any time of the day, in any weather, effectively by anyone.

Practically, they have also taken the time to create a sufficiently large data set of healthy and infected leaves which would have been the largest cost (time/work) in this process for them. By using the created CNN model, quality checks can be done online to ensure that what the model indicates as healthy or infected, is still correct. Additionally the model could be used and trained on leaves of other plants/trees that they have in their portfolio, allowing them to save further time and work.

Essentially for Farmy Foods going forward is creating a reliable workflow of collecting leaf images of their trees/plants, a way to upload, document and track them. This to ensure they know which tree was determined healty/infected at which specific time and place. This is however outside of the scope of this machine learning project and would be an advice to the client directly.

[Back to top ⇧](#table-of-contents)

## Implementation of the Business Requirements

**1. Information gathering and data collection.**
  - As a client I gather images and store them in one place so that they can be easily downloaded.
      - AC 1 - Images can be uploaded and downloaded from Kaggle.

  - As the developer I can use all provided images without concern so that the ML tool can use it for training.
      - AC 1 - All images in dataset are functioning.
      - AC 2 - All images in dataset are the correct/same size.
      - AC 3 - ML tool responds to all images correctly.

**2. Data visualization, cleaning, and preparation.**
  - As a client I can visually differentiate between healthy and infected leaves so that I understand the difference.
      - AC 1 - Clear visual guidance is provided whether a leaf is healty of infected.
      - AC 2 - There is a montage available to see the differences between healthy and infected leaves.
  
  - As a developer I have a clear dataset of images so that I can train the ML tool.
      - AC 1 - Image dataset is large enough to split into train, test, validation.
      - AC 2 - I can determine the image average and variability for each class (healthy and infected).

**3. Model training, optimization and validation.**
  - As a developer I can use the provided dataset to train the CNN model.
      - AC 1 - The data set has clear labels for its classes.
      - AC 2 - the image shape for that images is correctly determined.
      - AC 3 - Image dataset is large enough to split into train, test, validation.
      - AC 4 - Image augmentation is possible to increase training data for the CNN model.
    
  - As a developer I have the space/time to trial different settings so that the highest success can be obtained.
      - AC 1 - Time is made available to train the model.
      - AC 2 - Different "loss functions", Optimizers and "activation functions" can be tested.

**4. Dashboard planning, designing, and development.**
  - As a client I can define what I find relevant information so that the dashboard fits my needs.
      - AC 1 - Dashboard contains study information on the visual cues between healthy infected leaves.
      - AC 2 - It is possible for the clients IT team to understand how the model worked.
      - AC 3 - Client has been able to provide their priorities for the dashboard.
      - AC 4 - Client is able to upload images of leaves that they want to have tested and receive immediate feedback.
      - AC 5 - It is clear for the client what can be found on the dashboard.
      - AC 6 - When predictions on leaf healthy are made, the client can see that the degree of accuracy is >97%.
     
  - As a developer I can provide context on what is possible in the dashboard so that I can match the clients expectations.
      - AC 1 - Developer has been part of the dashboard conversations.
      - AC 2 - Developer has been made aware of clients needs/priorities.

**5. Dashboard deployment and release.**
   - As a client I have easy access to the dashboard so that it can be used without challenge.
     - AC 1 - An easy to use platform has been chosen to host the platform.
     - AC 2 - Platform is avaiable in the browser for easy/quick access. 
   
   - As a developer I can update the dashboard after deployment so that I can ensure it remains up to date.
     - AC 1 - chosen platform should be available also after deployment.
     - AC 2 - changes can me made/prepared without it directly impacting deployment, only when chosen to do so.

[Back to top ⇧](#table-of-contents)

## ML Business case

**Objective:** The issues at hand is a binary one. Provide clarity on if an image of a cherry leaves, contains a leaf that is healty, or if it contains the mildew fungus. A ML model needs to be trained that can inspect such images quickly and provide an answer immediately. 

**Desired Outcome:** A model that based on a provided imagesof a cherry leaf, is able to detect/predict whether the leaf is healthy or contains the mildew fungus. The model should be quick and easy to use. It should also provide realiable outcomes.

**Success Metrics:**

- *Accuracy:* The created model is required to have a degree of accuracy of at least >97%
- *User Experience:* The created dashboard should be easy to use and provide the ability to quickly and effectively review batches of leaf images. To make it applicable in the day to day, the provided feedback should be instantaneous. 

**Model Output:** The output of the model is binary. Stating that the provided image contains a leaf that is healthy, or a leaf that conatins the powdery mildew fungus. The model should also indicate how certain it is of this outcome, which it should be able to give with a degree of at least 97% certainty. The output should also easily be accesseable by the client through an online dashboard. In this same dashboard the client should be able to input new images for the model to review and download a report based on these images, stating all the images and the result according to the model.

**Heuristics:** The current process for determining the health of a cherry tree is done by inspecting its leaves. This takes a specialist around 30 minutes per tree. This is a timely and therefore costly process that can only be done by trained individuals. Having the ability to do this process through the ML model, based on pictures taken from the leaves. Will safe time, finances and allows for more employess to do the job, as it requires less skill. Allowing for the job to be done more frequently while it will be less dependant on human error and or the speciality of a few indivduals.

**Training Data:** The training data has been provided through [Kaggle](https://www.kaggle.com/datasets/codeinstitute/cherry-leaves/) and is deemed sufficient. Containing 4208 images of leaves, of which both classes (healthy and powdery mildew infected) have 2104 designated images which can be used to train the model. Images are colored (RGB) and of good quality. Also all images are of the same size (256, 256, 3).

**Business Benefits:**

- *Efficiency:* The trained model will be able to review many images/leaves at the same time, documenting results and allows for tracking of tree health. It does no longer require specialists to do the quality task. And answers can be provided instantly.
- *Reliability:* Now that the model has been trained, the reliability of the model is 99%. Which gives the client almost a certain answer to the question whether a leaf is healthy or not. Especially if multiple leaves of a single tree are reviewed, it will be very clear if a tree is healthy or not. Additionally the client is no longer dependant of an employees ability/speciality of being able to determine if a leaf/tree is healthy, taking human error out of the equation almost completely.
- *Scalability:* When an effective and reliable way can be set up to collect, document, upload and track the images/results of leaves and its related trees, this new way of working would be very scalable. The 'bottle neck' would be adapting the current way of working, to the collecting and processing of the images and finding a way of using this information in a practical manner. Allowing for the client to separate healthy from unhealthy trees and provide treatment where needed/possible. 

## Dashboard design

The dashboard was created using the Streamlit framework. The dashboard contains 5 pages which provides the client access to all relevant data. The dashboard answers the question for all business requirements, all in one place.

<details>
    <summary><strong>Dashboard Expectations</strong></summary>
    <table>
        <thead>
            <tr>
                <th></th>
                <th>Expectation</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>1.</td>
                <td>
                A project summary page, showing the project dataset summary and the client's requirements.
                </td>
            </tr>
            <tr>
                <td>2.</td>
                <td>
                A page listing your findings related to a study to visually differentiate a cherry leaf that is healthy from one that contains powdery mildew.
                </td>
            </tr>
            <tr>
                <td>3.</td>
                <td>A page containing:<br>
                -  A link to download a set of cherry leaf images for live prediction (you may use the Kaggle repository that was provided to you).<br>
                - A User Interface with a file uploader widget. The user should have the capacity to upload multiple images. For each image, it will display the image and a prediction statement, indicating if a cherry leaf is healthy or contains powdery mildew and the probability associated with this statement.<br>
                - A table with the image name and prediction results, and a download button to download the table.
                </td>
            </tr>
            <tr>
                <td>4. </td>
                <td>A page indicating your project hypothesis and how you validated it across the project.</td>
                <td>
            </tr>
            <tr>
                <td>5.</td>
                <td>A technical page displaying your model performance.</td>
                <td>
            </tr>
        </tbody>
    </table>
</details>

**Page 1. - Project summary**
The Project summary page provides general information about the mildew fungus and how it can be recognized on leaves when compared with healthy leaves. It gives information on the data that was used for the machine learning tool and states the two business requirements that this dashboard provides answers to. This page provides in writing part of the answer to Business Requirement 1: How to visually see the differences between a healthy leaf and a leaf with powdery mildew.

**Page 2. - Leaves visualizer**
The Leaves page provides a visual image montage, answering Business Requirement 1: How to visually see the differences between a healthy leaf and a leaf with powdery mildew. After the page intro this is split into three sections that can be activated by clicking the checkboxes:

*1. Difference between average and variability image*
The client can see the average and variability for the images of healthy and infected leaves.

*2. Differences between an average leaf that is healthy from one that contains powdery mildew*
Compare the differences between an average leaf that is healthy from one that contains powdery mildew

*3. Image Montage*
Provides the user with the ability to see a montage of 24 images of either healthy images, or images containing powdery mildew.

**Page 3. - Mildew detector**
Predictor tool with capabilities of predicing for a single image, or mutiple whether the leaves on the images are healthy or infected. It also provides a link to the original Kaggle set to showcase, so that images from the original set can also be tested.

When images are uploaded, the result provided is a quick visual of the uploaded image and a confirmation on if it's indeed a healthy leaf or if it is a leaf containing powdery mildew. It will also provide the probability of this prediciton in graph format.

**Page 4. - Project hypothesis and validation**
This page contains information on the initial hypothesis, the way this hypothesis would be validated and the result of this validation.

**Page 5. - Technical page showing model performance**
- Train, Validation and Test Set: Labels Frequencies
- Model history
- Performance on test set
- Confusion matrix

[Back to top ⇧](#table-of-contents)

## (Un)fixed Bugs

* When building the dashboard page for the "Mildew detector", it worked when uploading a single image. However, when uploading multiple images, a StreamlitDuplicateElementId error occured. Essentially stating that the graphs that I was trying to add needed to have a unique ID. I added a unique ID to the "plotly graphs" which creating the graphs, but I forgot to add the ID creation as well to the for loop of the graph generator, on the Mildew detector app page.
* After collecting the data and visualizing the data, I ran into a 'bug' that I could not seem to fix in the beginning. When I ran the model, the epochs would end after 4 or 5 runs. After trying to update the criteria I also received the error that the tensorflow packages might have been incorrectly installed.
* The original CNN model was overfitted, so I halved the filters in the second layer of the model from 64 to 32. This helped the model become more accurate. However loss and val_accuracy were still nog fully in line, although the estimated accuracy of the model to determine the right class was 99.99998%. So I was unclear on if I should reset the model again to get a better aligned performance between loss and val_accuracy, as it still seemed over fitted. In which case I should try out different combinations with the hyperparameters.
  * metrics tried: Adam / Adagrad / RMSprop
  * Loss tried : binary_crossentropy / categorical_crossentropy
  * v1 - binary_crossentropy + Adam : 99%+ acc. 11 epochs
  * v3 - binary_crossentropy + Adagrad :90%+ acc. 29 epochs
  * v4 - categorical_crossentropy + Adam: 4 epochs
* Somewhere in the modelling the definition of 0 = healthy and 1 = powdery_mildew got reversed.

[Back to top ⇧](#table-of-contents)

## Deployment

### Render

- The App live link is: `https://cherry-leaves-mildew-detection.onrender.com/`
- The project was deployed to Render using the following [Guide](https://code-institute-students.github.io/deployment-docs/42-pp5-pa/) .

1. If using the CI P5 project (if not, skip this step), prepare your codespace by:
   - Delete Procfile
   - Delete runtime.txt
   - Add, commit, and push your changes to GitHub
2. Log in to Render and click the "+ Add New" button
3. Click "Web Services" in the following drop down
4. Search for relevant repo from Github and click “Connect”
5. Give a name to your project
6. Ensure the settings of the project as as follows:
   - Setting Name: Value
   - Root Directory: blank
   - Environment: Python 3
   - Region: Frankfurt (EU Central), For those outside of Europe, a more localized region may be preferred
   - Branch: main
7. Set the Build Command to: " pip install -r requirements.txt "
8. Set the Start Command to: " streamlit run app.py "
9. Select desired payment plan (if needed, depending on size)
10. Scroll down and click “Advanced”
11. Click “Add Environment Variable”
12. Add a key: PORT and a value: 8501
13. Add a second environment variable with a key: PYTHON_VERSION and value: 3.12.1
14. Click “Create Web Service”
15. Wait for deployment… (Watch the console for some activity, deployment can take up to 15 minutes to complete)
16. Deployment completed!
17. Open the deployed site via the link below the WEB SERVICE name
18. Run your program to check that it all works as expected. Render can be slow for Predictive Analytics projects, so be patient

### 
- Below are the steps to fork the repository:
  - Locate the GitHub Repository of this project and log into your GitHub account.
  - Click on the "Fork" button, on the top right of the page, just above the "Settings".
  - Then locate 'Create Fork' below the page and click on it.
  - You now have a copy of the original repository in your GitHub account.

### Making a local clone
- Below are the steps to clone a repository:
  - On the page for the repository, click the 'Code' button
  - To clone the repository using HTTPS, copy the HTTPS URL provided there
  - Open your CLI application of choice and change the current working directory to the location where you want the cloned directory to be made.
  - Type git clone, and then paste the previously copied URL to create the clone

[Back to top ⇧](#table-of-contents)

## Technologies used

| Technology | Use
| --- | ---
| [Github](https://github.com/j) | To store the project code after being pushed from Codespaces
| [Jupyter Notebook](https://jupyter.org/) | Dataset and model management
| [Render](https://render.com/) | Tool hosting
| [Kaggle](https://www.kaggle.com/) | Image hosting
| [ChatGPT](https://openai.com/index/chatgpt/) | Support


[Back to top ⇧](#table-of-contents)

### Main Data Analysis and Machine Learning Libraries

| Libraries | Use
| --- | ---
| numpy==1.26.1 | to work with data in arrays
| pandas==2.1.1 | for data manipulation and analysis
| matplotlib==3.8.0 | for data visualisation
| seaborn==0.13.2 | for data visualisation
| streamlit==1.40.2 | for the app interface deployed on Heroku
| scikit-learn==1.3.1 | for predictive analysis
| tensorflow-cpu==2.16.1 | for model training
| keras>=3.0.0 | for setting model's hyperparameters
| plotly==5.17.0 | plotting the model's learning curve and diagnostic graphs
| tensorflow-cpu==2.16.1 | for model training
| kaggle==1.5.12 | Image importation


[Back to top ⇧](#table-of-contents)

## Testing

### Manual testing

**1. Information gathering and data collection.**
  - As a client I gather images and store them in one place so that they can be easily downloaded.
      - AC 1 - Images can be uploaded and downloaded from Kaggle.

  - As the developer I can use all provided images without concern so that the ML tool can use it for training.
      - AC 1 - All images in dataset are functioning.
      - AC 2 - All images in dataset are the correct/same size.
      - AC 3 - ML tool responds to all images correctly.

**2. Data visualization, cleaning, and preparation.**
  - As a client I can visually differentiate between healthy and infected leaves so that I understand the difference.
      - AC 1 - Clear visual guidance is provided whether a leaf is healty of infected.
      - AC 2 - There is a montage available to see the differences between healthy and infected leaves.
  
  - As a developer I have a clear dataset of images so that I can train the ML tool.
      - AC 1 - Image dataset is large enough to split into train, test, validation.
      - AC 2 - I can determine the image average and variability for each class (healthy and infected).

**3. Model training, optimization and validation.**
  - As a developer I can use the provided dataset to train the CNN model.
      - AC 1 - The data set has clear labels for its classes.
      - AC 2 - the image shape for that images is correctly determined.
      - AC 3 - Image dataset is large enough to split into train, test, validation.
      - AC 4 - Image augmentation is possible to increase training data for the CNN model.
    
  - As a developer I have the space/time to trial different settings so that the highest success can be obtained.
      - AC 1 - Time is made available to train the model.
      - AC 2 - Different "loss functions", Optimizers and "activation functions" can be tested.

**4. Dashboard planning, designing, and development.**
  - As a client I can define what I find relevant information so that the dashboard fits my needs.
      - AC 1 - Dashboard contains study information on the visual cues between healthy infected leaves.
      - AC 2 - It is possible for the clients IT team to understand how the model worked.
      - AC 3 - Client has been able to provide their priorities for the dashboard.
      - AC 4 - Client is able to upload images of leaves that they want to have tested and receive immediate feedback.
      - AC 5 - It is clear for the client what can be found on the dashboard.
      - AC 6 - When predictions on leaf healthy are made, the client can see that the degree of accuracy is >97%.
     
  - As a developer I can provide context on what is possible in the dashboard so that I can match the clients expectations.
      - AC 1 - Developer has been part of the dashboard conversations.
      - AC 2 - Developer has been made aware of clients needs/priorities.

**5. Dashboard deployment and release.**
   - As a client I have easy access to the dashboard so that it can be used without challenge.
     - AC 1 - An easy to use platform has been chosen to host the platform.
     - AC 2 - Platform is avaiable in the browser for easy/quick access. 
   
   - As a developer I can update the dashboard after deployment so that I can ensure it remains up to date.
     - AC 1 - chosen platform should be available also after deployment.
     - AC 2 - changes can me made/prepared without it directly impacting deployment, only when chosen to do so.

[Back to top ⇧](#table-of-contents)

### PEP8 Python code validation


## Credits



### Content

- The text for the Home page was taken from Wikipedia Article A.
- Instructions on how to implement form validation on the Sign-Up page were taken from [Specific YouTube Tutorial](https://www.youtube.com/).
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/).

### Media

- The photos used on the home and sign-up page are from This Open-Source site.
- The images used for the gallery page were taken from this other open-source site.

[Back to top ⇧](#table-of-contents)

## Acknowledgements (optional)

- Mohammed Shami : mentor for this project
- Roman Rakic and the CI support team : providing answers when I was stuck and Google & ChatGPT were not able to provide an answer

[Back to top ⇧](#table-of-contents)



# NOTES AND OTHERS

### Business Case understanding and ML validation
<details>
    <summary><strong>Business case assessment</strong></summary>
    <table>
        <thead>
            <tr>
                <th>Ask</th>
                <th>Requirements</th>
                <th>Pass/Fail</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>1. What are the business requirements?</td>
                <td>
                - The client is interested in conducting a study to visually differentiate a cherry leaf that is healthy from one that contains powdery mildew.<br>
                - The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.
                </td>
                <td>
                <!-- &#10003; -->
                </td>
            </tr>
            <tr>
                <td>2. Is there any business requirement that can be answered with conventional data analysis?</td>
                <td>
                - Yes, we can use conventional data analysis to conduct a study to visually differentiate a cherry leaf that is healthy from one that contains powdery mildew.
                </td>
                <td>
                <!-- &#10003; -->
                </td>
            </tr>
            <tr>
                <td>3. Does the client need a dashboard or an API endpoint?</td>
                <td>- The client needs a dashboard.</td>
                <td>
                <!-- &#10003; -->
                </td>
            </tr>
            <tr>
                <td>4. What does the client consider as a successful project outcome?</td>
                <td>
                - A study showing how to visually differentiate a cherry leaf that is healthy from one that contains powdery mildew.<br>
                - Also, the capability to predict if a cherry leaf is healthy or contains powdery mildew.</td>
                <td>
                <!-- &#10003; -->
                </td>
            </tr>
            <tr>
                <td>5. Can you break down the project into Epics and User Stories?</td>
                <td>
                - Information gathering and data collection.<br>
                - Data visualization, cleaning, and preparation.<br>
                - Model training, optimization and validation.<br>
                - Dashboard planning, designing, and development.<br>
                - Dashboard deployment and release.
                </td>
                <td>
                <!-- &#10003; -->
                </td>
            </tr>
            <tr>
                <td>6. Ethical or Privacy concerns?</td>
                <td>
                - The client provided the data under an NDA (non-disclosure agreement), therefore the data should only be shared with professionals that are officially involved in the project.
                </td>
                <td>
                <!-- &#10003; -->
                </td>
            </tr>
            <tr>
                <td>7. Does the data suggest a particular model?</td>
                <td>
                - The data suggests a binary classifier, indicating whether a particular cherry leaf is healthy or contains powdery mildew.
                </td>
                <td>
                <!-- &#10003; -->
                </td>
            </tr>
            <tr>
                <td>8. What are the model's inputs and intended outputs?</td>
                <td>
                - The input is a cherry leaf image and the output is a prediction of whether the cherry leaf is healthy or contains powdery mildew.
                </td>
                <td>
                <!-- &#10003; -->
                </td>
            </tr>
            <tr>
                <td>9. What are the criteria for the performance goal of the predictions?</td>
                <td>- We agreed with the client a degree of 97% accuracy.</td>
                <td>
                <!-- &#10003; -->
                </td>
            </tr>
            <tr>
                <td>10. How will the client benefit?</td>
                <td>- The client will not supply the market with a product of compromised quality.</td>
                <td>
                <!-- &#10003; -->
                </td>
            </tr>
        </tbody>
    </table>
</details>

[Back to top ⇧](#table-of-contents)

## ML Business Case
**In the previous bullet, you potentially visualised an ML task to answer a business requirement. You should frame the business case using the method we covered in the course.**

<details>
    <summary><strong>Project Considerations</strong></summary>
    <table>
        <thead>
            <tr>
                <th>Business Requirements</th>
                <th>Requirements</th>
                <th>Pass/Fail</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>BR 1</td>
                <td>
                Your study should include at least analysis on:<br>
                - average images and variability images for each class (healthy or powdery mildew),<br>
                - the differences between average healthy and average powdery mildew cherry leaves,<br>
                - an image montage for each class.
                </td>
                <td>
                <!-- &#10003; -->
                </td>
            </tr>
            <tr>
                <td>BR 2</td>
                <td>
                - You may deliver an ML system that is capable of predicting whether a cherry leaf is healthy or contains powdery mildew. In this case, we suggest to use Neural Networks to map the relationships between the features and the labels.<br><br>
                - You will notice when exploring the dataset that the images are 256 pixels × 256 pixels. When defining your image shape to load the images to memory for training the model, you may choose 256 × 256 as your image shape. However, that will lead to a trained model that will likely be larger than 100Mb. This is fine as long as the model meets the project requirement, the caveat is that you may need to use Git LFS (Large File Storage) to push files larger than 100Mb to GitHub. As a result, we suggest you consider using an image shape that is smaller, like 100 × 100 or 50 × 50, with the expectation that the model would still meet the performance requirement and will be smaller than 100Mb for a smoother push to GitHub.
                </td>
                <td>
                <!-- &#10003; -->
                </td>
            </tr>
        </tbody>
    </table>
</details>

[Back to top ⇧](#table-of-contents)

## The rationale to map the business requirements to the Data Visualisations and ML tasks
**List your business requirements and a rationale to map them to the Data Visualisations and ML tasks.**

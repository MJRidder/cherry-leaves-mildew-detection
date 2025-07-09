![header_image](/images/readme/readme-cherry-leaves-banner.png)

# Mildew detection tool for cherry leaves

# Introduction

The cherry plantation crop from Farmy & Foods is facing a challenge where their cherry plantations have been presenting powdery mildew. Currently, the process is manual verification if a given cherry tree contains powdery mildew. An employee spends around 30 minutes in each tree, taking a few samples of tree leaves and verifying visually if the leaf tree is healthy or has powdery mildew. If there is powdery mildew, the employee applies a specific compound to kill the fungus. The time spent applying this compound is 1 minute. The company has thousands of cherry trees located on multiple farms across the country. As a result, this manual process is not scalable due to the time spent in the manual process inspection.

To save time in this process, the IT team suggested an ML system that detects instantly, using a leaf tree image, if it is healthy or has powdery mildew. A similar manual process is in place for other crops for detecting pests, and if this initiative is successful, there is a realistic chance to replicate this project for all other crops. The dataset is a collection of cherry leaf images provided by Farmy & Foods, taken from their crops.

**Deployed version can be found [here](https://cherry-leaves-mildew-detection.onrender.com/)**

# Table of Contents

- [Mildew detection tool for cherry leaves](#mildew-detection-tool-for-cherry-leaves)
- [Introduction](#introduction)
- [Table of Contents](#table-of-contents)
  - [Dataset Content](#dataset-content)
  - [Business Requirements](#business-requirements)
  - [Hypothesis and validation](#hypothesis-and-validation)
  - [Rationale for ML model](#rationale-for-ml-model)
  - [Implementation of the Business Requirements](#implementation-of-the-business-requirements)
  - [ML Business case](#ml-business-case)
  - [ML model development](#ml-model-development)
  - [Dashboard design](#dashboard-design)
  - [Unfixed Bugs](#unfixed-bugs)
  - [Deployment](#deployment)
  - [Technologies used](#technologies-used)
  - [Main Data Analysis and Machine Learning Libraries](#main-data-analysis-and-machine-learning-libraries)
  - [Testing](#testing)
    - [Manual testing](#manual-testing)
    - [PEP8 Python code validation](#pep8-python-code-validation)
  - [Credits](#credits)

## Dataset Content

- The dataset is sourced from [Kaggle](https://www.kaggle.com/datasets/codeinstitute/cherry-leaves/) and contains 4208 images of cherry leaves images. The images are split into two classes: healthy leaves and leaves that contain Mildew, a generally white powdery substance which can be found on the leaves. This type of fungal disease can affect many plant species, which makes this project valuable across the agricultural sector.

- Overall the images are of a good quality and have normal (RGB) colors. The dataset was collected to train a machine learning model which could be used to predict whether the leaf on the image is healthy or would contain the powdery mildew.

- The cherry plantation crop is one of the finest products in their portfolio, and the company is concerned about supplying the market with a compromised quality product.

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

- Healthy leaves are of a consistant and brighter green color, with strong lines (veines) and texture.
- Leaves with mildew do not have a consistant green color (irregular), have unclear lines and have visually white collored textures, covering the leaves. This is also more prudent in the veins of the leaves.

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

## ML model development

For this tool to work, a Convolutional Neural Network (CNN) model was created. A CNN is a type of deep learning model particularly well-suited for analyzing visual data like images and videos. It's a specialized type of artificial neural network that excels at identifying patterns and features within these visual inputs. CNNs are widely used for tasks such as image classification, object detection, and facial recognition.

**General chosen layout**
There are three convolutional layers, each followed by a max pooling layer. These are used for feature extraction from the input images. Each convolutional layer is followed by a max pooling layer with a pool size of 2x2, which reduces the spatial dimensions of the output. After the convolutional and pooling layers, the model flattens the output to convert it into a one-dimensional array. This is necessary for feeding into the dense layers for classification.

Dense Layers: The first dense layer has 64 neurons and uses 'relu' activation. It serves as a fully connected layer that processes features extracted by the convolutional layers. This is followed by a dropout layer with a dropout rate of 0.5 to reduce overfitting by randomly setting input units to 0 during training. The final dense layer has 1 neuron with a 'sigmoid' activation function. This is suitable for binary classification, producing a probability output indicating the likelihood of belonging to one of the two classes.

Compilation: The model uses the 'adam' optimizer, a popular choice for deep learning models due to its efficiency. The loss function is 'binary_crossentropy', which is standard for binary classification problems. The model seemed well-suited for tasks like image-based binary classification, which could include applications such as distinguishing between two different types of objects or conditions in images.

**Other chosen compilations**
As results varied and with several tests orignally, the model fitting stopped after 4 epochs, other optimizers functions have been trialed to see which would give the best result:

- other optimizers tried: Adagrad / RMSprop
- other loss function tried: categorical_crossentropy
- other activation function tried: Softmax

None of the other compilations would have a desired effect:

v1 - relu / sigmoid / binary_crossentropy / Adam : 99%+ acc. | 11 epochs (Chosen result)
v2 - relu / sigmoid / binary_crossentropy / Adagrad :90%+ acc. | 29 epochs (did not match the desired >97% accuracy and was overfitted)
v2 - relu / sigmoid / binary_crossentropy / RMSprop :<90% acc. | 3 epochs (insufficient accuracy)
v4 - relu / sigmoid / categorical_crossentropy / Adam: 20+% acc. | 4 epochs (insufficient accuracy)
v5 - relu / softmax / binary_crossentropy / Adam: -10% acc. | 30 epochs (maxed out)

After trialling different variations, I resorted back to the original fitting (v1). The filters of the second convolution layer were lowered from 64 (original amount) to 32 which then gave better results.

## Dashboard design

The dashboard was created using the Streamlit framework. The dashboard contains 5 pages which provides the client access to all relevant data. The dashboard answers the question for all business requirements, all in one place.

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
This page is designed for the clients IT team to review the models performance.

- Train, Validation and Test Set: Labels Frequencies
- Model history
- Performance on test set
- Confusion matrix

[Back to top ⇧](#table-of-contents)

## Unfixed Bugs

When operated in the intended manner, No remaining bugs exist in the code or on the dashboard. However, the tool is solely created with the purpose and design of evaluating clear images of leaves. When images are uploaded that are unclear, the tool does not yet have the capability to indicate that it needs a clearer image. It will simply indicate healty or infected (containing powdery_mildew). Furthermore, if images are used that are not leaves, the tool will also simply give them a class.

This would still need to be reviewed and fixed before it can be made fully available and operational for the client. As at the moment there is still room for human error in this area.

## Deployment

**Deploy on Render**

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

**Forking the Repository**

- Below are the steps to fork the repository:
  - Locate the GitHub Repository of this project and log into your GitHub account.
  - Click on the "Fork" button, on the top right of the page, just above the "Settings".
  - Then locate 'Create Fork' below the page and click on it.
  - You now have a copy of the original repository in your GitHub account.

**Making a local clone**

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

## Main Data Analysis and Machine Learning Libraries

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

| Feature | Action | Expected Result | Pass/Fail
| --- | --- | --- | ---
| Client images upload | Easy uploading of images | Images are uploaded on Kaggle | Pass
| Developer image download | Downloading images from Kaggle without issue< | All images on Kaggle are useable and correct | Pass

**2. Data visualization, cleaning, and preparation.**

| Feature | Action | Expected Result | Pass/Fail
| --- | --- | --- | ---
| Client can see healthy/infected | Visually or by reading the study indicates the differences between healthy and infected leaves | It is clear how to differentiate between healthy and infected leaves | Pass
| Client can see healthy/infected | On request the client can see the difference between healthy and infected leaves | There is a montage available to view | Pass
| Developer has a clean dataset | Accurate dataset is present to work with | A clean dataset of images is available | Pass
| Developer has a clean dataset | Define average & variability of images | It is possible to calculate average & variability with available dataset | Pass

**3. Model training, optimization and validation.**

| Feature | Action | Expected Result | Pass/Fail
| --- | --- | --- | ---
| Model training | Available dataset can be used directly | Available dataset is accurate & correct | Pass
| Model training | Calculate image shape | Avg image shape is available | Pass
| Model training | Dataset is large enough | Image dataset is large enough to split into train, test, validation | Pass
| Model training | define binary classes (Healthy & Infected) | The data set has clear labels for its classes | Pass
| Model training | Image augmentation | Image augmentation is possible to increase training data for the CNN model | Pass
| Model training | Trial & Error of different model settings | Time is made available to test for best result | Pass

**4. Dashboard planning, designing, and development.**

| Feature | Action | Expected Result | Pass/Fail
| --- | --- | --- | ---
| Client dashboard preference | View study findings | Dashboard contains study information on the visual cues between healthy infected leaves | Pass
| Client dashboard preference | It is possible for the clients IT team to understand how the model worked | Model explanation and metrics can be found on the dashboard | Pass
| Client dashboard preference | Client has been able to provide their priorities for the dashboard | Client preferences have been documented and shared | Pass
| Client dashboard preference | Check health of leaves in realtime | ability to upload images of leaves that they want to have tested and receive immediate feedback | Pass
| Client dashboard preference | Check health of leaves in realtime | leaf health predictions are made with a degree of accuracy of >97% | Pass

**5. Dashboard deployment and release.**

| Feature | Action | Expected Result | Pass/Fail
| --- | --- | --- | ---
| Client dashboard access | Access dashboard at any time | Dashboard is available online | Pass
| Developer updates | Developer can update dashboard | Developer can make updates after the dashboard launch and upload changes in collaboration with the client | Pass

**Dashboard functionality.**

| Dashboard | Feature | Expected Result | Pass/Fail
| --- | --- | --- | ---
| Project Summary | Project summary  | Provides information about the project and the subject matter | Pass
| Project Summary | Business requirements | Makes clear what the dashboard is intended to answer | Pass
| Leaves Visualizer | Page usage | It is clear what the page is inteded for | Pass
| Leaves Visualizer | avg & variability | Allows the user to view the image average and variability of the Healty and Infected classes | Pass
| Leaves Visualizer | avg & variability comparison | Allows user to compare visual average differences between healthy and infected class | Pass
| Leaves Visualizer | image montage | Allows user to create a visual image montage for each Healthy and infected class  | Pass
| Mildew Detection | Page usage | It is clear what the page is inteded for | Pass
| Mildew Detection | See original dataset | Original dataset is made clear and accesseable | Pass
| Mildew Detection | Image upload for Mildew detection | The function to upload images works well and allows for multiple images to upload at the same time | Pass
| Mildew Detection | View health check | With a general >97% accuracy the answer is given if the leaf in the image is healthy or contains powdery mildew | Pass
| Mildew Detection | Healthy diagnoses graph | Graph shows accuracy of diagnoses visually and in numbers  | Pass
| Mildew Detection | Report download | Results of health check can be downloaded as .csv files | Pass
| Project Hypothesis | Hypotheses | All three hypothesis are explained | Pass
| Project Hypothesis | Hypotheses | It is explained how the hypothesis were validated | Pass
| Project Hypothesis | Hypotheses | Validation results for all three hypothesis are mentioned | Pass
| ML Performance Metrics | Train, Validation and Test Sets | The split between train, validation and test sets are visible and explained | Pass
| ML Performance Metrics | Model History | Model history is visible and the different tools that have been tried are explained | Pass
| ML Performance Metrics | Tool accuracy | the Generalised Performance on Test Set shows the accuracy of the tool | Pass
| ML Performance Metrics | Confusion Matrix | the Confusion Matrix provides further test results on the accuracy | Pass

[Back to top ⇧](#table-of-contents)

### PEP8 Python code validation

Reviewed all .py pages for [PEP8](https://pep8ci.herokuapp.com/), all pages are now without errors. General updates that were made:

- Adding/Removal of white lines
- Updating indentations
- Removal of white spaces after code
- General formatting

[Back to top ⇧](#table-of-contents)

## Credits

- The template used for this project belongs to CodeInstitute (CI) - [GitHub](https://github.com/Code-Institute-Solutions/milestone-project-mildew-detection-in-cherry-leaves)
- The CI Malaria Walkthrough project, for providing the step by step template for data collection, visualization and modeling. For also providing a clear overview of the type of files/folders required.
- The following Github users and relevant projects, creating similar deeplearning projects with which I could compare notes with on structure, input, phrasing and document layout.
  - HughKeenan : [Cherry-Picker](https://github.com/HughKeenan/CherryPicker)
  - jfpaliga : [CVD-predictor](https://github.com/jfpaliga/CVD-predictor)
  - ocassidydev : [mushroom-safety](https://github.com/ocassidydev/mushroom-safety)
  - Edgarkimbugwe : [CLPM-Detector](https://github.com/Edgarkimbugwe/CLMP-Detector)
  - tomdu3 : [brain-tumor-detector](https://github.com/tomdu3/brain-tumor-detector)

[Back to top ⇧](#table-of-contents)

**Content**

- The Leaves dataset was hosted and downloaded by Kaggle.
- The Business case itself was creaed by Code Institute.

[Back to top ⇧](#table-of-contents)

**Media**

- The banner image was downloaded from the University of California Agriculture and Natural Resources website

[Back to top ⇧](#table-of-contents)

**Acknowledgements**

- Mohammed Shami : mentor for this project, for providing guidance and helping me create the confidence to complete this project in the required time.
- Roman Rakic and the CI support team : providing answers when I was stuck and Google & ChatGPT were not able to provide an answer.

[Back to top ⇧](#table-of-contents)

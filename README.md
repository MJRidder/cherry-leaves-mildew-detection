![Banner](/images/readme/readme-cherry-leaves-banner.png)

# Mildew detection tool for cherry leaves

# Introduction

### Deployed version at https://cherry-leaves-mildew-detection.onrender.com/


# Table of Contents
  - [Dataset Content](#dataset-content)
Business Requirements
Hypothesis and validation
Rationale for the model
Implementation of the Business Requirements
ML Business case
Dashboard design
Unfixed Bugs
Deployment
Technologies used
Testing
Credits

## Dataset Content

- The dataset is sourced from [Kaggle](https://www.kaggle.com/datasets/codeinstitute/cherry-leaves/) and contains 4208 images of cherry leaves images. The images are split into two classes: healthy leaves and leaves that contain Mildew, a generally white powdery substance which can be found on the leaves. This type of fungal disease can affect many plant species, which makes this project valuable across the agricultural sector.

Overall the images are of a good quality and have normal (RGB) colors. The dataset was collected to train a machine learning model which could be used to predict whether the leaf on the image is healthy or would contain the powdery mildew.

The cherry plantation crop is one of the finest products in their portfolio, and the company is concerned about supplying the market with a compromised quality product.


- The dataset contains +4 thousand images taken from the client's crop fields. The images show healthy cherry leaves and cherry leaves that have powdery mildew, a fungal disease that affects many plant species. 
## Business Requirements

The cherry plantation crop from Farmy & Foods is facing a challenge where their cherry plantations have been presenting powdery mildew. Currently, the process is manual verification if a given cherry tree contains powdery mildew. An employee spends around 30 minutes in each tree, taking a few samples of tree leaves and verifying visually if the leaf tree is healthy or has powdery mildew. If there is powdery mildew, the employee applies a specific compound to kill the fungus. The time spent applying this compound is 1 minute. The company has thousands of cherry trees located on multiple farms across the country. As a result, this manual process is not scalable due to the time spent in the manual process inspection.

To save time in this process, the IT team suggested an ML system that detects instantly, using a leaf tree image, if it is healthy or has powdery mildew. A similar manual process is in place for other crops for detecting pests, and if this initiative is successful, there is a realistic chance to replicate this project for all other crops. The dataset is a collection of cherry leaf images provided by Farmy & Foods, taken from their crops.

- 1 - The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew.
- 2 - The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.

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

## ML Business Case
**In the previous bullet, you potentially visualised an ML task to answer a business requirement. You should frame the business case using the method we covered in the course.**

## Hypothesis and how to validate?

**Hypothesis 1:**
It is visibly possible to differintiate a healthy leave, from a leave containing powdery mildew.

Valitation:
review images and determine whether there are specific indicators that can be viewed, determining if a leave is healthy or containing powdery mildew.

**Hypothesis 2**
Based on visible indicators, it can be predicted with a 97% accuracy if a leave is healthy, or containing powdery mildew.

Valitation:
A CNN model will be trained, tested and used on a validation set of images to determine if this is possible.

**Hypothesis 3**
By using a trained CNN model, time spend & costs for cherry leaves health checks can be drastically reduced.

Validation:
Taking in account the time/cost needed to make pictures, upload them and have the CNN model run over them, a comparison can be made between these actions and the 30 minutes per tree that it costs today to verify if a Cherry tree is healthy, or infected with Mildew.

## The rationale to map the business requirements to the Data Visualisations and ML tasks
**List your business requirements and a rationale to map them to the Data Visualisations and ML tasks.**

## Dashboard Design

**List all dashboard pages and their content, either blocks of information or widgets, like buttons, checkboxes, images, or any other items, that your dashboard library supports.**
**Finally, during the project development, you may revisit your dashboard plan to update a given feature (for example, at the beginning of the project, you were confident you would use a given plot to display an insight, but later, you chose another plot type).**

Page 1: Project Summary
Quick project summary
**General Information**
ABC

**Project Dataset**
The available dataset contains ...

Link to additional information (Readme file)
Business requirements
- ABC
- DEF

Page 2: Cells Visualizer
It will answer business requirements 1
Checkbox 1 - Difference between average and variability image <br>
Checkbox 2 - Differences between average parasitised and average uninfected cells <br>
Checkbox 3 - Image Montage <br>

Page 3: Malaria Detection
Business requirement two information - "The client is interested in telling whether a given cell contains malaria parasite or not."
Link to download a set of parasite-contained and uninfected cell images for live prediction.
Create a user interface with a file uploader widget. The user should upload multiple malaria cell images. It will display the image and a prediction statement, indicating if the cell is infected or not with malaria and the probability associated with this statement.
Table with the image name and prediction results.
Download button to download table.

Page 4: Project Hypothesis and Validation
Block for each project hypothesis, describe the conclusion and how you validated it.
Page 5: ML Prediction Metrics
Label Frequencies for Train, Validation, and Test Sets
Model History - Accuracy and Losses
Model evaluation result

## Unfixed Bugs

- You will need to mention unfixed bugs and why they were unfixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a significant variable for consideration, paucity of time and difficulty understanding implementation is not a valid reason to leave bugs unfixed.

## Deployment

### Heroku

- The App live link is: `https://YOUR_APP_NAME.herokuapp.com/`
- Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
- The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click the button Open App on the top of the page to access your App.
6. If the slug size is too large, then add large files not required for the app to the .slugignore file.

## Main Data Analysis and Machine Learning Libraries

- Here, you should list the libraries used in the project and provide an example(s) of how you used these libraries.

## Credits

- In this section, you need to reference where you got your content, media and from where you got extra help. It is common practice to use code from other repositories and tutorials. However, it is necessary to be very specific about these sources to avoid plagiarism.
- You can break the credits section up into Content and Media, depending on what you have included in your project.

### Content

- The text for the Home page was taken from Wikipedia Article A.
- Instructions on how to implement form validation on the Sign-Up page were taken from [Specific YouTube Tutorial](https://www.youtube.com/).
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/).

### Media

- The photos used on the home and sign-up page are from This Open-Source site.
- The images used for the gallery page were taken from this other open-source site.

## Acknowledgements (optional)

- Thank the people who provided support throughout this project.


# NOTES



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

<details>
    <summary><strong>Dashboard Expectations</strong></summary>
    <table>
        <thead>
            <tr>
                <th></th>
                <th>Expectation</th>
                <th>Pass/Fail</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>1.</td>
                <td>
                A project summary page, showing the project dataset summary and the client's requirements.
                </td>
                <td>
                <!-- &#10003; -->
                </td>
            </tr>
            <tr>
                <td>2.</td>
                <td>
                A page listing your findings related to a study to visually differentiate a cherry leaf that is healthy from one that contains powdery mildew.
                </td>
                <td>
                <!-- &#10003; -->
                </td>
            </tr>
            <tr>
                <td>3.</td>
                <td>A page containing:<br>
                -  A link to download a set of cherry leaf images for live prediction (you may use the Kaggle repository that was provided to you).<br>
                - A User Interface with a file uploader widget. The user should have the capacity to upload multiple images. For each image, it will display the image and a prediction statement, indicating if a cherry leaf is healthy or contains powdery mildew and the probability associated with this statement.<br>
                - A table with the image name and prediction results, and a download button to download the table.
                </td>
                <td>
                <!-- &#10003; -->
                </td>
            </tr>
            <tr>
                <td>4. </td>
                <td>A page indicating your project hypothesis and how you validated it across the project.</td>
                <td>
                <!-- &#10003; -->
                </td>
            </tr>
            <tr>
                <td>5.</td>
                <td>A technical page displaying your model performance.</td>
                <td>
                <!-- &#10003; -->
                </td>
            </tr>
        </tbody>
    </table>
</details>

# Bugs / Fixes
* After collecting the data and visualizing the data, I ran into a 'bug' that I could not seem to fix in the beginning. When I ran the model, the epochs would end after 4 or 5 runs. After trying to update the criteria I also received the error that the tensorflow packages might have been incorrectly installed.
* The original CNN model was overfitted, so I halved the filters in the second layer of the model from 64 to 32. This helped the model become more accurate. However loss and val_accuracy were still nog fully in line, although the estimated accuracy of the model to determine the right class was 99.99998%. So I was unclear on if I should reset the model again to get a better aligned performance between loss and val_accuracy, as it still seemed over fitted. In which case I should try out different combinations with the hyperparameters.
  * metrics tried: Adam / Adagrad / RMSprop
  * Loss tried : binary_crossentropy / categorical_crossentropy
  * v1 - binary_crossentropy + Adam : 99%+ acc. 11 epochs
  * v3 - binary_crossentropy + Adagrad :90%+ acc. 29 epochs
  * v4 - categorical_crossentropy + Adam: 4 epochs
* Somewhere in the modelling the definition of 0 = healthy and 1 = powdery_mildew got reversed.

# Dashboard planning

Page 1. - Project summary <br>
Page 2. - Study findings determining healthy leaves and leaves with powdery_mildew <br>
Page 3. - Predictor tool with capabilities of using existing images or images uploaded by user <br>
Page 4. - Project hypothesis and validation <br>
Page 5. - Technical page showing model performance <br>
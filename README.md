# Overview
When we walk or drive on the roads, we see some deformities like broken trees, potholes, or others that need to be fixed or repaired.

Here our project will detect automatically all of these deformities and alert the destination with info like the name of the class and the image.

The current classes are: **Potholes**, **Broken Trees**, **Accidents** and **Fires**.


# Setup the configuration of your local environment (You should use *CMD*)

### Setup a virtual environment in the CMD:
- Create a virtual environment with the required python version: $`conda create -n visual-deformity python==3.11.5 -y`
- Activate the created environment: $`conda activate visual-deformity`
- Install the required packages: $`pip install -r requirements.txt`
- Initialize the DVC: $`dvc init`

# Pipeline Stages
1) Data Preparation
2) Train the model on the prepared data
3) Evaluate the trained model

<br>**Note:** This pipeline is fully automated and other stages will be added later.

# Run the pipeline (You should use *CMD*)
- See the DAG (Directed Cyclic Graph): $`dvc dag`
- Run the pipeline with this command: $`dvc repro`
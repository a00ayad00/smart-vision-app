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
1) Download the datasets from Roboflow
2) Train the model on the datasets
3) Evaluate the trained model

<br>**Notes:**
- This pipeline is fully automated and other stages will be added later.
- If you encountered this error **_ImportError: libGL.so.1: cannot open shared object file: No such file or directory_** on linux, run $`apt-get update && apt-get install -y libgl1 libglib2.0-0`. If you encountered a **_permission deny_** message, run $`sudo su` first, then exit from the admin terminal using $`exit`

# Run the pipeline (You should use *CMD*)
- See the DAG (Directed Cyclic Graph): $`dvc dag`
- Run the pipeline with this command: $`dvc repro`

# Run the app
### From local
- First, you have to run the API from _main.py_ file: $`python main.py`
- Run the streamlit app: $`streamlit run app.py`
### From Docker



docker build -t backend -f back .
docker run -p 5000:5000 backend

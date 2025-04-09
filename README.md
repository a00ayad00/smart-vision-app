# Overview
When we walk or drive on the roads, we see some deformities like broken trees, potholes, or others that need to be fixed or repaired.

Here our project will detect automatically all of these deformities and alert the destination with info like the name of the class and the image.

The current classes are: **Potholes**, **Broken Trees**, **Accidents** and **Fires**.

# Setup the configuration of your local environment (You should use *CMD*)

### Setup a virtual environment:
- Create a virtual environment with the required python version: $`conda create -n visual-deformity python==3.11.5 -y`
- Activate the created environment: $`conda activate visual-deformity`
- Install the required packages: $`pip install -r requirements.txt`

# Run the app
### From local
- First, you have to run the API from _main.py_ file: $`python main.py`
- Run the streamlit app: $`streamlit run app.py`

# Run the app
### From local
- First, you have to run the API from _main.py_ file: $`python main.py`
- Run the streamlit app: $`streamlit run app.py`
### From Docker
- Pull the image from the hup: $`docker pull ayad33/smart-vision-api:1`
- Run the pulled image: $`docker run -p 5000:5000 ayad33/smart-vision-api:1`
- Reach the API through http://localhost:5000


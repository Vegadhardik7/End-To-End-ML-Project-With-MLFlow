# End-To-End-ML-Project-With-MLFlow

## Workflows

1. Update config.yaml
2. Update schema.yaml
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline 
8. Update the main.py
9. Update the app.py

Image Reference In Sequence:

![Screenshot 2025-06-27 150602](https://github.com/user-attachments/assets/e51ec45f-6b26-4be5-83fa-5e91ffcf5a31)

# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/Vegadhardik7/End-To-End-ML-Project-With-MLFlow
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n mlproj python=3.11 -y
```

```bash
conda activate mlproj
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up you local host and port
```



## MLflow

[Documentation](https://mlflow.org/docs/latest/index.html)


##### cmd
- mlflow ui

### dagshub
[dagshub](https://dagshub.com/)

My DagsHub Link: https://dagshub.com/Vegadhardik7/End-To-End-ML-Project-With-MLFlow

```
MLFLOW_TRACKING_URI=https://dagshub.com/Vegadhardik7/End-To-End-ML-Project-With-MLFlow.mlflow \
MLFLOW_TRACKING_USERNAME=Vegadhardik7 \
MLFLOW_TRACKING_PASSWORD=0b097abf2f947a5cd50556274d27ae5b907535de \
python script.py
```

Run this to export as env variables:

For Linux:

```bash
export MLFLOW_ENABLE_LEGACY_LOGGING_API=true

export MLFLOW_TRACKING_URI=https://dagshub.com/Vegadhardik7/End-To-End-ML-Project-With-MLFlow.mlflow

export MLFLOW_TRACKING_USERNAME=Vegadhardik7 

export MLFLOW_TRACKING_PASSWORD=0b097abf2f947a5cd50556274d27ae5b907535de

```

For Windows:

```bash
set MLFLOW_ENABLE_LEGACY_LOGGING_API=true

set MLFLOW_TRACKING_URI=https://dagshub.com/Vegadhardik7/End-To-End-ML-Project-With-MLFlow.mlflow

set MLFLOW_TRACKING_USERNAME=Vegadhardik7 

set MLFLOW_TRACKING_PASSWORD=0b097abf2f947a5cd50556274d27ae5b907535de

```



# AWS-CICD-Deployment-with-Github-Actions

## 1. Login to AWS console.

## 2. Create IAM user for deployment

	#with specific access

	1. EC2 access : It is virtual machine

	2. ECR: Elastic Container registry to save your docker image in aws


	#Description: About the deployment

	1. Build docker image of the source code

	2. Push your docker image to ECR

	3. Launch Your EC2 

	4. Pull Your image from ECR in EC2

	5. Lauch your docker image in EC2

	#Policy:

	1. AmazonEC2ContainerRegistryFullAccess

	2. AmazonEC2FullAccess

	
## 3. Create ECR repo to store/save docker image
    - Save the URI: 737281587410.dkr.ecr.us-east-1.amazonaws.com/mlproject

	
## 4. Create EC2 machine (Ubuntu) 

## 5. Open EC2 and Install docker in EC2 Machine:
	
	
	#optinal

	sudo apt-get update -y

	sudo apt-get upgrade
	
	#required

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker
	
# 6. Configure EC2 as self-hosted runner:
    setting>actions>runner>new self hosted runner> choose os> then run command one by one

Deployment Completed on EC2 instance:

![Screenshot 2025-06-28 215533](https://github.com/user-attachments/assets/3e5889f8-6d8c-4d28-ae8c-b84fbf193124)


# 7. Setup github secrets:

    AWS_ACCESS_KEY_ID=

    AWS_SECRET_ACCESS_KEY=

    AWS_REGION = us-east-1

    AWS_ECR_LOGIN_URI = 737281587410.dkr.ecr.us-east-1.amazonaws.com

    ECR_REPOSITORY_NAME = mlproject




## About MLflow 
MLflow

 - Its Production Grade
 - Trace all of your expriements
 - Logging & tagging your model

List Of Model Trained On Different HyperParameters:

![Screenshot 2025-06-28 194102](https://github.com/user-attachments/assets/49c6ba9c-1fcc-43a4-bbce-fbb8a7881943)

Model Performance Comparison using MLFlow:

![Screenshot 2025-06-28 194046](https://github.com/user-attachments/assets/db3b1d47-22a1-4e84-acbf-7cc02fa85775)

Best Performing Model:

![Screenshot 2025-06-28 194132](https://github.com/user-attachments/assets/499fbfb0-b4d6-47fc-9a70-32c56d081816)



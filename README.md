# MLProject
LearningMoreML

- Still pending deployment in aws. I think I have some issues with the naming (MLProject,mlproj and mlProject) of the repo but this is something that I will try to fix in the future. I am done for now with this project.
-  I will try to do this project for Barcelona Accidents but only with the model itself (a similar project that th one pending of streamlit).


## Workflows
1. Update config.yaml
2. Update schema.yaml
3. Update params.yaml
4. Update entity
5. Update the configuration manager in src config
6. Update components
7. Update pipeline
8. Update main.py
9. Update app.py


I am stuck with the conda environment. I hope it will not bring more problems down the road,

Skipping cleaning in data_validation for this exercise
Data Validation pending task: check the datatype for each column


#  How to run?

## Steps:
Clone the repository
```bash
https://github.com/AlexChicote/MLProject.git
```
### STEP 01 --Create a conda environment
```bash
conda create -n mlProject python =3.11 -y
```

```bash
conda activate mlProject
```
### STEP 02 -- INstall the requirements
```bash
pip install -r requirements.txt
```
```bash
# Run the following command
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

LFLOW_TRACKING_URI=https://dagshub.com/alex.chicote.larregola/MLProject.mlflow \
MLFLOW_TRACKING_USERNAME=alex.chicote.larregola \
MLFLOW_TRACKING_PASSWORD=070d3fe3bfd64012a18020eaa63df393 \
python script.py

Run this to export as env variables:

```bash

export MLFLOW_TRACKING_URI=https://dagshub.com/alex.chicote.larregola/MLProject.mlflow

export MLFLOW_TRACKING_USERNAME=alex.chicote.larregola

export MLFLOW_TRACKING_PASSWORD=070d3fe3bfd64012a18020eaa63df393


```
Maybe this other one 8343a6e76ce9d88db17e6094c94bba912293c423
8343a6e76ce9d88db17e6094c94bba912293c423


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
    - Save the URI: 975365664731.dkr.ecr.us-east-1.amazonaws.com/mlproject

	
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


# 7. Setup github secrets:

    AWS_ACCESS_KEY_ID=

    AWS_SECRET_ACCESS_KEY=

    AWS_REGION = us-east-1

    AWS_ECR_LOGIN_URI = demo>>  566373416292.dkr.ecr.ap-south-1.amazonaws.com

    ECR_REPOSITORY_NAME = simple-app




## About MLflow 
MLflow

 - Its Production Grade
 - Trace all of your expriements
 - Logging & tagging your model


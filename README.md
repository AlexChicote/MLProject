# MLProject
LearningMoreML


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

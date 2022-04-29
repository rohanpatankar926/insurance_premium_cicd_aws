### Internship - Ineuron

### Project Title 
- Insurance Premium Prediction

<img src="https://github.com/Nix-code/Insurance-premium-prediction-Ineuron/blob/main/docs/Insurance.jpg" alt="Insurance">

### Domain
- Insurance

### Problem Statement
<p>The goal of this project is to give people an estimate of how much they need based on
their individual health situation</p>

### Dataset
[Dataset](https://www.kaggle.com/noordeen/insurance-premium-prediction) is provided by Ineuron

### Web application 
- Input 
<img src="https://github.com/Nix-code/Insurance-premium-prediction-Ineuron/blob/main/docs/input.png" alt="input-value">

- Output
<img src="https://github.com/Nix-code/Insurance-premium-prediction-Ineuron/blob/main/docs/output.png" alt="output-value">



### Procedure
<p> Creating the working environment</p>

- You can either use conda environment where you will get pre installed libraries
- You can create virtual environment and install the required libraries manually

## Activate the virtual environment

``` cd virtual env
    source venv/bin/activate
 ```
 1. create template.py
 2. create params.yaml file for structuring your project operations
 3. create dvc.yaml for pipeline
 
 ## Src 
 - src file usually contains the source code we write
 - You can see files like get_data.py or load_data.py inside src file
 
 ## Version Control
 - It is advised to use git for tracking the code , you can also use dvc for tracking the changes
 
 ## Here is simple snippet for tracking
 ```
 pip install -r requirements.txt
 git init
 dvc init
 dvc add data_given/csv
 git add .
 git commit -m "add the changes"
 git remote add origin:HTTP url
 git branch -M main
 git push origin main
 
 ```
 
 ## Tox command
 ```tox```
 
 ## For rebuilding
 
 ``` tox -r ```
 ## pytest 
 
 ``` pytest -v ```
 ## setup
 
 ```pip install -e ```
 
 ## Package building
 
 ```python setup.py sdist bdist_wheel ```
 

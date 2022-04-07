import os
# os.path helps to manage the directories easily irrespective of the operating system 

dirs = [
    os.path.join('data','raw'),
    os.path.join('data','processed'),
    "notebooks",
    "saved_models",
    "src",
    "webapp",
    "reports",
]
for dir in dirs:
    """ exist_ok checks if the folder is already created or not
     if the dir is not created before, it will create new dir
     else it will ignore"""
    os.makedirs(dir, exist_ok = True)
    with open(os.path.join(dir,'.gitkeep'),'w') as f:
        pass

# files for staging and pipeline

files = [
    'dvc.yaml',
    'params.yaml',
    '.gitignore',
    os.path.join('src','__init__.py')
]

# __init__.py ensures that src file is the python package

for file in files:
    with open(file,'w') as f:
        pass

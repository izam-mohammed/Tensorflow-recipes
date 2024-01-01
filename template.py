import os

FOLDERS = [
    "Basics with Keras",
    "Keras",
    "Tensorflow Extended",
    "Tensorflow-lite",
    "Load and preprocessing",
    "Customization",
    "Distributed Training",
    "Vision",
    "Text",
    "Audio",
    "Structured Data",
    "Generative",
    "Model Optimization",
    "Model Understanding",
    "Reinforcement",
]

for folder in FOLDERS:
    folder_path = os.path.join(os.getcwd(), folder)
    os.makedirs(folder_path, exist_ok=True)
    
    # create readme and trials.ipynb
    with open(os.path.join(folder_path,"README.md"), "w") as f:
        print(f"Created the readme in {folder_path}")
    
    with open(os.path.join(folder_path,"trials.ipynb"), "w") as f:
        print(f"Created the trial notebook in {folder_path}")
    
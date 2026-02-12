import os
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "spam_detect"

list_of_files=[
    "data/dataset/.gitkeep",
    "data/models/.gitkeep",
    "NoteBook_Experiments/Spam_Detection.ipynb",
    "outputs/.gitkeep",
    "src/__init__.py",
    "src/components/__init__.py",
    "src/components/data_ingestion.py",
    "src/components/data_transformation.py",
    "src/components/model_training.py",
    "src/config/__init__.py",
    "src/config/config.py",
    "src/pipeline/__init__.py",
    "src/pipeline/prediction_pipeline.py",
    "src/pipeline/training_pipeline.py",
    "src/utils/__init__.py",
    "src/utils/email_utils.py",
    "src/utils/logger.py",
    "src/utils/state.py",
    "src/utils/utils.py",
    "app.py",
    "pyproject.toml",
    "README.md",
    "requirements.txt"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} already exists")
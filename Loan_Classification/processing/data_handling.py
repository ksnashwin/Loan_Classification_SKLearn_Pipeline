import os
import pandas as pd
import joblib
from Loan_Classification.config import config

#load the dataset
def load_dataset(file_name):
    filepath = os.path.join(config.DATA_PATH,file_name)
    _data = pd.read_csv(filepath)
    return _data

#save the dataset - serialization
def save_pipeline(pipeline_to_save):
    save_path = os.path.join(config.SAVE_MODEL_PATH,config.MODEL_NAME)
    joblib.dump(pipeline_to_save,save_path)
    print(f"Model has been saved under the name {config.MODEL_NAME}")

#Desrtialization
def load_pipeline(pipeline_to_load):
    save_path = os.path.join(config.SAVE_MODEL_PATH,config.MODEL_NAME)
    model_loaded = joblib.load(save_path)
    print(f"Model has been loaded")
    return model_loaded


import pandas as pd
import numpy as np
import joblib
from Loan_Classification.config import config  
from Loan_Classification.processing.data_handling import load_pipeline,load_dataset



classification_pipeline = load_pipeline(config.MODEL_NAME)

# def generate_predictions(data_input):
#     data = pd.DataFrame(data_input)
#     pred = classification_pipeline.predict(data[config.FEATURES])
#     output = np.where(pred==1,'Y','N')
#     result = {"prediction":output}
#     return result

def generate_predictions():
    test_data = load_dataset(config.TEST_FILE)
    pred = classification_pipeline.predict(test_data[config.FEATURES])
    output = np.where(pred==1,'Y','N')
    print(output)
    #result = {"Predictions":output}
    return output

if __name__=='__main__':
    generate_predictions()
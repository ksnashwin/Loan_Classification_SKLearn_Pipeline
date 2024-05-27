# import pytest
# from Loan_Classification.config import config
# from Loan_Classification.processing.data_handling import load_dataset
# from Loan_Classification.predict import generate_predictions

# # output from predict script not null
# # output from predict script is str data type
# # output is Y for an example data

# # Fixture --> functions before test function

# @pytest.fixture
# def single_prediction():
#     test_dataset = load_dataset(config.TEST_FILE)
#     single_row = test_dataset[:1]
#     result = generate_predictions(single_row)
#     return result

# def test_single_pred_not_none(single_prediction): # output is not none
#     assert single_prediction is not None
    
# def test_single_pred_str_type(single_prediction): # data type is string
#     assert isinstance(single_prediction.get('prediction')[0],str)
    
# def test_single_pred_validate(single_prediction):
#     assert single_prediction.get('prediction')[0] == 'Y'
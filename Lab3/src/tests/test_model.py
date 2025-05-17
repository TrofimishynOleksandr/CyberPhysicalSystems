import joblib

def test_model_output():
    model = joblib.load('src/ml/model.joblib')
    sample = [15.0]*24
    pred = model.predict([sample])[0]
    assert len(pred) == 24
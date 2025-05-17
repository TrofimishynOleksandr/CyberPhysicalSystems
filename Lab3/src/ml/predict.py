import joblib

def predict_next_day(X_today):
    model = joblib.load('src/ml/model.joblib')
    return model.predict([X_today])[0]
import joblib
from sklearn.datasets import make_regression

#테스트용 데이터
X, x = make_regression(n_samples=100, n_features=1, noise=0.1)

#모델 로드
loaded_model = joblib.load('linear_model.pkl')
print('load ok!')


#모델 사용
y_pred = loaded_model.predict(X)
print(y_pred)
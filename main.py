# example of gaussian naive bayes 
from sklearn.datasets import make_blobs
from sklearn.naive_bayes import GaussianNB 

# generate 2d classfication datasets
X, y = make_blobs(n_samples=100, centers=2, n_features=2, random_state=1)

# define the model
model = GaussianNB() 

# fit the model
model.fit(X, y)

# select a single sample
Xsample, ysample = [X[0]], y[0]

# make a probabilistic prediction
yhat_prob = model.predict_proba(Xsample) 
print('Predicted probabilities: ', yhat_prob)

# make a classification prediction 
yhat_class = model.predict(Xsample)
print('Predicted Class: ', yhat_class)
print('Truth y=%d' % ysample)
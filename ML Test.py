import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import BernoulliNB
from sklearn.naive_bayes import GaussianNB

classifier = SVC()
classifier2 = DecisionTreeClassifier()
classifier3 = BernoulliNB()
classifier4 = GaussianNB()

dfA = pd.read_csv('Training_set.txt', sep=',').sample(n=200)
vector = zip(dfA['n12'].values.tolist(), dfA['n21'].values.tolist(), dfA['p12'].values.tolist(), dfA['p21'].values.tolist(), dfA['a12'].values.tolist(), dfA['a21'].values.tolist(), dfA['result'].values.tolist())
rem_dup = []
listA = []
for i in vector:
    if i not in rem_dup:
        rem_dup.append(list(i))

train_x = [i[:6] for i in rem_dup[:195]]
print(train_x)
train_y = [i[6] for i in rem_dup[:195]]
print(train_y)
test_x = [i[:6] for i in rem_dup[195:]]
test_y = [i[6] for i in rem_dup[195:]]

classifier.fit(train_x, train_y)
classifier2.fit(train_x, train_y)
classifier3.fit(train_x, train_y)
classifier4.fit(train_x, train_y)


prediction = classifier.predict(test_x)
prediction2 = classifier2.predict(test_x)
prediction3 = classifier3.predict(test_x)
prediction4 = classifier4.predict(test_x)


score1 = accuracy_score(test_y, prediction)
score2 = accuracy_score(test_y, prediction2)
score3 = accuracy_score(test_y, prediction3)
score4 = accuracy_score(test_y, prediction4)

print(str(test_y).replace(',', ''))
print(prediction)
print(prediction2)
print(prediction3)
print(prediction4)
print(score1, score2, score3, score4)




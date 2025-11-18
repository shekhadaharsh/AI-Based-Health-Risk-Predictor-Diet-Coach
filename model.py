import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pickle

df =pd.read_csv("health_data.csv")

# print(df.head())

le=LabelEncoder()

df['smoking'] = le.fit_transform(df['smoking'])
df['activity'] = le.fit_transform(df['activity'])
df['disease'] = le.fit_transform(df['disease'])
df['diet'] = le.fit_transform(df['diet'])
df['risk'] = le.fit_transform(df['risk'])


X=df.drop('risk',axis=1)
y=df['risk']

X_train,X_test, y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
model=RandomForestClassifier()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"model Accuracy: {accuracy*100:.2f}%")

pickle.dump(model, open("health_model.pkl", "wb")) 

# print("Model saved successfully as 'health_model.pkl'")
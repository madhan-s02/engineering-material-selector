import pandas as pd
df = pd.read_csv("data/Material.csv")
print("shape of dataset:",df.shape)
print("\nFirst 5 rows:")
print(df.head())
print("\nColumn names:")
print(df.columns.to_list())
print("\nData types")
print(df.dtypes)
print("\n any missing value")
print(df.isnull().sum())

from sklearn.preprocessing import LabelEncoder
df = df.drop("Material",axis=1)
le = LabelEncoder()
df["Cost"] = le.fit_transform(df["Cost"])
df["Weight"] = le.fit_transform(df["Weight"])
df["Corrosion_Resistance"] = le.fit_transform(df["Corrosion_Resistance"])
target_encoder = LabelEncoder()
df["Best_For"] = target_encoder.fit_transform(df["Best_For"])
print("After Encoding:")
print(df.head())
print("\nUnique values in Best_For:",df["Best_For"].unique())
print("\nBest_For classes:",target_encoder.classes_)

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
x = df.drop("Best_For",axis=1)
y = df["Best_For"]
x_train, x_test, y_train,y_test = train_test_split(x,y, test_size=0.1, random_state=42)
print("\nTraining samples:",x_train.shape[0])
print("Testing sample:",x_test.shape[0])
model = RandomForestClassifier(n_estimators=100,random_state=42)
model.fit(x_train,y_train)
y_pred = model.predict(x_test)
accuracy = accuracy_score(y_test,y_pred)
print("\nModel Accuracy:",round(accuracy*100,2),"%")
print("\nActual values:   ", y_test.values)
print("Predicted values:", y_pred)
print("\nTraining accuracy:", round(model.score(x_train, y_train)*100, 2), "%")

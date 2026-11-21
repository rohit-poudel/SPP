from sklearn.model_selection import train_test_split
import pandas as pd

df = pd.read_csv(r"data\raw\student\student-mat.csv", sep=";")

y = df["G3"]
X = df.drop(columns=["G3"])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print("X_train", X_train.shape)
print("y_train", y_train.shape)
print("X_test", X_test.shape)
print("y_test", y_test.shape)

print("Features X:", X.shape)#feature
print("Target y:", y.shape)#target 

guess = y_train.mean()#x_train not used as it has features and y_train used as it has grades
errors = (y_test -guess).abs()#y_test has the true grade
mae = errors.mean() #got 3.65
print("Baseline guess:", guess)
print("Baseline MAE:", mae)
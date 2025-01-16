# Import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from tkinter import *
import tkinter as tk

# Step 1: Read and Analyze the Dataset
df = pd.read_csv("heart.csv")

# Display the first 5 records
print(df.head())

# Check dataset info and missing values
print(df.info())

# Statistical summary of numeric columns
print(df.describe())

# Target distribution
print(df.target.value_counts())

# Plot target counts
sns.countplot(x="target", data=df, palette="bwr")
plt.show()

# Plot gender distribution
sns.countplot(x='sex', data=df, palette="mako_r")
plt.xlabel("Sex (0 = female, 1= male)")
plt.show()

# Analyze gender vs. target
pd.crosstab(df.sex, df.target).plot(kind="bar", figsize=(15, 6), color=['#1CA53B', '#AA1111'])
plt.title('Heart Disease Frequency for Sex')
plt.xlabel('Sex (0 = Female, 1 = Male)')
plt.xticks(rotation=0)
plt.legend(["Haven't Disease", "Have Disease"])
plt.ylabel('Frequency')
plt.show()

# Step 2: Visualizations
sns.scatterplot(x='age', y='thalach', hue='target', data=df)
plt.title("Scatter plot: Age vs. Maximum Heart Rate (Hue = Target)")
plt.show()

# Correlation Matrix
corr_matrix = df.corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Matrix')
plt.show()

# Step 3: Data Preprocessing
# Handle categorical variables using one-hot encoding
a = pd.get_dummies(df['cp'], prefix="cp")
b = pd.get_dummies(df['thal'], prefix="thal")
c = pd.get_dummies(df['slope'], prefix="slope")

# Combine the new columns with the original dataframe and drop the old ones
df = pd.concat([df, a, b, c], axis=1)
df = df.drop(columns=['cp', 'thal', 'slope'])

# Define target variable 'y' and feature variables 'X'
y = df.target.values
X = df.drop(['target'], axis=1)

# Scaling the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Step 3a: Logistic Regression Model
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)

# Logistic Regression Model
lr = LogisticRegression()
lr.fit(X_train, y_train)

# Evaluate the Logistic Regression model
lr_acc = lr.score(X_test, y_test) * 100
print(f"Logistic Regression Accuracy: {lr_acc:.2f}%")

# Confusion Matrix for Logistic Regression
lr_pred = lr.predict(X_test)
lr_cm = confusion_matrix(y_test, lr_pred)
lr_disp = ConfusionMatrixDisplay(confusion_matrix=lr_cm)
lr_disp.plot(cmap='Blues')
plt.title('Logistic Regression - Confusion Matrix')
plt.show()

# Step 3b: KNN Model
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

# Evaluate the KNN model
knn_acc = knn.score(X_test, y_test) * 100
print(f"KNN Accuracy: {knn_acc:.2f}%")

# Confusion Matrix for KNN
knn_pred = knn.predict(X_test)
knn_cm = confusion_matrix(y_test, knn_pred)
knn_disp = ConfusionMatrixDisplay(confusion_matrix=knn_cm)
knn_disp.plot(cmap='Blues')
plt.title('KNN - Confusion Matrix')
plt.show()

# Step 4: Build the GUI for Heart Disease Classification
def check_inputs():
    if age.get() == "":
        print("Age Field is Empty!!")
        Label(win, text="Age Field is Empty!!", fg="blue", bg="yellow", font=("Calibri 10 bold")).place(x=12, y=580)
    elif rbp.get() == "":
        print("Resting Blood Pressure Field is Empty!!")
        Label(win, text="Resting Blood Pressure Field is Empty!!", fg="blue", bg="yellow", font=("Calibri 10 bold")).place(x=12, y=580)
    elif chol.get() == "":
        print("Cholestrol Field is Empty!!")
        Label(win, text="Cholestrol Field is Empty!!", fg="blue", bg="yellow", font=("Calibri 10 bold")).place(x=12, y=580)
    elif heart_rate.get() == "":
        print("Heart Rate Field is Empty!!")
        Label(win, text="Heart Rate Field is Empty!!", fg="blue", bg="yellow", font=("Calibri 10 bold")).place(x=12, y=580)
    elif peak.get() == "":
        print("Depression By Exercise Field is Empty!!")
        Label(win, text="Depression By Exercise Field is Empty!!", fg="blue", bg="yellow", font=("Calibri 10 bold")).place(x=12, y=580)
    else:
        predict()

def predict():
    # Define necessary dictionaries for encoding
    gender_dict = {"Male": 1, "Female": 0}
    fbs_dict = {"True": 1, "False": 0}
    eia_dict = {"True": 1, "False": 0}
    cp_dict = {"1: typical angina": 0, "2: atypical angina": 1, "3: non-anginal pain": 2, "4: asymptomatic": 3}
    thal_dict = {"0: No Test": 0, "1: Fixed Defect": 1, "2: Normal Flow": 2, "3: Reversible Defect": 3}
    pred_dict = {0: "Prediction: No Heart Disease Detected", 1: "Prediction: Signs of Heart Disease Detected\nYou should consult with your Doctor!"}
    
    data = [float(age.get()), gender_dict[str(radio.get())], cp_dict[str(variable.get())], float(rbp.get()),
            float(chol.get()), fbs_dict[str(radio_fbs.get())], int(str(variable_ecg.get())) - 1, float(heart_rate.get()),
            eia_dict[str(radio_eia.get())], float(peak.get()), int(str(variable_slope.get())) - 1, int(str(variable_n_vessels.get())) - 1,
            thal_dict[str(variable_thal.get())]]
    
    # Predict using the Logistic Regression model
    prediction = lr.predict(np.array(data).reshape(1, -1))
    pred_label = pred_dict[prediction.tolist()[0]]
    Label(win, text=pred_label, fg="blue", bg="yellow", font=("Calibri 10 bold")).place(x=12, y=580)

def reset():
    age.set("")
    rbp.set("")
    chol.set("")
    heart_rate.set("")
    peak.set("")

# Create the GUI
win = Tk()
win.geometry("450x600")
win.configure(background="#Eaedee")
win.title("Heart Disease Classifier")

title = Label(win, text="Heart Disease Classifier", bg="#2583be", width="300", height="2", fg="white", font=("Arial 20 italic")).pack()

# Define labels and input fields for the GUI
age = StringVar()
rbp = StringVar()
chol = StringVar()
heart_rate = StringVar()
peak = StringVar()

entry_age = Entry(win, textvariable=age, width=30)
entry_age.place(x=150, y=65)

entry_rbp = Entry(win, textvariable=rbp, width=30)
entry_rbp.place(x=150, y=105)

entry_chol = Entry(win, textvariable=chol, width=30)
entry_chol.place(x=150, y=145)

entry_heart_rate = Entry(win, textvariable=heart_rate, width=30)
entry_heart_rate.place(x=150, y=185)

entry_peak = Entry(win, textvariable=peak, width=30)
entry_peak.place(x=150, y=225)

reset = Button(win, text="Reset", width="12", height="1", activebackground="red", command=reset, bg="Pink", font=("Calibri 12 ")).place(x=24, y=540)
submit = Button(win, text="Classify", width="12", height="1", activebackground="violet", bg="Pink", command=check_inputs, font=("Calibri 12 ")).place(x=240, y=540)

win.mainloop()

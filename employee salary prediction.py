#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import tkinter as tk
from tkinter import messagebox, filedialog

def load_and_train():
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file_path:
        try:
            df = pd.read_csv(file_path)
            if 'Experience' in df.columns and 'Education_Level' in df.columns and 'Age' in df.columns and 'Salary' in df.columns:
                X = df[['Experience', 'Education_Level', 'Age']]
                y = df['Salary']
                global model
                model = LinearRegression()
                model.fit(X, y)
                messagebox.showinfo("Success", "Model trained successfully!")
            else:
                messagebox.showerror("Error", "CSV must contain: Experience, Education_Level, Age, Salary")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load or train:\n{e}")

def predict_salary():
    try:
        exp = float(entry_exp.get())
        edu = float(entry_edu.get())
        age = float(entry_age.get())
        prediction = model.predict([[exp, edu, age]])
        messagebox.showinfo("Predicted Salary", f"Estimated Salary: ₹{prediction[0]:,.2f}")
    except Exception as e:
        messagebox.showerror("Error", f"Prediction failed:\n{e}")

# GUI
root = tk.Tk()
root.title("Employee Salary Predictor")
root.geometry("400x300")

tk.Label(root, text="Employee Salary Predictor", font=("Arial", 16)).pack(pady=10)
tk.Button(root, text="Load CSV & Train Model", command=load_and_train).pack(pady=5)

tk.Label(root, text="Experience (years):").pack()
entry_exp = tk.Entry(root)
entry_exp.pack()

tk.Label(root, text="Education Level (1-Bachelor, 2-Master, 3-PhD):").pack()
entry_edu = tk.Entry(root)
entry_edu.pack()

tk.Label(root, text="Age:").pack()
entry_age = tk.Entry(root)
entry_age.pack()

tk.Button(root, text="Predict Salary", command=predict_salary).pack(pady=15)

root.mainloop()


# In[ ]:





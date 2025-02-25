# 🚀 Datathon Machine Learning Model

## 📌 Project Overview
This project is designed to **predict daily sales quantities** for infrastructure machinery using an **XGBoost regression model**. The model considers various factors such as **market share, political influence, marketing efforts, and regional impact**. The goal is to improve **sales forecasting accuracy** for better business decisions.

🔗 **Live Demo**: [Datathon ML](https://datathonml.streamlit.app/)

---

## 🛠 Tech Stack
- **Python** (pandas, numpy, sklearn, XGBoost, joblib, pulp)
- **Jupyter Notebook** (Data Processing & Model Training)
- **Streamlit** (Web App for Prediction)
- **GitHub** (Version Control & Documentation)

---

## 📂 Dataset
The dataset contains information about **past sales records**, including:
- Date
- Infrastructure machinery type
- Market Share
- Marketing budget
- Political factors
- Region
- Daily sales quantity

## 🛠️ Workflow
### **1️⃣ Data Preprocessing**
- Loaded the dataset and removed **invalid machinery types**.
- Converted `Date` column to **datetime format**.
- Extracted new features: `year`, `month`, `day`, and `dayofweek`.
- One-hot encoded categorical columns (`Infrastructure_Machineries` & `Region`).

### **2️⃣ Exploratory Data Analysis (EDA)**
- **Visualized sales trends** over time using line plots.
- **Checked data distribution** to detect outliers.
- **Created correlation heatmaps** to identify feature relationships.

### **3️⃣ Model Training**
- Used **XGBoost Regressor** for training.
- Split data into **train & test sets**.
- Tuned hyperparameters for **better accuracy**.

### **4️⃣ Prediction**
- Prepared **new input data** following the same processing steps.
- Predicted **future sales quantity** for a given date and parameters.

### **5️⃣ Deployment with Streamlit**
- Developed a **web-based UI** for easy interaction.
- Users can **input parameters** and get **real-time sales predictions**.

---

## 📌 Installation & Setup

### **2️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
```

### **3️⃣ Run the Streamlit App**
```sh
streamlit run app.py
```

---

## 🚀 Understanding Streamlit
**Streamlit** is a Python framework for building **interactive web applications** with minimal code. It is useful for deploying **machine learning models** quickly.

### **🔹 Key Features**
✅ Simple syntax for UI elements (`st.title()`, `st.text_input()`, `st.button()`).  
✅ Real-time interaction with **dynamic updates**.  
✅ Supports **data visualization**, tables, and model outputs.  
✅ Runs locally and can be **hosted on cloud platforms**.  

### **🔹 How We Used Streamlit**
- Created a **user-friendly UI** where users **input features**.
- Displayed **real-time predictions** using our trained XGBoost model.
- Integrated **charts and tables** for a better user experience.

---

## 📌 Team Members
- **Deepan B** 
- **Balaji D** 



## ⭐ Support
If you like this project, give it a ⭐ on GitHub!

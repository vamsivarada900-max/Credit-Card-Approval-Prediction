# 💳 Credit Card Approval Prediction using Machine Learning

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-Web%20App-black?style=for-the-badge&logo=flask)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?style=for-the-badge&logo=scikitlearn)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

## 📌 Project Overview

This project predicts whether a credit card application should be **Approved** or **Rejected** using Machine Learning.

The application takes applicant details such as income, education, occupation, family status, age, employment years, etc., preprocesses the data, and uses a trained **Random Forest Classifier** to make predictions.

A simple and interactive **Flask Web Application** allows users to enter applicant information and instantly view the prediction.

---

# 🚀 Features

- Credit Card Approval Prediction
- Machine Learning Model (Random Forest)
- Data Preprocessing
- Label Encoding
- Feature Scaling
- Flask Web Application
- User-friendly Interface
- Real-time Predictions

---

# 📂 Project Structure

```
Credit-Card-Approval-Prediction/
│
├── app.py
├── model.pkl
├── scaler.pkl
├── encoders.pkl
├── requirements.txt
├── README.md
│
├── templates/
│   ├── home.html
│   ├── index.html
│   └── result.html
│
├── static/
│   └── style.css
│
├── notebooks/
│   ├── 01_Data_Cleaning.ipynb
│   ├── 02_Preprocessing.ipynb
│   └── 03_Model_Building.ipynb
│
└── data set/
    ├── application_record.csv
    ├── credit_record.csv
    └── processed_credit_card_data.csv
```

---

# 🛠 Technologies Used

- Python
- Flask
- Pandas
- NumPy
- Scikit-learn
- Joblib
- HTML
- CSS

---

# 🤖 Machine Learning Workflow

### Data Collection

- Application Record Dataset
- Credit Record Dataset

### Data Preprocessing

- Missing Value Handling
- Feature Engineering
- Label Encoding
- Standard Scaling

### Model Training

Several machine learning algorithms were evaluated, including:

- Decision Tree
- Logistic Regression
- K-Nearest Neighbors (KNN)
- Support Vector Machine (SVM)
- **Random Forest (Selected Model)**

Random Forest was selected because it provided the best overall performance for this project.

---

# 📊 Input Features

The model uses the following applicant information:

- Gender
- Own Car
- Own Property
- Number of Children
- Annual Income
- Income Type
- Education Level
- Family Status
- Housing Type
- Mobile Phone
- Work Phone
- Phone
- Email
- Occupation
- Family Members
- Age
- Employment Years

---

# 💻 Running the Project

## Clone Repository

```bash
git clone https://github.com/vamsivarada900-max/Credit-Card-Approval-Prediction.git
```

## Move into Project Folder

```bash
cd Credit-Card-Approval-Prediction
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run Flask App

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000/
```

---

# 📸 Screenshots

## Home Page

> *<img width="1849" height="852" alt="home" src="https://github.com/user-attachments/assets/8dd7e650-91e5-4618-b5a5-2efbdec06aff" />
*

---

## Prediction Form

> *<img width="1849" height="852" alt="prediction form" src="https://github.com/user-attachments/assets/c4ee389e-05f9-4740-aec9-5ad8294bda41" />
*

---

## Prediction Result

> *<img width="1862" height="851" alt="prediction result" src="https://github.com/user-attachments/assets/b34d1f7a-d2e8-43fe-bfce-171c16a20de3" />
*

---

# 📈 Future Improvements

- Improve handling of class imbalance
- Hyperparameter tuning
- Deploy on Render or Railway
- Add probability score to prediction
- Explain predictions using SHAP
- Responsive UI improvements

---

# ⚠ Note

The dataset used in this project is **highly imbalanced**, which may lead to a bias toward approval predictions. Future versions will incorporate balancing techniques such as **SMOTE** or **class weighting** to improve performance on minority-class predictions.

---

## 👥 Team Members

This project was developed as a group project by:

- Vamsi Krishna Varada
- Niveditha
- Meghana Reddy
- sravya 

---

## 🤝 Contributions

- **Data Collection & Preprocessing**
- **Feature Engineering**
- **Machine Learning Model Development**
- **Flask Web Application**
- **Frontend Design (HTML/CSS)**
- **Testing & Documentation**

Each team member contributed to different phases of the project.rning

GitHub:
https://github.com/vamsivarada900-max

---

# ⭐ Support

If you found this project helpful, please consider giving it a ⭐ on GitHub.

It motivates me to build more Machine Learning projects.

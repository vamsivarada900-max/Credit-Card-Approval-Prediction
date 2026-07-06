from flask import Flask, render_template, request
import pandas as pd
import joblib
import os

# Initialize Flask App
app = Flask(__name__)

# Load Model, Scaler and Encoders
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")
encoders = joblib.load("encoders.pkl")
print("Current Folder:", os.getcwd())
print("Model Type:", type(model))



# ==========================================
# Home Pag e
# ==========================================

@app.route('/')
def home():
    return render_template('home.html')



# ==========================================
# Prediction Form
# ==========================================

@app.route('/predict')
def predict_page():
    return render_template('index.html')


# ==========================================
#Prediction Logic
# ==========================================

@app.route('/result', methods=['POST'])
def result():

    # Get form data
    form_data = request.form.to_dict()

    # Convert to DataFrame
    input_df = pd.DataFrame([form_data])

    # Separate categorical and numerical columns
    categorical_columns = [
        'CODE_GENDER',
        'FLAG_OWN_CAR',
        'FLAG_OWN_REALTY',
        'NAME_INCOME_TYPE',
        'NAME_EDUCATION_TYPE',
        'NAME_FAMILY_STATUS',
        'NAME_HOUSING_TYPE',
        'OCCUPATION_TYPE'
    ]

    numerical_columns = [
        'CNT_CHILDREN',
        'AMT_INCOME_TOTAL',
        'FLAG_MOBIL',
        'FLAG_WORK_PHONE',
        'FLAG_PHONE',
        'FLAG_EMAIL',
        'CNT_FAM_MEMBERS',
        'AGE',
        'EMPLOYMENT_YEARS'
    ]
       # Encode categorical columns
    print("\n===== INPUT DATA =====")
    print(input_df)

    for column in categorical_columns:
      print(f"\nEncoding: {column}")
      print("Value:", input_df[column].tolist())
      print("Classes:", encoders[column].classes_)

      input_df[column] = encoders[column].transform(
        input_df[column].astype(str)
    )
        # Convert numerical columns to float
    for column in numerical_columns:
        input_df[column] = input_df[column].astype(float)

        # Arrange columns in training order
    input_df = input_df[[
        'CODE_GENDER',
        'FLAG_OWN_CAR',
        'FLAG_OWN_REALTY',
        'CNT_CHILDREN',
        'AMT_INCOME_TOTAL',
        'NAME_INCOME_TYPE',
        'NAME_EDUCATION_TYPE',
        'NAME_FAMILY_STATUS',
        'NAME_HOUSING_TYPE',
        'FLAG_MOBIL',
        'FLAG_WORK_PHONE',
        'FLAG_PHONE',
        'FLAG_EMAIL',
        'OCCUPATION_TYPE',
        'CNT_FAM_MEMBERS',
        'AGE',
        'EMPLOYMENT_YEARS'
    ]]

        # Scale input
    print("\n===== AFTER ENCODING =====")
    print(input_df)
    print(input_df.dtypes)
    
    print("STEP 1")

    print("STEP 1")

    input_scaled = scaler.transform(input_df)

    print("STEP 2")

    prediction = model.predict(input_scaled)[0]

    print("STEP 3")

    print("Prediction =", prediction)

    print("STEP 4")

    print(model.predict_proba(input_scaled))

    print("STEP 5")

    if hasattr(model, "predict_proba"):
      print("Prediction Probability =", model.predict_proba(input_scaled))

    if prediction == 0:
      result = "✅ Credit Card Approved"
    else:
      result = "❌ Credit Card Rejected"

    return render_template("result.html", prediction=result)
    

encoders = joblib.load("encoders.pkl")
print("Encoder path loaded successfully")
print(encoders["CODE_GENDER"].classes_)
print(encoders["FLAG_OWN_CAR"].classes_)
print(type(encoders))
print(encoders.keys())
print(encoders["CODE_GENDER"].classes_)

if __name__ == "__main__":
    app.run(debug=True)
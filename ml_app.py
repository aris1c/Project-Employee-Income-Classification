import streamlit as st
import pandas as pd
import joblib 
import os

def load_model(model_file):
    loaded_model = joblib.load(open(os.path.join(model_file), "rb"))
    return loaded_model 

def run_ml_app():
    st.subheader("Machine Learning Selection")
    
    # Memuat model
    model = load_model('income_model.pkl') 

    # Siapkan list untuk pilihan fitur
    workclass_options = ['State-gov', 'Self-emp-not-inc', 'Private', 'Federal-gov', 'Local-gov', '?', 'Self-emp-inc', 'Without-pay', 'Never-worked']
    education_options = ['Bachelors', 'HS-grad', '11th', 'Masters', '9th', 'Some-college', 'Assoc-acdm', 'Assoc-voc', '7th-8th', 'Doctorate', 'Prof-school', '5th-6th', '10th', '1st-4th', 'Preschool', '12th']
    marital_status_options = ['Never-married', 'Married-civ-spouse', 'Widowed', 'Divorced', 'Separated', 'Married-spouse-absent', 'Married-AF-spouse']
    occupation_options = ['Adm-clerical', 'Exec-managerial', 'Handlers-cleaners', 'Prof-specialty', 'Other-service', 'Sales', 'Craft-repair', 'Farming-fishing', 'Tech-support', 'Transport-moving', 'Priv-house-serv', 'Machine-op-inspct', 'Armed-Forces', '?']
    relationship_options = ['Not-in-family', 'Husband', 'Wife', 'Own-child', 'Unmarried', 'Other-relative']
    race_options = ['White', 'Black', 'Asian-Pac-Islander', 'Amer-Indian-Eskimo', 'Other']
    gender_options = ['Male', 'Female']
    native_country_options = ['United-States', 'Mexico', 'Philippines', 'Puerto-Rico', 'Germany', 'Canada', 'El-Salvador', 'Cuba', 'Jamaica', 'Italy', 'Vietnam', 'Ecuador', 'Dominican-Republic', 'Guatemala', 'England', 'Columbia', 'Poland', 'South', 'Japan', 'Haiti', 'Portugal', 'Taiwan', 'Peru', 'Iran', 'Honduras', 'India', 'Thailand', 'Nicaragua', 'Greece', 'Trinadad&Tobago', 'Hungary', 'Laos', 'China', 'Outlying-US(Guam-USVI-etc)', 'France', 'Scotland', 'Cambodia', 'Yugoslavia', 'Holand-Netherlands', 'Hong', 'Ireland']

    st.markdown("---")
    
    # Buat form input untuk semua 14 fitur
    with st.form("input_form"):
        st.write("Silakan masukkan data berikut:")
        
        # Fitur numerik
        age = st.number_input('Age', value=30)
        fnlwgt = st.number_input('Final Weight', value=100000)
        educational_num = st.number_input('Educational Number', value=10)
        capital_gain = st.number_input('Capital Gain', value=0)
        capital_loss = st.number_input('Capital Loss', value=0)
        hours_per_week = st.number_input('Hours per Week', value=40)
        
        # Fitur kategorikal
        workclass = st.selectbox('Workclass', options=workclass_options, index=workclass_options.index('Private'))
        education = st.selectbox('Education', options=education_options, index=education_options.index('Bachelors'))
        marital_status = st.selectbox('Marital Status', options=marital_status_options, index=marital_status_options.index('Married-civ-spouse'))
        occupation = st.selectbox('Occupation', options=occupation_options, index=occupation_options.index('Exec-managerial'))
        relationship = st.selectbox('Relationship', options=relationship_options, index=relationship_options.index('Husband'))
        race = st.selectbox('Race', options=race_options, index=race_options.index('White'))
        gender = st.selectbox('Gender', options=gender_options, index=gender_options.index('Male'))
        native_country = st.selectbox('Native Country', options=native_country_options, index=native_country_options.index('United-States'))

        submitted = st.form_submit_button("Predict")

    st.markdown("---")
    
    if submitted:
        # Buat dictionary dengan nama kolom yang BENAR (sesuai pesan error)
        single_data = {
            'Age': age,
            'Workclass': workclass,
            'Final Weight': fnlwgt,
            'Education': education,
            'EducationNum': educational_num,
            'Marital Status': marital_status,
            'Occupation': occupation,
            'Relationship': relationship,
            'Race': race,
            'Gender': gender,
            'Capital Gain': capital_gain,
            'capital loss': capital_loss,
            'Hours per Week': hours_per_week,
            'Native Country': native_country
        }

        # Ubah dictionary menjadi DataFrame
        single_array_df = pd.DataFrame([single_data])
        
        st.subheader("Selected Input Data:")
        st.write(single_array_df)

        # Melakukan prediksi
        prediction = model.predict(single_array_df)
        pred_proba = model.predict_proba(single_array_df)
        
        # Menyusun hasil prediksi probabilitas
        pred_probability_score = {'<=50K': pred_proba[0][0], '>50K': pred_proba[0][1]}

        # Menampilkan hasil prediksi
        st.subheader("Prediction Result")
        
        if prediction[0] == 1:
            st.success("The Employee's Income is more than 50K")
            st.write(pred_probability_score)
        else:
            st.warning("The Employee's Income is less than or equal to 50K")
            st.write(pred_probability_score)
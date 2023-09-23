import streamlit as st
import pickle

with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

def predict_gpa(sat_score, attendance):
    sat_score = int(sat_score)
    attendance = int(attendance)
    prediction = model.predict([[1, sat_score, attendance]])
    return float(prediction)

def main():
    st.title('GPA Predictor')
    st.write('Enter 1 if attendance is 75% or above else 0 in Attendance field')
    sat_score = st.text_input("SAT Score")
    attendance = st.text_input("Attendance")
    try:
        if st.button('Predict'):
            output = predict_gpa(sat_score, attendance)
            st.success(f'Predicted GPA is: {output}')
    except ValueError as e:
        st.warning('Please enter valid value in empty field(s)')

if __name__ == '__main__':
    main()

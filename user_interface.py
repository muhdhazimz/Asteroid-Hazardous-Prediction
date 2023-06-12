import joblib
import pandas as pd
import streamlit as st

st.title("Asteroid Hazardous Prediction")

AbsoluteMagnitude = st.number_input("Enter Absolute Magnitude:", 1, 117)
RelativeVelocitykmperhr = st.number_input("Enter Relative Velocity km per hr:", 1, 136)
OrbitUncertainity = st.number_input("Enter Orbit Uncertainity:", 1, 193)
MinimumOrbitIntersection = st.number_input("Enter your Minimum Orbit Intersection:", 1, 136)
PerihelionDistance = st.number_input("Enter Perihelion Distance:", 1, 193)

user_input = pd.DataFrame([[AbsoluteMagnitude, RelativeVelocitykmperhr, OrbitUncertainity, MinimumOrbitIntersection, PerihelionDistance]], columns=['Absolute Magnitude', 'Relative Velocity km per hr', 'Orbit Uncertainity', 'Minimum Orbit Intersection', 'Perihelion Distance'])
model = joblib.load('hybridmodel.pkl')

prediction = model.predict(user_input)

if st.button("Predict"):
    st.write("The asteroid is", prediction[0])

pd.show_versions()

import streamlit as st
import plotly.express as px
from backened import get_data

st.title("Weather forecast for the next days")
place = st.text_input("place: ")
days = st.slider("forecast days", min_value=1, max_value=5,
                 help="select the number for forecast days")
option = st.selectbox("select data to view", ("Temperature", "Sky"))
st.subheader(f'{option} for the next {days} days in {place}')


if place:

    try:
        # Get data
        filtered_data = get_data(place, days)
        if option == "Temperature":
            temperatures = [dict["main"]["temp"] / 10 for dict in filtered_data]
            dates=[dict["dt_txt"] for dict in filtered_data]

        # Create line plot

        try:
            figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature (C)"})
            st.plotly_chart(figure)

            if option == "Sky":
                images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png",
                "Rain":"images/rain.png", "Snow": "images/snow.png"}
                sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
                image_path = [images[condition] for condition in sky_conditions]
                print(sky_conditions)
                st.image()
        except NameError:
            st.write("Sky option is under process, Please check for temperature option.")
    except KeyError:
        st.write("That place does not exist")



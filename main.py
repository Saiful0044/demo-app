import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set the title of the app
st.title("Streamlit Demo App 🚀")

# Add a sidebar for additional options
st.sidebar.header("Settings")

# Add a file uploader to the sidebar
uploaded_file = st.sidebar.file_uploader("Upload a CSV file", type=["csv"])

# Display some text
st.write("This is a simple Streamlit app to demonstrate its features.")

# Add a slider for user input
slider_value = st.slider("Select a number", 0, 100, 50)
st.write(f"You selected: {slider_value}")

# Add a checkbox to toggle display
if st.checkbox("Show a random DataFrame"):
    st.write("### Random DataFrame")
    random_data = pd.DataFrame({
        "Column A": np.random.randn(10),
        "Column B": np.random.rand(10)
    })
    st.dataframe(random_data)

# Add a selectbox for user choice
option = st.selectbox("Choose a visualization", ["Line Chart", "Bar Chart", "Scatter Plot"])

# Generate some sample data
data = pd.DataFrame({
    "x": np.arange(1, 101),
    "y": np.random.randn(100).cumsum()
})

# Display the selected visualization
if option == "Line Chart":
    st.write("### Line Chart")
    st.line_chart(data.set_index("x"))
elif option == "Bar Chart":
    st.write("### Bar Chart")
    st.bar_chart(data.set_index("x"))
elif option == "Scatter Plot":
    st.write("### Scatter Plot")
    fig, ax = plt.subplots()
    sns.scatterplot(x="x", y="y", data=data, ax=ax)
    st.pyplot(fig)

# If a CSV file is uploaded, display its contents
if uploaded_file is not None:
    st.write("### Uploaded CSV Data")
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)

    # Show a summary of the data
    st.write("### Summary Statistics")
    st.write(df.describe())

    # Allow the user to select a column for histogram
    column_to_plot = st.selectbox("Select a column to plot", df.columns)
    st.write(f"### Histogram for {column_to_plot}")
    fig, ax = plt.subplots()
    sns.histplot(df[column_to_plot], kde=True, ax=ax)
    st.pyplot(fig)

# Add a button for fun
if st.button("Click me!"):
    st.balloons()  # Show balloons animation
    st.write("🎉 You clicked the button!")

# Add a markdown section
st.markdown("""
### About This App
This is a demo app built with **Streamlit** to showcase its capabilities:
- Interactive widgets (sliders, buttons, checkboxes, etc.)
- Data visualization (charts, plots, etc.)
- File upload and data processing
- Markdown support for rich text
""")
st.header('Course')
st.subheader('DDC')
st.subheader("EEE")
st.subheader("FFFF")
st.subheader("python")
st.subheader("SQl")
st.subheader("EEE")
st.sidebar.title("Menu")
st.sidebar.markdown("""
- Home
- About
- Contact
""")
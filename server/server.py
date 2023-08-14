import streamlit as st
import util

# Load saved artifacts
util.load_saved_artifacts()

def classify_image(image_data):
    return util.classify_image(image_data)

def main():
    st.title("Sports Celebrity Image Classification")

    image_data = st.text_area("Paste your image data here:", "")

    if st.button("Classify"):
        result = classify_image(image_data)
        st.write("Prediction:", result)

if __name__ == "__main__":
    main()

import streamlit as st
from PIL import Image
import numpy as np

# Background removal function
def remove_background(image):
    # Implement your background removal algorithm here
    # Replace the following line with your actual implementation
    processed_image = np.array(image)  # Placeholder
    return processed_image

def main():
    st.title("Background Removal Tool")
    uploaded_image = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_image is not None:
        image = Image.open(uploaded_image)
        st.image(image, caption="Original Image", use_column_width=True)

        if st.button("Remove Background"):
            processed_image = remove_background(image)
            st.image(processed_image, caption="Image with Background Removed", use_column_width=True)

if __name__ == "__main__":
    main()

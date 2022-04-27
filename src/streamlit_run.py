import os
import sys

import cv2
import numpy as np
import streamlit as st
from loguru import logger
import matplotlib.pyplot as plt

from modules.request import post

logger.configure(
    handlers=[
        {"sink": sys.stderr, "level": "DEBUG"},
        dict(
            sink="logs/debug.log",
            format="{time} {level} {message}",
            level="DEBUG",
            rotation="1 weeks",
        ),
    ]
)

if __name__ == "__main__":

    title = "EuroSat Classification"
    st.markdown(
        f"<h1 style='text-align: center; color: red;'> " f"{title} </h1>", unsafe_allow_html=True
    )

    ip = os.getenv("IP", None)
    port = os.getenv("PORT", None)

    uploaded_file = st.file_uploader("", type="jpg")
    if uploaded_file is not None:
        # To read file as bytes:
        logger.info("Load image")
        bytes_data = uploaded_file.getvalue()
        np_array = np.fromstring(bytes_data, np.uint8)
        image = cv2.imdecode(np_array, cv2.COLOR_BGR2RGB)

        logger.info(f"image.shape = {image.shape}")

        try:
            response = post(file=uploaded_file,
                            url=f"http://{ip}:{port}/api/v1/files/")

            label = response.json().get("predict")
            logger.info(response.json())

            fig = plt.figure()
            plt.imshow(image)
            plt.title(f"Predict class ~ {label}")
            plt.axis("off")
            st.pyplot(fig)

        except Exception as e:
            logger.error(e)

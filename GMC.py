# Growth MindSet Project (Sir Zia 1st Project),
# Created By Huzaifa Ghouri (419013), 
# I created Video to Gif Converter.

import streamlit as st
from moviepy.editor import VideoFileClip
from io import BytesIO
import imageio
import tempfile
import os

# Basic Theme Configuration
st.set_page_config(page_title="MP4 to GIF Converter", page_icon="🎬", layout="centered")
st.title("Growth Mindset Challenge")

# Custom CSS
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(135deg, #f0f2f5, #e1e4e8);
        background-size: 400% 400%;
        animation: gradientAnimation 15s ease infinite;
        color: #333;
        font-family: 'Roboto', sans-serif;
        line-height: 1.7;
    }
    @keyframes gradientAnimation {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap');
    .stApp {
        max-width: 800px;
        margin: 2rem auto;
        padding: 3rem;
        background-color: rgba(255, 255, 255, 0.95);
        border-radius: 15px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.15);
        transition: box-shadow 0.3s ease;
        animation: appContainerPulse 5s ease infinite alternate;
    }
    @keyframes appContainerPulse {
        0% { transform: scale(1); }
        100% { transform: scale(1.01); }
    }
    .stApp:hover {
        box-shadow: 0 12px 35px rgba(0, 0, 0, 0.2);
    }
    .stTitle, .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
        color: #2c3e50;
        font-weight: 700;
        margin-bottom: 1.5rem;
        text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.08);
        animation: titleAnimation 5s ease infinite alternate;
        font-size: 1.5rem;
    }
    @keyframes titleAnimation {
        0% { transform: translateY(0); }
        100% { transform: translateY(-5px); }
    }
    .stButton > button, .stDownloadButton > button {
        background: linear-gradient(to right, #4a90e2, #2e69a3);
        color: white;
        border: none;
        padding: 14px 30px;
        border-radius: 10px;
        cursor: pointer;
        transition: transform 0.2s ease, box-shadow 0.3s ease, background 0.3s ease;
        font-weight: 500;
        box-shadow: 0 5px 15px rgba(74, 144, 226, 0.4);
        animation: buttonPulse 2s ease infinite alternate;
    }
    @keyframes buttonPulse {
        0% { transform: scale(1); }
        100% { transform: scale(1.05); }
    }
    .stButton > button:hover, .stDownloadButton > button:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 20px rgba(74, 144, 226, 0.5);
        background: linear-gradient(to right, #357ebd, #235a8f);
    }
    .stFileUploader > div > div > div {
        border: 2px dashed #b3e5fc;
        padding: 30px;
        border-radius: 12px;
        background-color: #f5faff;
        margin-bottom: 2rem;
        transition: border-color 0.3s ease, box-shadow 0.3s ease;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
        animation: fileUploadShine 3s ease infinite alternate;
    }
    @keyframes fileUploadShine {
        0% { box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1); }
        100% { box-shadow: 0 6px 15px rgba(179, 229, 252, 0.5); }
    }
    .stFileUploader > div > div > div:hover {
        border-color: #4a90e2;
        box-shadow: 0 6px 15px rgba(74, 144, 226, 0.3);
    }
    .stSpinner > div > div {
        border-color: #4a90e2;
        border-width: 4px;
    }
    @keyframes spinnerRotate {
        100% { transform: rotate(360deg); }
    }
    .stError {
        background-color: #fff0f0;
        color: #d32f2f;
        padding: 20px;
        border-radius: 10px;
        margin-top: 2rem;
        box-shadow: 0 4px 10px rgba(211, 47, 47, 0.2);
        animation: errorShake 0.8s ease infinite alternate;
    }
    @keyframes errorShake {
        0% { transform: translateX(0); }
        25% { transform: translateX(-5px); }
        75% { transform: translateX(5px); }
        100% { transform: translateX(0); }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Main Section
st.title("🎬 MP4 to GIF Converter")
st.markdown("Convert your MP4 videos into captivating GIFs.")

uploaded_video = st.file_uploader("Upload MP4 file", type=["mp4"])
if uploaded_video:
    if st.button("Convert Video to GIF"):
        with st.spinner("Converting video..."):
            try:
                video_file = BytesIO(uploaded_video.read())
                with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as tmp_file:
                    tmp_file.write(video_file.getvalue())
                    temp_file_path = tmp_file.name

                video = VideoFileClip(temp_file_path)
                images = [frame for frame in video.iter_frames()]

                gif_buffer = BytesIO()
                imageio.mimsave(gif_buffer, images, format="GIF")

                st.download_button(
                    label="Download GIF",
                    data=gif_buffer.getvalue(),
                    file_name="converted.gif",
                    mime="image/gif",
                )
                gif_buffer.close()
                video.close()
                os.unlink(temp_file_path)

            except Exception as e:
                st.error(f"Error converting video: {e}")
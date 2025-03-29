import streamlit as st
from PIL import Image
import os
import moviepy.editor as moviepy
from model import fetch_model
from helper import mkdirs
# import requests


model_results_path = os.path.join('app_temp', 'results')
model_input_path = os.path.join('app_temp', 'inputs')
mkdirs([model_results_path, model_input_path])


model = fetch_model()

@st.fragment
def download_button_for_vid(path, key):
    data = open(path, "rb")
    st.download_button(
        label="📥 تنزيل الفيديو",
        data=data,
        file_name="result.mp4",
        mime="video/mp4",
        key = key
    )
    data.close()

@st.fragment
def download_button_for_img(path, name):
    data = open(path, "rb")
    st.download_button(
        label = "📥 تنزيل الصورة",
        data = data,
        file_name = name,
        mime = "image/jpg"
    )
    data.close()

def main():
    # Arabic RTL support and custom styling
    st.markdown("""
    <style>
        /* RTL Support for Arabic */
        body {z
            direction: rtl;
            text-align: right;
            font-family: 'Tajawal', sans-serif;
        }
        .element-container {
            direction: rtl;
        }
        /* Main background and text color */
        .main {
            background-color: #1a1a1a;
            color: #ffffff;
        }
        /* Sidebar background and text color */
        .sidebar .sidebar-content {
            background-color: #2d2d2d;
            direction: rtl;
            text-align: right;
        }
        /* Text input styling */
        .stTextInput textarea {
            color: #ffffff !important;
            background-color: #3d3d3d !important;
            text-align: right;
            direction: rtl;
        }
        /* Select box styling */
        .stSelectbox div[data-baseweb="select"] {
            color: white !important;
            background-color: #3d3d3d !important;
            text-align: right;
            direction: rtl;
        }
        .stSelectbox svg {
            fill: white !important;
        }
        .stSelectbox option {
            background-color: #2d2d2d !important;
            color: white !important;
            text-align: right;
        }
        /* Dropdown menu items */
        div[role="listbox"] div {
            background-color: #2d2d2d !important;
            color: white !important;
            text-align: right;
        }
        /* Button styling */
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            border-radius: 5px;
            padding: 10px 24px;
            font-size: 16px;
        }
        .stButton>button:hover {
            background-color: #45a049;
        }
        /* File uploader styling */
        .stFileUploader>div>div {
            background-color: #3d3d3d !important;
            color: white !important;
            border-radius: 5px;
            text-align: right;
        }
        /* Radio button styling */
        .stRadio>div {
            background-color: #3d3d3d !important;
            border-radius: 5px;
            padding: 10px;
            text-align: right;
            direction: rtl;
        }
        .stRadio>div>label {
            color: white !important;
        }
        /* Spinner styling */
        .stSpinner>div {
            color: white !important;
        }
        /* Import Arabic font */
        @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700&display=swap');
    </style>
    """, unsafe_allow_html=True)

    # Google Fonts for Arabic (Tajawal)
    st.markdown("""
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700&display=swap" rel="stylesheet">
    """, unsafe_allow_html=True)

    # Title and caption in Arabic
    st.title("🛣️ الكشف عن تشوهات الطرق")
    st.caption("🔍 اكتشف الحرائق والحوادث والأشجار المتساقطة وغيرها من التشوهات باستخدام تقنية الرؤية الحاسوبية المتقدمة")

    # Sidebar configuration in Arabic
    with st.sidebar:
        st.header("⚙️ الإعدادات")
        # detection_mode = st.selectbox(
        #     "وضع الكشف",
        #     ["قياسي", "دقة عالية", "كشف سريع"],
        #     index=0
        # )
        # st.divider()
        st.markdown("### إمكانيات الكشف")
        st.markdown("""
        - 🔥 كشف الحرائق
        - 💥 التعرف على الحوادث
        - 🌲 تحديد الأشجار المتساقطة
        - 🕳️ تحليل أضرار الطرق
        """)
        st.divider()
        st.markdown("تم التطوير بواسطة [RMG](https://www.bing.com/ck/a?!&&p=46d86158bd46de3e921bb063698e46d828fe1d56238389f5ae9196b2b800adc0JmltdHM9MTc0MDUyODAwMA&ptn=3&ver=2&hsh=4&fclid=35b4d946-977c-6272-19eb-cafe960063b1&psq=RMG&u=a1aHR0cHM6Ly93d3cucm1nLXNhLmNvbS9lbi8&ntb=1)")

    # Main content area
    main_container = st.container()

    with main_container:
        # Upload tabs in Arabic
        file_type = st.radio("اختر نوع المدخل:", ('صورة', 'فيديو'), horizontal=True)

        if file_type == 'صورة':
            with st.form("my-form", clear_on_submit=True):
                uploaded_images = st.file_uploader("اختر صورة...", type=["jpg", "png", "jpeg"], accept_multiple_files=True)
                st.form_submit_button("ابدأ...")

            if not isinstance(uploaded_images, list): uploaded_images = [uploaded_images]

            for i, img in enumerate(uploaded_images):
                
                col1, col2 = st.columns(2)

                with col1:
                    st.markdown("### الصورة الأصلية")
                    st.image(img)

                # Run object detection
                with st.spinner("🔍 جاري تحليل الصورة..."):
                    img = Image.open(img)
                    result = model(img)[0]
                    # inp_path = os.path.join(model_input_path, f"img.{img.name.split('.')[-1]}")
                    # with open(inp_path, "wb") as f:
                    #     f.write(img.getvalue())
                    # with open(inp_path, 'rb') as f:
                    #     files = {'file': f.read()}
                    # result = model(inp_path)[0]
                    # response = requests.post(
                    #     url = 'http://127.0.0.1:5000/process/image', 
                    #     files = files,
                    # )

                # Process results
                results_file_path = os.path.join(model_results_path, f"result_{i}.jpg")
                result.save(filename = results_file_path)
                # with open(results_file_path, 'wb') as im:
                #     im.write(response.content)

                with col2:
                    st.markdown("### النتيجة المعالجة")
                    st.image(results_file_path)

                    st.success("✅ اكتمل التحليل!")

                    # Download button
                    download_button_for_img(results_file_path, os.path.basename(results_file_path))

        elif file_type == 'فيديو':
            
            with st.form("my-form", clear_on_submit=True):
                uploaded_videos = st.file_uploader("رفع فيديو...", type=["mp4", "mov", 'avi'], accept_multiple_files=True)
                st.form_submit_button("ابدأ...")

            if not isinstance(uploaded_videos, list): uploaded_videos = [uploaded_videos]

            if uploaded_videos:
                for i, vid in enumerate(uploaded_videos, 1):

                    col1, col2 = st.columns(2)

                    with col1:
                        st.markdown("### الفيديو الأصلي")
                        st.video(vid)

                    # put the uploaded vid in the model input path
                    uploaded_videos_path = os.path.join(model_input_path, 'vid.mp4')
                    with open(uploaded_videos_path, mode='wb') as f:
                        f.write(vid.getvalue())
                    
                    with st.spinner("🔍 جاري معالجة الفيديو...", show_time=True):
                        # with open(uploaded_videos_path, 'rb') as f:
                        #     files = {'file': f.read()}
                        # response = requests.post(
                        #     url = 'http://127.0.0.1:5000/process/video', 
                        #     files = files
                        # )

                        model.predict(
                            uploaded_videos_path, project='app_temp', name='results', verbose=True, save=True, exist_ok=True
                        )

                        file_path = os.path.join(model_results_path, 'vid.avi')
                        # with open(file_path, 'wb') as f:
                        #     f.write(response.content)


                    st.success("✅ تمت معالجة الفيديو بنجاح!")

                    with st.spinner("🔄 جاري تحويل تنسيق الفيديو...", show_time=True):
                        processed_vid_path = os.path.join(model_results_path, f'vid_{i}.mp4')
                        clip = moviepy.VideoFileClip(file_path)
                        clip.write_videofile(processed_vid_path)

                    with col2:
                        st.markdown("### النتيجة المعالجة")
                        st.video(processed_vid_path)

                    download_button_for_vid(processed_vid_path, key = i)

if __name__ == "__main__":
    main()
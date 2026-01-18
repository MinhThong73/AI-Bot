import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load biến môi trường (chỉ dùng khi chạy local)
#load_dotenv()

# Cấu hình API key
genai.configure(api_key="AIzaSyD74DAMCjIDlqRm2hvsm0krWFC7xftBdCs")

# Cấu hình sinh văn bản
generation_config = {
    "temperature": 0.7,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 2048,
}

# System instruction
system_instruction = (
    "Bạn là một giáo sư khoa học, tự nhiên và xã hội. "
    "Nhiệm vụ của bạn là trả lời các câu hỏi về khoa học tự nhiên và xã hội. "
    "Nếu người dùng hỏi những vấn đề không liên quan, "
    "hãy khéo léo từ chối và nhắc rằng bạn chỉ chuyên về khoa học, tự nhiên và xã hội."
)

# Khởi tạo model
model = genai.GenerativeModel(
    model_name="gemini-2.5-flash",
    generation_config=generation_config,
    system_instruction=system_instruction
)

# ================= STREAMLIT UI =================
st.set_page_config(page_title="AI Khoa học", page_icon="🧠")
st.title("🧠 Trợ lý AI Khoa học")
st.write("Hỏi về **khoa học tự nhiên & xã hội** nhé!")

# Lưu lịch sử chat
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

# Hiển thị lịch sử
for msg in st.session_state.chat.history:
    with st.chat_message("assistant" if msg.role == "model" else "user"):
        st.write(msg.parts[0].text)

# Ô nhập chat
prompt = st.chat_input("Nhập câu hỏi của bạn...")

if prompt:
    with st.chat_message("user"):
        st.write(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Đang suy nghĩ..."):
            try:
                response = st.session_state.chat.send_message(prompt)
                st.write(response.text)
            except Exception as e:
                st.error(f"Có lỗi xảy ra: {e}")




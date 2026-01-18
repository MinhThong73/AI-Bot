import google.generativeai as genai
import os
from dotenv import load_dotenv
# 1. Cấu hình API Key của bạn
load_dotenv()

genai.configure(api_key=os.getenv("GENAI_API_KEY"))

# 2. Thiết lập cấu hình mô hình
generation_config = {
    "temperature": 0.7, # Độ sáng tạo (0.7 là vừa phải cho nấu ăn)
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 2048,
}

# 3. Định nghĩa "Tính cách" cho AI (System Instruction)
# Đây là phần quan trọng nhất để AI chỉ trả lời về ẩm thực
system_instruction = (
    "Bạn là một giáo sư khoa học, tự nhiên và xã hội. "
    "Nhiệm vụ của bạn là trả lời các câu hỏi về khoa học tự nhiên và xã hội "
    "Nếu người dùng hỏi những vấn đề không liên quan đến khoa học, tự nhiên và xã hội"
    "hãy khéo léo từ chối và nhắc người dùng rằng bạn chỉ chuyên về khoa học, tự nhiên và xã hội."
)

model = genai.GenerativeModel(
    model_name="gemini-2.5-flash", # Dùng bản flash cho tốc độ nhanh
    generation_config=generation_config,
    system_instruction=system_instruction
)

# 4. Bắt đầu chương trình hỏi đáp
def chat_ve_khoa_hoc():
    chat_session = model.start_chat(history=[])
    print("Chào bạn! Tôi là trợ lý AI chuyên về khoa học xã hội.")
    print("Bạn có thể hỏi tôi về các vấn đề khoa học tự nhiên và xã hội nhé!")
    print("(Gõ 'thoát' để dừng)\n")

    while True:
        user_input = input("Bạn: ")
        
        if user_input.lower() in ["thoát", "exit", "quit"]:
            print("AI Đầu bếp: Tạm biệt! Chúc bạn có những buổi học thú vị.")
            break

        try:
            # Gửi câu hỏi đến AI
            response = chat_session.send_message(user_input)
            
            print(f"\nAI Đầu bếp: \n{response.text}\n")
            print("-" * 30)
            
        except Exception as e:
            print(f"Có lỗi xảy ra: {e}")

if __name__ == "__main__":
    chat_ve_khoa_hoc()
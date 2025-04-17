import google.generativeai as genai
from google.generativeai.types import HarmCategory, HarmBlockThreshold

genai.configure(api_key="YOUR_API_KEY")  # 🔐 Don’t keep real keys in public code

model = genai.GenerativeModel(
    model_name="models/gemini-1.5-pro-latest",
    safety_settings={
        HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
    }
)

def generate_ai_response(crime_type, user_input):
    prompt = f"""
You are an AI Cyber Law Assistant.

A user is reporting a case of {crime_type}. Here is their description:
\"{user_input}\"

Please provide a professional response in this exact format:

1. **Applicable Indian Laws** (IPC + IT Act):
   - IPC Section X: [Title] – [Short explanation]
   - IT Act Section X: [Title] – [Short explanation]

2. **Recommended Actions (Step-by-Step)**:
   1. Collect [evidence type] – [why it's important]
   2. Report to [agency] – [steps to file]
   3. Notify bank / platform – [action]

3. **Important Tips**:
   - [Precaution or caution advice]

Keep the language simple and legal-professional. Don't sound too emotional. Format everything cleanly with markdown-style bullet points.
"""
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"⚠️ Gemini Error: {str(e)}"

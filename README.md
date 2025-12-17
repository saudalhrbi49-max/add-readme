import streamlit as st
from llm_backend import process_query

# إعدادات الصفحة
st.set_page_config(page_title="Baqit Hub", page_icon="icon.png", layout="wide")

# تحميل صور الخلفية والشعار (اختياري)
st.markdown(
    """
    <style>
    body {
        background-color: #f5f5f0;
        font-family: 'Cairo', sans-serif;
    }
    .stChatMessage {
        direction: rtl;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# اختيار اللغة
lang = st.sidebar.selectbox("Language / اللغة", ["English", "العربية"])

# عنوان التطبيق
st.image("logo.png", width=120)
st.title("🇸🇦 Baqit Hub – منصة تعليمية ذكية")

# إدارة المحادثة
if "messages" not in st.session_state:
    st.session_state.messages = []

# عرض المحادثة السابقة
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# إدخال المستخدم
if prompt := st.chat_input("اكتب سؤالك هنا..." if lang == "العربية" else "Type your question here..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
import json
import subprocess

LLM_MODEL = "qwen2.5:14b"

# تحميل قاعدة البيانات
with open("resources.json", "r", encoding="utf-8") as f:
    RESOURCES = json.load(f)

def detect_query_language(query: str) -> str:
    if any("\u0600" <= ch <= "\u06FF" for ch in query):
        return "ar"
    return "en"

def ask_llm_intent(query: str):
    """استدعاء نموذج Ollama لتصنيف الاستعلام"""
    result = subprocess.run(
        ["ollama", "run", LLM_MODEL, query],
        capture_output=True,
        text=True
    )
    return result.stdout.strip()

def extract_resource_key(llm_response: str):
    """يبسط استخراج المفتاح من رد النموذج"""
    for res in RESOURCES:
        if res["title_en"].lower() in llm_response.lower() or res["title_ar"] in llm_response:
            return res
    return None

def build_response(resource, lang="en"):
    if not resource:
        return "❌ Resource not found. حاول صياغة السؤال بشكل أوضح." if lang == "ar" else "❌ Resource not found. Please rephrase your query."

    if lang == "ar":
        return f"""
### {resource['title_ar']}
{resource['description_ar']}

**الخطوات:**
{resource['steps_ar']}

**المتطلبات:**
{resource['requirements_ar']}

[رابط رسمي]({resource['official_link']})
"""
    else:
        return f"""
### {resource['title_en']}
{resource['description_en']}

**Steps:**
{resource['steps_en']}

**Requirements:**
{resource['requirements_en']}

[Official Link]({resource['official_link']})
"""

def process_query(query: str, lang: str):
    llm_response = ask_llm_intent(query)
    resource = extract_resource_key(llm_response)
    return build_response(resource, "ar" if lang == "العربية" else "en")
[
  {
    "platform": "Qiyas",
    "category": "Testing",
    "title_ar": "التحضير لاختبار القدرات",
    "title_en": "Qiyas Exam Preparation",
    "description_ar": "موارد لمساعدتك في التحضير لاختبار القدرات.",
    "description_en": "Resources to help you prepare for Qiyas exam.",
    "steps_ar": "١. سجل في موقع قياس\n٢. اختر نوع الاختبار\n٣. اطلع على المواد التدريبية",
    "steps_en": "1. Register on Qiyas website\n2. Select exam type\n3. Review training materials",
    "requirements_ar": "حساب في موقع قياس",
    "requirements_en": "Qiyas account",
    "official_link": "https://www.qiyas.sa"
  },
  {
    "platform": "Coursera",
    "category": "Courses",
    "title_ar": "كورس برمجة بايثون",
    "title_en": "Python Programming Course",
    "description_ar": "تعلم أساسيات لغة بايثون عبر كورس تفاعلي.",
    "description_en": "Learn Python basics through an interactive course.",
    "steps_ar": "١. سجل في كورسيرا\n٢. ابحث عن Python\n٣. ابدأ الكورس",
    "steps_en": "1. Sign up on Coursera\n2. Search for Python\n3. Start the course",
    "requirements_ar": "بريد إلكتروني فعال",
    "requirements_en": "Valid email address",
    "official_link": "https://www.coursera.org"
  }
]

    # معالجة الاستعلام عبر LLM
    response = process_query(prompt, lang)

    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)

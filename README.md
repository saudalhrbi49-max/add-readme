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

    # معالجة الاستعلام عبر LLM
    response = process_query(prompt, lang)

    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)

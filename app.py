import streamlit as st
from llm_backend import process_query

st.set_page_config(page_title="Hospital Services Navigator", layout="centered")

st.title("🏥 Hospital Services Navigator")
st.write("Ask about hospital services in Arabic or English")

if "messages" not in st.session_state:
    st.session_state.messages = []

user_input = st.text_input("Type your question here:")

if st.button("Send") and user_input:
    response = process_query(user_input)
    st.session_state.messages.append(("You", user_input))
    st.session_state.messages.append(("System", response))

for sender, message in st.session_state.messages:
    if sender == "You":
        st.markdown(f"**🧑 You:** {message}")
    else:
        st.markdown(f"**🤖 System:** {message}")

def process_query(query: str, lang: str):
    llm_response = ask_llm_intent(query)
    resource = extract_resource_key(llm_response)
    return build_response(resource, "ar" if lang == "العربية" else "en")

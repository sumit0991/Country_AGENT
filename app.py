import streamlit as st
from main import agent_loop

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Country Info AI Agent",
    page_icon="🌍",
    layout="centered"
)

# -----------------------------
# Title
# -----------------------------
st.title("🌍 Country Info AI Agent")
st.markdown(
    "Ask me anything about **countries**, including:\n"
    "- Capital\n"
    "- Currency\n"
    "- Population\n"
    "- Languages\n"
    "- Continent"
)

# -----------------------------
# Session State
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# -----------------------------
# Display Chat History
# -----------------------------
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# -----------------------------
# User Input
# -----------------------------
prompt = st.chat_input("Ask about any country...")

if prompt:

    # Show user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate response
    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            try:
                response = agent_loop(prompt)

            except Exception as e:
                response = f"Error: {e}"

            st.markdown(response)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )

# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:

    st.title("🌍 Country Agent")

    st.write("### Example Questions")

    st.write("""
- Nepal
- India
- Capital of Japan
- Population of China
- Currency of USA
- Languages of Canada
- Tell me about Germany
""")

    st.divider()

    if st.button("🗑 Clear Chat"):

        st.session_state.messages = []

        st.rerun()

    st.divider()

    st.write("Built with ❤️ using")

    st.write("- Python")
    st.write("- Streamlit")
    st.write("- OpenRouter API")
    st.write("- REST Countries API")
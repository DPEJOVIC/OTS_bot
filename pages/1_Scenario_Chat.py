import streamlit as st
from openai import OpenAI


st.set_page_config(
    page_title="Chat",
    page_icon="👋",
)


st.title("Scenario Chat")


# Set up  system prompt
if "system_prompt" not in st.session_state:
    st.session_state["system_prompt"] = ""


# Set up OpenAI API client
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])


# Select GPT model
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"


# Add reload counter
if "counter" not in st.session_state:
    st.session_state.counter = 0
st.session_state.counter += 1


# Initialise chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


# Initialise response counter
if "response_counter" not in st.session_state:
    st.session_state.response_counter = 0


# Write chat history
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


if not st.session_state["system_prompt"]:
    st.write("Please select a scenario from the Home page.")
    st.stop()


# Chat logic
if prompt := st.chat_input("Ask the supervisor questions", disabled = st.session_state.response_counter >= 5):
    st.session_state.chat_history.append({"role": "user", "content": prompt})

    st.write(st.session_state["response_counter"])

    if st.session_state.response_counter < 5:
    
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            messages_with_system_prompt = [{"role": "system", "content": st.session_state["system_prompt"]}] + [
                {"role": m["role"], "content": m["content"]}
            for m in st.session_state.chat_history
            ]

            stream = client.chat.completions.create(
                model = st.session_state["openai_model"],
                messages = messages_with_system_prompt,
                stream = True,
            )
            response = st.write_stream(stream)

        st.session_state.response_counter += 1
        st.session_state.chat_history.append({"role": "assistant", "content": response})
    
    else:
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            message_with_system_prompt = [{"role": "system", "content": f"Just repeat these words as closely as possible, but fix the formatting. You may add paragraph breaks where logical: {st.session_state['cutoff']}"}]

            stream = client.chat.completions.create(
                    model = st.session_state["openai_model"],
                    messages = message_with_system_prompt,
                    stream = True,
            )
            response = st.write_stream(stream)
            
        st.session_state.chat_history.append({"role": "assistant", "content": response})


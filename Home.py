import streamlit as st
import json


st.title("Operation Training Simulator Chatbot")


def clearhistory(): 
    if "chat_history" not in st.session_state:
        st.session_state["chat_history"] = []
    st.session_state["chat_history"] = []

    # Initialise response counter
    if "response_counter" not in st.session_state:
        st.session_state.response_counter = 0
    st.session_state["response_counter"] = 0


# Allow the user to select a scenario.
scenario_selection = st.selectbox(
    "Please select the scenario you completed below.",
    ("Scenario 1", "Scenario 2", "Scenario 3", "Scenario 4", 
     "Research Scenario 1", "Research Scenario 2", "Research Scenario 3", "Research Scenario 4", 
     "Research Scenario 5", "Research Scenario 6", "Research Scenario 7"),
    index = None,
    on_change = clearhistory)


# Sets the system prompt based on the user's selection
def setprompt(context, s, cutoff):
    if "system_prompt" not in st.session_state:
        st.session_state["system_prompt"] = ""
    
    if "cutoff" not in st.session_state:
        st.session_state["cutoff"] = ""

    with open("scenarios.json", "r") as file:
        data = json.load(file)
        st.session_state["system_prompt"] = data[context] + "\n" + data[s]
        st.session_state["cutoff"] = data[cutoff]
    

# If statement for user selection
if scenario_selection == "Scenario 1":
    setprompt("context", "s1", "s1cutoff")
elif scenario_selection == "Scenario 2":
    setprompt("context", "s2", "s2cutoff")
elif scenario_selection == "Scenario 3":
    setprompt("context", "s3", "s3cutoff")
elif scenario_selection == "Scenario 4":
    setprompt("context", "s4", "s4cutoff")
elif scenario_selection == "Research Scenario 1":
    setprompt("rscontext", "rs1", "rs1cutoff")
elif scenario_selection == "Research Scenario 2":
    setprompt("rscontext", "rs2", "rs2cutoff")
elif scenario_selection == "Research Scenario 3":
    setprompt("rscontext", "rs3", "rs3cutoff")
elif scenario_selection == "Research Scenario 4":
    setprompt("rscontext", "rs4", "rs4cutoff")
elif scenario_selection == "Research Scenario 5":
    setprompt("rscontext", "rs5", "rs5cutoff")
elif scenario_selection == "Research Scenario 6":
    setprompt("rscontext", "rs6", "rs6cutoff")
elif scenario_selection == "Research Scenario 7":
    setprompt("rscontext", "rs7", "rs7cutoff")


# Prompt user to proceed to scenario
if scenario_selection:
    st.write("You've selected:", scenario_selection)
    st.write("Please proceed to the scenario chat window. ")
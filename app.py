import streamlit as st
from dotenv import load_dotenv
import os

from chatbot.prompts import get_interview_prompt
from chatbot.interviewer import Interviewer
from chatbot.evaluator import Evaluator

load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")

st.set_page_config(page_title="AI Interview Chatbot")
st.title("AI Interview Chatbot")


# ---------------- SESSION INIT ----------------
if "interviewer" not in st.session_state:
    st.session_state.interviewer = Interviewer(api_key)

if "evaluator" not in st.session_state:
    st.session_state.evaluator = Evaluator(api_key)

if "qa_pairs" not in st.session_state:
    st.session_state.qa_pairs = []

if "question" not in st.session_state:
    st.session_state.question = ""

if "step" not in st.session_state:
    st.session_state.step = "setup"


# ---------------- SETUP ----------------
if st.session_state.step == "setup":

    name = st.text_input("Enter Your Name")

    role = st.selectbox(
        "Select Job Role",
        [
            "Data Analyst",
            "Data Scientist",
            "AI Engineer",
            "AI Developer",
            "Software Engineer",
            "Machine Learning Engineer",
            "Full Stack Developer"
        ]
    )

    interview_type = st.selectbox(
        "Select Interview Type",
        ["HR Interview", "Technical Interview"]
    )

    if st.button("Start Interview"):

        prompt = get_interview_prompt(role, interview_type)
        st.session_state.interviewer.start_interview(prompt)

        first_q = st.session_state.interviewer.get_question()

        st.session_state.question = first_q
        st.session_state.role = role
        st.session_state.name = name
        st.session_state.interview_type = interview_type
        st.session_state.step = "interview"

        st.rerun()


# ---------------- INTERVIEW ----------------
elif st.session_state.step == "interview":

    # Progress
    st.progress(len(st.session_state.qa_pairs) / 5)
    st.write(f"Question {len(st.session_state.qa_pairs) + 1} / 5")

    # Conversation history
    for i, (q, a) in enumerate(st.session_state.qa_pairs):
        st.markdown(f"### Q{i+1}")
        st.write(q)
        st.markdown(f"**Your Answer:** {a}")
        st.divider()

    # Current question
    st.markdown("### 🤖 Interviewer")
    st.write(st.session_state.question)

    # Input
    answer = st.text_area("Your Answer", key="answer_box")

    # Submit
    if st.button("Submit Answer"):

        if answer.strip() == "":
            st.warning("Please write an answer before submitting.")
            st.stop()

        # Save Q&A
        st.session_state.qa_pairs.append(
            (st.session_state.question, answer)
        )

        # Next question
        with st.spinner("Generating next question..."):
            next_q = st.session_state.interviewer.get_question(answer)

        st.session_state.question = next_q

        # Stop after 5 questions
        if len(st.session_state.qa_pairs) >= 5:
            st.session_state.step = "result"

        st.rerun()


# ---------------- RESULT ----------------
elif st.session_state.step == "result":

    st.subheader("🎯 Interview Completed")

    result = st.session_state.evaluator.evaluate(
        st.session_state.role,
        st.session_state.qa_pairs
    )

    st.text_area("Evaluation Report", result, height=400)

    if st.button("Re-Interview"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()
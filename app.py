import streamlit as st
from agent import run_agent

st.set_page_config(page_title="Essay AI Agent", layout="centered")

st.title("🧠 Essay Writing AI Agent")
st.caption("Generate high-quality essays using AI")

st.markdown("---")

topic = st.text_input("Enter your topic")

if st.button("🚀 Generate Essay"):
    if topic.strip():
        with st.spinner("Thinking... Generating your essay step-by-step 🧠"):
            result = run_agent(topic)

            # Tabs for better UI
            tab1, tab2, tab3 = st.tabs(["📝 Draft", "🔍 Review", "✨ Final Essay"])

            with tab1:
                st.subheader("First Draft")
                st.markdown(result.get("draft", "No draft available"))

            with tab2:
                st.subheader("Review Feedback")
                st.markdown(result.get("review", "No review available"))

            with tab3:
                st.subheader("Final Essay")
                st.markdown(result.get("final_essay", "No final essay available"))

                # Download button
                st.download_button(
                    label="📥 Download Essay",
                    data=result.get("final_essay", ""),
                    file_name="essay.txt",
                    mime="text/plain"
                )

        st.markdown("---")
        st.caption("Built with LangGraph + Groq 🚀")
    else:
        st.warning("Please enter a topic")
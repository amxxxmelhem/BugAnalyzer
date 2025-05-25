import streamlit as st
from bug_analyzer import analyze_code

st.set_page_config(page_title="AI Bug Finder", layout="wide")

st.title("🔍Python Static Code Bug Analyzer")
st.markdown("Paste code in any programming language below and click **Analyze** to detect bugs and get suggestions.")

# Code input area
code_input = st.text_area("📝 Enter your code here:", height=300)

# File name input (optional, for display)
file_name = st.text_input("📄 File name:", value="example.py")

# Analyze button
if st.button("Analyze"):
    if not code_input.strip():
        st.warning("Please enter some code before clicking Analyze.")
    else:
        with st.spinner("Analyzing code..."):
            results = analyze_code(code_input, file_name)

        if not results:
            st.success("✅ No bugs detected! Your code looks clean.")
        else:
            st.markdown("### 🐞 Bug Report")
            for bug in results:
                st.markdown(f"""
                **File**: `{bug['file']}`  
                **Line Number**: `{bug['line']}`  
                **Issue Detected**: {bug['issue']}  
                **Variable Name**: `{bug['variable']}`  
                **Suggested Fix**: {bug['fix']}  
                **Confidence Score**: `{bug['confidence']:.2f}`  
                ---
                """)

import streamlit as st
import pandas as pd
import gzip

st.title("FASTQ Read Counter")

st.markdown("""
Upload one or more compressed FASTQ files (`.fastq.gz`).  
The app will count how many reads are in each file.
""")

uploaded_files = st.file_uploader("Upload .fastq.gz files", type="gz", accept_multiple_files=True)

if uploaded_files:
    results = []

    for uploaded_file in uploaded_files:
        with gzip.open(uploaded_file, "rt") as f:
            num_lines = sum(1 for _ in f)
        read_count = num_lines // 4  # Each read has 4 lines
        results.append((uploaded_file.name, read_count))

    df = pd.DataFrame(results, columns=["sample", "read_count"])
    st.dataframe(df)

    st.download_button(
        label="Download Results as CSV",
        data=df.to_csv(index=False),
        file_name="read_counts.csv",
        mime="text/csv"
    )


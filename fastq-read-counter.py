import streamlit as st
import subprocess
import os
import pandas as pd

st.title("FASTQ Read Counter")
st.markdown("This app counts reads in compressed FASTQ files from a selected directory.")

# File input
fastq_dir = st.text_input("Enter the path to your FASTQ directory:", "/home/betre/illumina_paired/data/trimmed")

if st.button("Count Reads"):
    if not os.path.isdir(fastq_dir):
        st.error("Directory does not exist.")
    else:
        output_file = "read_counts.csv"
        with open(output_file, "w") as f:
            f.write("sample,read_count\n")

        # List fastq.gz files
        fastq_files = [f for f in os.listdir(fastq_dir) if f.endswith(".fastq.gz")]
        results = []

        progress = st.progress(0)
        for i, fastq_file in enumerate(fastq_files):
            full_path = os.path.join(fastq_dir, fastq_file)
            cmd = f"zcat '{full_path}' | wc -l"
            try:
                wc_output = subprocess.check_output(cmd, shell=True, text=True)
                read_count = int(int(wc_output.strip()) / 4)
                results.append((fastq_file, read_count))
            except Exception as e:
                st.warning(f"Error processing {fastq_file}: {e}")
            progress.progress((i + 1) / len(fastq_files))

        # Save to CSV
        df = pd.DataFrame(results, columns=["sample", "read_count"])
        df.to_csv(output_file, index=False)
        st.success(f"Read counts saved to `{output_file}`")
        st.dataframe(df)
        st.download_button("Download CSV", df.to_csv(index=False), file_name="read_counts.csv", mime="text/csv")


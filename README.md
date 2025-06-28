# fastq-read-counter2
This project provides a simple and user-friendly tool for counting reads in .fastq.gz files.
It is especially useful for researchers and bioinformaticians who need to:

    Quickly assess sequencing data volume per sample

    Estimate read depth before upstream and downstream analysis

    Validate sample quality or completeness

You can either:

    Run it online with no installation, or

    Clone the repository and run it locally using Python and Streamlit.

    
Click to launch:
https://fastq-read-counter2-ywdzx7vykenizknsuti3kx.streamlit.app/


# Clone the repository
git clone https://github.com/Abaysew/fastq-read-counter2.git
You can download the results as a CSV

# Change into the project directory
cd fastq-read-counter2

# Install required Python packages
pip install -r requirements.txt

# Run the Streamlit app
streamlit run read_counter_app.py

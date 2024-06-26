import os
import sys
import signal
import subprocess

def clear_sessions_csv():
    sessions_file = "sessions.csv"
    if os.path.exists(sessions_file):
        with open(sessions_file, 'w'):
            pass
        print(f"\nCleared contents of {sessions_file}")
    else:
        print(f"{sessions_file} does not exist.")

def run_streamlit_app():
    subprocess.run(["streamlit", "run", "app.py"])

if __name__ == "__main__":
    clear_sessions_csv()
    run_streamlit_app()

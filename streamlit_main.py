import streamlit as st
import subprocess
import streamlit as st
import subprocess
import sys

# subprocess.run(["/home/appuser/venv/bin/python", "streamlit_valid_expansion.py"])

p = subprocess.Popen([f"{sys.executable} -m streamlit_valid_expansion.py"], shell=True)
# p.run()

import streamlit as st
import subprocess
import streamlit as st
import subprocess
import sys
subprocess.check_call([sys.executable, "-m", "pip", "install", "https://storage.googleapis.com/en_ud_model"
                                                               "/en_ud_model_sm-2.0.0.tar.gz"])
subprocess.run([f"{sys.executable}", "streamlit_valid_expansion.py"])
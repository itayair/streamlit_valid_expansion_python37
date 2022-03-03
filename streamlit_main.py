import streamlit as st
import subprocess
import streamlit as st
import subprocess
import sys
import pip
# import streamlit_valid_expansion
# subprocess.check_call([sys.executable, "-m", "pip", "install", "https://storage.googleapis.com/en_ud_model"
#                                                                "/en_ud_model_sm-2.0.0.tar.gz"])
# subprocess.run([f"{sys.executable}", "streamlit_valid_expansion.py"])
#
#
#
# def install(package):
#     if hasattr(pip, 'main'):
#         pip.main(['install', package])
#     else:
#         pip._internal.main(['install', package])
#
# # Example
# if __name__ == '__main__':
#     streamlit_valid_expansion.main()
    # install("https://storage.googleapis.com/en_ud_model/en_ud_model_sm-2.0.0.tar.gz")

import sys
from streamlit import cli as stcli

if __name__ == '__main__':
    sys.argv = ["streamlit", "run", "streamlit_valid_expansion.py"]
    sys.exit(stcli.main())
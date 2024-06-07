import streamlit as st

from client_timezone import client_timezone

# from __init__ import client_timezone
from datetime import datetime

timezone = client_timezone(key="client-timezone")
st.write(timezone)
st.write(format(datetime.now(tz=timezone)))

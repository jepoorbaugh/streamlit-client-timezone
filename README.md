# Streamlit Client Timezone
Streamlit custom component to get the client's timezone as a tzinfo object. 

## Download
```bash
pip install streamlit-client-timezone==0.1.2
```
## Usage
```python
import streamlit as st
from datetime import datetime

from client_timezone import client_timezone

timezone = client_timezone(key="client-timezone")

time_loaded = datetime.now(tz=timezone)
```

# Streamlit Client Timezone
Streamlit custom component to get the client's timezone as a tzinfo object. 

## Usage
```python
timezone = client_timezone(key="client-timezone")

time_loaded = datetime.now(tz=timezone)
```
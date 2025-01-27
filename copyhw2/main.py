import pandas as pd
import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts")
response.raise_for_status()
data = response.json()
df = pd.DataFrame(data)
print(df.head())





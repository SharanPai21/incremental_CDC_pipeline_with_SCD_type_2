import os
from dotenv import load_dotenv
import requests

load_dotenv()

host = os.getenv("DATABRICKS_HOST")
token = os.getenv("DATABRICKS_TOKEN")

if not host or not token:
    print("missing token or host")
    raise SystemExit(1)

url = f"{host.rstrip('/')}/api/2.2/jobs/list"

headers = {
    "Authorization": f"Bearer {token}"
}

response = requests.get(url, headers=headers, timeout = 30)

print("Status code:", response.status_code)
print("Response JSON:", response.json())
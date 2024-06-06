import os

print(os.environ)
bearer_token = os.environ.get("WT_API_TOKEN")
print("Bearer Token:", bearer_token)
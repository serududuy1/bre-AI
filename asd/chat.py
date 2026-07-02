from openai import OpenAI
import requests

client = OpenAI(
    base_url="http://127.0.0.1:1234/v1",
    api_key="lm-studio"
)

# Ambil JSON dari LibreHardwareMonitor
data = requests.get("http://localhost:8085/data.json").json()


def walk(node):
    yield node
    for child in node.get("Children", []):
        yield from walk(child)


def get_temperature(keyword):
    keyword = keyword.lower()

    for node in walk(data):
        if node.get("Type") != "Temperature":
            continue

        text = node.get("Text", "").lower()

        if keyword in text:
            return node.get("Value")

    return None

gpu_temp = get_temperature("gpu core")
cpu_temp = get_temperature("core (tctl/tdie)")

status = {
    "gpu": {
        "name": "GTX 1070",
        "temperature": 44,
        "hotspot": 56,
        "usage": 4,
        "fan": 32
    },
    "cpu": {
        "name": "Ryzen 5 5600G",
        "temperature": 53
    }
}


prompt = f"""
Status PC:

{status}

Jawab seperti teman.
"""

response = client.chat.completions.create(
    model="google/gemma-3-12b",
    messages=[
        {
            "role": "system",
            "content": prompt
        },
        {
            "role": "user",
            "content": "bre suhu gpu"
        }
    ]
)

print(response.choices[0].message.content)
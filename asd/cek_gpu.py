import requests

data = requests.get("http://localhost:8085/data.json").json()

def walk(node):
    yield node
    for child in node.get("Children", []):
        yield from walk(child)

for node in walk(data):
    if node.get("Type") == "Temperature":
        print(node.get("Text"))
import requests

URL = "http://localhost:8085/data.json"

data = requests.get(URL).json()


def find_gpu_temp(node):
    if isinstance(node, dict):

        if node.get("Type") == "Temperature":

            sensor = node.get("SensorId", "")

            if "gpu" in sensor.lower():
                return node["Value"]

        for child in node.get("Children", []):
            result = find_gpu_temp(child)
            if result:
                return result

    return None


temp = find_gpu_temp(data)

print(temp)
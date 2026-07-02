from app.sensors import get_sensor
from app.router import detect_intent
from app.llm import ask_ai

from app.tools import gpu,cpu,ram,system,chat

print("BREMON ONLINE 😎")

while True:

    user=input("BRE > ")

    if user=="exit":
        break

    sensor=get_sensor()

    intent=detect_intent(user)

    if intent=="gpu":

        prompt=gpu.build(sensor)

    elif intent=="cpu":

        prompt=cpu.build(sensor)

    elif intent=="ram":

        prompt=ram.build(sensor)

    elif intent=="system":

        prompt=system.build(sensor)

    else:

        prompt=chat.build(sensor,user)

    print()

    print(ask_ai(prompt))

    print()
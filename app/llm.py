from openai import OpenAI

from app.config import *

from app.prompts import SYSTEM_PROMPT

client = OpenAI(
    base_url=LM_STUDIO_URL,
    api_key=API_KEY
)


def ask_ai(prompt):

    response = client.chat.completions.create(

        model=MODEL,

        temperature=0.7,

        messages=[

            {
                "role":"system",
                "content":SYSTEM_PROMPT
            },

            {
                "role":"user",
                "content":prompt
            }

        ]

    )

    return response.choices[0].message.content
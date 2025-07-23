import os
from together import Together
from dotenv import load_dotenv

load_dotenv()

client = Together()

class WaterIntakeAgent:

    def __init__(self):
        self.history=[]

    def analayze_intake(self, intake_ml):
        prompt = f"""
        you are a hydration assistant. The user has consumed {intake_ml} ml of water today.
        provide a hydration status and suggest if they need to drink more water.
        """
        response = client.chat.completions.create(
            model="Qwen/Qwen3-235B-A22B-Instruct-2507-tput",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.choices[0].message.content

if __name__=='__main__':
    agent = WaterIntakeAgent()
    intake = 1500
    feedback = agent.analayze_intake(intake)
    print(f"Hydration Analysis: {feedback}")

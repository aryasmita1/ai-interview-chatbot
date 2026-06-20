from openai import OpenAI

class Interviewer:
    def __init__(self, api_key):
        self.client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=api_key
        )
        self.messages = []

    def start_interview(self, prompt):
        self.messages = [{"role": "system", "content": prompt}]

    def get_question(self, user_answer=None):
        if user_answer:
            self.messages.append({"role": "user", "content": user_answer})

        response = self.client.chat.completions.create(
            model="qwen/qwen-2.5-7b-instruct",
            messages=self.messages,
            max_tokens=200
        )

        msg = response.choices[0].message.content
        self.messages.append({"role": "assistant", "content": msg})
        return msg
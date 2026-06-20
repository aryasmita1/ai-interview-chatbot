from openai import OpenAI

class Evaluator:
    def __init__(self, api_key):
        self.client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=api_key
        )

    def evaluate(self, role, qa_pairs):

        # Format Q&A cleanly
        text = "\n".join(
            [f"Q{i+1}: {q}\nA{i+1}: {a}\n" for i, (q, a) in enumerate(qa_pairs)]
        )

        prompt = f"""
You are a strict professional interview evaluator.

Role: {role}

IMPORTANT RULES:
- Reply ONLY in English
- Do NOT use any other language
- Do NOT break format
- Do NOT add extra commentary

Evaluate the candidate strictly and return in this format:

Technical Skills: X/10
Communication Skills: X/10
Problem Solving: X/10
Overall Score: X/10

Feedback:
- Strengths:
- Weaknesses:
- Suggestions for improvement:

Interview Data:
{text}
"""

        response = self.client.chat.completions.create(
            model="qwen/qwen-2.5-7b-instruct",
            messages=[
                {"role": "system", "content": "You are a strict interview evaluator."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=600
        )

        return response.choices[0].message.content
import os
import re

from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client()


def generate_prompt():
    return """write the python code to calculate
a loan payment with the following inputs: interest,
term, present value. return code only wrapped in a Markdown
code block (triple backticks). Do not add any extra text or
explanation outside the code block."""


response = client.models.generate_content(
    model="gemini-1.5-flash", contents=generate_prompt()
)

match = re.search(r"```(?:python)?\s*([\w\W]*?)```", response.text, re.DOTALL)
code_content = match.group(1).strip()
print("---Extracted code ---")
print(code_content)

output_path = os.path.join(os.getcwd(), "loan_payment.py")
with open(output_path, "w") as f:
    f.write(code_content)

print(f"Written to: {output_path}")
print(f"File size: {os.path.getsize(output_path)} bytes")

from groq import Groq

# -------------------------------
# CONFIG
# -------------------------------
API_KEY = "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"
MODEL_NAME = "llama-3.1-8b-instant"

client = Groq(api_key=API_KEY)

# -------------------------------
# 1. USER REQUIREMENT
# -------------------------------
requirement = input("Enter your requirement: ")

# -------------------------------
# 2. CODE GENERATION PROMPT
# -------------------------------
generate_prompt = f"""
You are a senior software engineer.

Generate clean, correct, executable Python code.

Rules:
- Only output code
- No explanation
- No markdown
- Code must be runnable

Requirement:
{requirement}
"""

gen_response = client.chat.completions.create(
    model=MODEL_NAME,
    messages=[{"role": "user", "content": generate_prompt}],
    temperature=0.2
)

generated_code = gen_response.choices[0].message.content.strip()

print("\n========== GENERATED CODE ==========\n")
print(generated_code)

# Save generated code
with open("generated_code.py", "w", encoding="utf-8") as f:
    f.write(generated_code)

# -------------------------------
# 3. CODE REVIEW PROMPT
# -------------------------------
review_prompt = f"""
You are a senior software architect performing a professional code review.

Review the following Python code and respond in this EXACT format:

Rating: <number out of 10>
Strengths:
- point 1
- point 2
Weaknesses:
- point 1
- point 2
Overall Verdict: <1 line summary>

Code:
{generated_code}
"""

review_response = client.chat.completions.create(
    model=MODEL_NAME,
    messages=[{"role": "user", "content": review_prompt}],
    temperature=0.1
)

review = review_response.choices[0].message.content.strip()

print("\n========== CODE REVIEW ==========\n")
print(review)

# Save review
with open("code_review.txt", "w", encoding="utf-8") as f:
    f.write(review)

print("\n Code saved as generated_code.py")
print(" Review saved as code_review.txt")

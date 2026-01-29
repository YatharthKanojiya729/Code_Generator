from groq import Groq
from github import Github
import re

# -------------------------------
# CONFIG
# -------------------------------
GROQ_API_KEY = "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"
GITHUB_TOKEN = "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"
GITHUB_REPO = "YatharthKanojiya729/Code_Generator" 
MODEL_NAME = "llama-3.1-8b-instant"

client = Groq(api_key=GROQ_API_KEY)

# -------------------------------
# 1. USER REQUIREMENT
# -------------------------------
requirement = input("Enter your requirement: ")

# -------------------------------
# 2. CODE GENERATION
# -------------------------------
generate_prompt = f"""
You are a senior software engineer.
Generate clean, correct, executable Python code.

Rules:
- Only output code
- No explanation
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

with open("generated_code.py", "w", encoding="utf-8") as f:
    f.write(generated_code)

print("\n✅ Code generated and saved.")

# -------------------------------
# 3. CODE REVIEW + RATING
# -------------------------------
review_prompt = f"""
You are a senior software architect.

Review the following Python code.

Return ONLY in this format:

Rating: <number>
Vulnerabilities:
- item
Fixes:
- item
Verdict: <APPROVED or NEEDS IMPROVEMENT>

Code:
{generated_code}
"""

review_response = client.chat.completions.create(
    model=MODEL_NAME,
    messages=[{"role": "user", "content": review_prompt}],
    temperature=0
)

review_text = review_response.choices[0].message.content.strip()

print("\n========== CODE REVIEW ==========\n")
print(review_text)

# -------------------------------
# 4. EXTRACT RATING
# -------------------------------
rating_match = re.search(r"Rating:\s*(\d+)", review_text)
if not rating_match:
    print("❌ Rating not found. Stopping.")
    exit()

rating = int(rating_match.group(1))
print(f"\n⭐ Final Rating: {rating}/10")

# -------------------------------
# 5. GITHUB AUTOMATION
# -------------------------------
if rating >= 7:
    print("\n🚀 Code approved. Uploading to GitHub...")

    g = Github(GITHUB_TOKEN)
    repo = g.get_repo(GITHUB_REPO)

    try:
        repo.create_file(
            path="generated_code.py",
            message="Auto-generated code approved by AI",
            content=generated_code,
            branch="main"
        )
        print("✅ Code pushed to GitHub successfully!")

    except Exception as e:
        print("⚠️ File already exists. Updating file...")

        file = repo.get_contents("generated_code.py", ref="main")
        repo.update_file(
            path=file.path,
            message="Updated auto-generated code",
            content=generated_code,
            sha=file.sha,
            branch="main"
        )
        print("✅ Code updated on GitHub!")

else:
    print("\n❌ Code not uploaded due to low rating.")
    print("Please fix vulnerabilities before deployment.")

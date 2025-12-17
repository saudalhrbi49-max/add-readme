def analyze_resume(resume_text):
    """
    Simulated LLM Resume Analyzer
    """
    skills = [
        "Communication",
        "Problem Solving",
        "Teamwork",
        "Python",
        "Critical Thinking"
    ]

    feedback = (
        "Resume Analysis Result:\n"
        "- Overall Quality: Good\n"
        "- Strengths: Clear structure, relevant skills\n"
        "- Improvements: Add more project details\n"
    )

    return skills, feedback


def main():
    print("=== AI Resume Analyzer ===\n")

    resume_text = input("Paste your resume text here:\n")

    skills, feedback = analyze_resume(resume_text)

    print("\n--- Extracted Skills ---")
    for skill in skills:
        print(f"- {skill}")

    print("\n--- Feedback ---")
    print(feedback)


if __name__ == "__main__":
    main()

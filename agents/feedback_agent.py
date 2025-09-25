from utils.groq_client import ask_groq

def analyze_solution(problem_desc, user_code):
    """Provide comprehensive solution analysis"""
    prompt = f"""
    As an experienced coding coach, analyze this solution:

    PROBLEM: {problem_desc}
    
    USER'S SOLUTION:
    ```python
    {user_code}
    ```
    
    Please provide:
    1. **Correctness Assessment**: Does the solution work? If not, what's wrong?
    2. **Time Complexity**: Big O analysis
    3. **Space Complexity**: Memory usage analysis
    4. **Code Quality**: Readability, style, best practices
    5. **Edge Cases**: What edge cases are handled/missed?
    6. **Improvement Suggestions**: Specific, actionable improvements
    
    Be constructive and educational. Focus on learning.
    """
    return ask_groq(prompt)

def provide_detailed_feedback(problem_desc, user_code, test_cases_passed):
    """Provide feedback with test case context"""
    prompt = f"""
    Problem: {problem_desc}
    
    User Code:
    {user_code}
    
    Test Cases Passed: {test_cases_passed}
    
    Analyze the solution and provide targeted feedback. Focus on:
    - Why some test cases might be failing
    - Efficiency improvements
    - Code structure and readability
    - Best practices for this problem type
    """
    return ask_groq(prompt)
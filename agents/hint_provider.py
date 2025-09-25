from utils.groq_client import ask_groq

def provide_hint(problem_desc, user_code):
    """Provide adaptive hints based on user's current attempt"""
    prompt = f"""
    Problem: {problem_desc}
    
    User's current attempt:
    {user_code}
    
    Provide a helpful hint that:
    1. Addresses the specific approach the user is taking
    2. Gives a nudge in the right direction without giving away the solution
    3. Points out any obvious logical errors
    4. Suggests the next step they should consider
    
    Keep it concise and actionable. Maximum 2-3 sentences.
    """
    return ask_groq(prompt)

def provide_approach_hint(problem_desc):
    """Provide high-level approach hint without seeing user code"""
    prompt = f"""
    For the problem: {problem_desc}
    
    Provide a high-level approach hint about:
    - What data structures might be useful
    - What algorithm pattern applies
    - Key insight needed
    
    Don't give away the solution, just point in the right direction.
    """
    return ask_groq(prompt)
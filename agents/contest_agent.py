from agents.problem_recommender import recommend_problem
from datetime import datetime

def generate_contest(progress_data, num_problems=3):
    """Generate a contest with recommended problems"""
    contest = []
    for _ in range(num_problems):
        problem = recommend_problem(progress_data)
        contest.append({
            "problem": problem,
            "time_assigned": str(datetime.now()),
            "solved": False
        })
    return contest

def update_contest(contest_data, problem_index, solved=True):
    """Update contest problem status"""
    if 0 <= problem_index < len(contest_data):
        contest_data[problem_index]["solved"] = solved
    return contest_data

def score_contest(contest_data):
    """Calculate contest score with percentage"""
    total = len(contest_data)
    if total == 0:
        return 0
    solved = sum(1 for p in contest_data if p["solved"])
    percentage = (solved / total) * 100
    return percentage
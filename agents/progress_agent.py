from datetime import datetime

def update_progress(progress_data, solved=True, topic=None):
    """Update user progress with better topic tracking"""
    if not topic:
        # Use current topic if available, otherwise default
        topic = progress_data.get("current_topic", "general")
    
    if solved:
        # Add to solved problems with timestamp and topic
        solved_entry = {
            "topic": topic,
            "timestamp": str(datetime.now()),
            "problem": progress_data.get("current_problem", "Unknown")
        }
        progress_data["solved"].append(solved_entry)
        progress_data["streak"] += 1
        
        # Remove from weak topics if solved successfully
        if topic in progress_data["weak_topics"]:
            progress_data["weak_topics"].remove(topic)
    else:
        # Add to failed problems
        failed_entry = {
            "topic": topic,
            "timestamp": str(datetime.now()),
            "problem": progress_data.get("current_problem", "Unknown")
        }
        progress_data["failed"].append(failed_entry)
        progress_data["streak"] = 0
        
        # Add to weak topics if not already there
        if topic not in progress_data["weak_topics"]:
            progress_data["weak_topics"].append(topic)
    
    return progress_data

def calculate_success_rate(progress_data):
    """Calculate success rate percentage"""
    total_attempts = len(progress_data["solved"]) + len(progress_data["failed"])
    if total_attempts == 0:
        return 0
    return (len(progress_data["solved"]) / total_attempts) * 100

def get_topic_stats(progress_data, topic):
    """Get statistics for a specific topic"""
    topic_solved = len([p for p in progress_data["solved"] if p.get("topic") == topic])
    topic_failed = len([p for p in progress_data["failed"] if p.get("topic") == topic])
    total_topic = topic_solved + topic_failed
    
    return {
        "solved": topic_solved,
        "failed": topic_failed,
        "total": total_topic,
        "success_rate": (topic_solved / total_topic * 100) if total_topic > 0 else 0
    }
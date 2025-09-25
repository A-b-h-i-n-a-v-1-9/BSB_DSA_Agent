import streamlit as st
from utils.storage import init_storage, load_data, save_data
from agents.problem_recommender import recommend_problem, recommend_next_problems
from agents.hint_provider import provide_hint
from agents.feedback_agent import analyze_solution
from agents.progress_agent import update_progress
from agents.contest_agent import generate_contest, update_contest, score_contest
import random

# --- Init storage ---
init_storage()
data = load_data()

# --- Page Configuration ---
st.set_page_config(
    page_title="DSA Coach AI-Agent", 
    layout="wide",
    page_icon=""
)

# --- Custom CSS for better styling ---
st.markdown("""
<style>
    .main-header {
        font-size: 3rem !important;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .section-header {
        border-bottom: 2px solid #1f77b4;
        padding-bottom: 0.5rem;
        margin-top: 2rem;
        margin-bottom: 1rem;
        color: #1f77b4;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 10px;
        border-left: 4px solid #1f77b4;
        margin-bottom: 1rem;
    }
    .success-box {
        background-color: #d4edda;
        border: 1px solid #c3e6cb;
        border-radius: 5px;
        padding: 1rem;
        margin: 1rem 0;
    }
    .info-box {
        background-color: #d1ecf1;
        border: 1px solid #bee5eb;
        border-radius: 5px;
        padding: 1rem;
        margin: 1rem 0;
    }
    .problem-card {
        background-color: #fff;
        border: 1px solid #ddd;
        border-radius: 10px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
</style>
""", unsafe_allow_html=True)

# --- Main Title ---
st.markdown('<div class="main-header">DSA Coach AI-Agent</div>', unsafe_allow_html=True)

# --- Sidebar for Navigation ---
st.sidebar.title("🎯 Navigation")
section = st.sidebar.radio("Go to:", [
    "Dashboard", 
    "Problem Recommendations Dashboard", 
    "Submit Solution", 
    "Mini Contest",
    "Progress Analytics"
])

# --- Motivational Nudge ---
st.sidebar.markdown("---")
st.sidebar.subheader("💬 Coach's Corner")
MOTIVATIONS = [
    "🔥 Keep going, you're on a roll!",
    "💡 Focus on your weak topics to level up faster!",
    "⚡ Almost there! One more problem and streak continues!",
    "🏆 You're nailing it! Let's crush the next one!",
    "🌟 Consistency is key! Small steps lead to big results!"
]
st.sidebar.info(random.choice(MOTIVATIONS))

# --- Dashboard Section ---
if section == "Dashboard":
    st.markdown('<div class="section-header">📊 Learning Dashboard</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("Problems Solved", len(data["solved"]), delta=f"+{random.randint(1,5)} this week")
        st.markdown('</div>', unsafe_allow_html=True)
        
    with col2:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("Current Streak", data["streak"], delta="🔥" if data["streak"] > 5 else "⚡")
        st.markdown('</div>', unsafe_allow_html=True)
        
    with col3:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("Success Rate", 
                 f"{(len(data['solved']) / (len(data['solved']) + len(data['failed'])) * 100):.1f}%" 
                 if (len(data['solved']) + len(data['failed'])) > 0 else "0%")
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Weak topics and current focus
    col4, col5 = st.columns(2)
    
    with col4:
        st.subheader("🎯 Areas to Improve")
        if data["weak_topics"]:
            for topic in data["weak_topics"][:3]:  # Show top 3 weak topics
                st.write(f"• {topic.title()}")
        else:
            st.write("No weak topics identified yet. Keep practicing!")
    
    with col5:
        st.subheader("📚 Current Focus")
        current_topic = data.get("current_topic", "Not set")
        st.info(f"**{current_topic.upper() if current_topic != 'Not set' else current_topic}**")
        if st.button("🔄 Update Focus Topic"):
            # Simple topic selection
            topics = ["Arrays", "Strings", "Linked Lists", "Trees", "Graphs", "Dynamic Programming", "Sorting", "Searching"]
            selected_topic = st.selectbox("Choose your focus topic:", topics)
            if st.button("Set Focus"):
                data["current_topic"] = selected_topic.lower()
                save_data(data)
                st.success(f"Focus updated to: {selected_topic}")

# --- Problem Recommendations Section ---
elif section == "Problem Recommendations Dashboard":
    st.markdown('<div class="section-header">Problem Recommendations Dashboard</div>', unsafe_allow_html=True)
    
    tab1, tab2 = st.tabs(["🎲 Get Random Problem", "📚 Topic-Based Recommendations"])
    
    with tab1:
        st.subheader("Your Next Challenge")
        if st.button("🎯 Recommend Random Problem", type="primary"):
            problem = recommend_problem(data)
            st.session_state["current_problem"] = problem
            st.markdown('<div class="problem-card">', unsafe_allow_html=True)
            st.write("**Problem:**", problem)
            st.markdown('</div>', unsafe_allow_html=True)
        elif "current_problem" in st.session_state:
            st.markdown('<div class="problem-card">', unsafe_allow_html=True)
            st.write("**Current Problem:**", st.session_state["current_problem"])
            st.markdown('</div>', unsafe_allow_html=True)
    
    with tab2:
        st.subheader("Personalized Learning Path")
        if st.button("📖 Get Topic Recommendations"):
            with st.spinner("Analyzing your progress..."):
                topic, links = recommend_next_problems(data)
                data["current_topic"] = topic
                save_data(data)
                
                st.success(f"**Recommended Focus Topic: {topic.upper()}**")
                
                if links:
                    st.info(f"Here are {len(links)} problems to practice {topic}:")
                    for i, (title, url) in enumerate(links, 1):
                        st.markdown(f"{i}. [{title}]({url})")
                else:
                    st.warning("No recommendations available for this topic yet.")

# --- Submit Solution Section ---
elif section == "Submit Solution":
    st.markdown('<div class="section-header">Submit Solution</div>', unsafe_allow_html=True)
    
    if "current_problem" not in st.session_state:
        st.warning("Please get a problem recommendation first!")
        if st.button("Get Problem Recommendation"):
            st.switch_page("Problem Recommendations Dashboard")
    else:
        st.subheader("Current Problem")
        st.markdown('<div class="problem-card">', unsafe_allow_html=True)
        st.write(st.session_state["current_problem"])
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.subheader("Your Solution")
        user_code = st.text_area("Paste your code here:", height=200, 
                                placeholder="// Write your solution here...")
        
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("💡 Get Hint", use_container_width=True):
                if user_code.strip():
                    hint = provide_hint(st.session_state["current_problem"], user_code)
                    st.markdown('<div class="info-box">', unsafe_allow_html=True)
                    st.write("**Hint:**", hint)
                    st.markdown('</div>', unsafe_allow_html=True)
                else:
                    st.warning("Please enter some code first!")
        
        with col2:
            if st.button("📝 Get Full Feedback", use_container_width=True, type="primary"):
                if user_code.strip():
                    with st.spinner("Analyzing your solution..."):
                        hint = provide_hint(st.session_state["current_problem"], user_code)
                        feedback = analyze_solution(st.session_state["current_problem"], user_code)
                    
                    st.markdown('<div class="info-box">', unsafe_allow_html=True)
                    st.subheader("💡 Hint")
                    st.write(hint)
                    st.markdown('</div>', unsafe_allow_html=True)
                    
                    st.markdown('<div class="success-box">', unsafe_allow_html=True)
                    st.subheader("📊 Feedback")
                    st.write(feedback)
                    st.markdown('</div>', unsafe_allow_html=True)
                    
                    # Progress update
                    st.subheader("📈 Update Progress")
                    solved = st.radio("Did you solve this problem?", 
                                    ["Yes", "No", "Partially"], horizontal=True)
                    
                    if st.button("Save Progress"):
                        topic_for_update = data.get("current_topic", "arrays")
                        data = update_progress(data, solved=(solved == "Yes"), topic=topic_for_update)
                        save_data(data)
                        st.success("Progress saved successfully!")
                else:
                    st.error("Please enter your solution code first!")

# --- Mini Contest Section ---
elif section == "Mini Contest":
    st.markdown('<div class="section-header">Mini Contest</div>', unsafe_allow_html=True)
    
    if st.button("🎮 Generate New Contest", type="primary"):
        with st.spinner("Creating your personalized contest..."):
            st.session_state["contest"] = generate_contest(data, num_problems=3)
        st.success("Contest generated! You have 3 problems to solve.")
    
    if "contest" in st.session_state:
        st.subheader("Contest Problems")
        
        for i, item in enumerate(st.session_state["contest"]):
            with st.expander(f"Problem {i+1} - Click to view", expanded=(i == 0)):
                st.markdown('<div class="problem-card">', unsafe_allow_html=True)
                st.write(item["problem"])
                solved = st.checkbox(f"Mark as solved", key=f"solved_{i}")
                st.session_state["contest"] = update_contest(st.session_state["contest"], i, solved)
                st.markdown('</div>', unsafe_allow_html=True)
        
        if st.button("📊 Score Contest", type="secondary"):
            score = score_contest(st.session_state["contest"])
            
            # Visual score display
            if score >= 80:
                st.balloons()
                st.success(f"🏅 Excellent! Contest Score: {score}%")
            elif score >= 60:
                st.success(f"🎯 Good job! Contest Score: {score}%")
            else:
                st.warning(f"📚 Keep practicing! Contest Score: {score}%")
            
            # Update progress
            for i, item in enumerate(st.session_state["contest"]):
                topic_for_update = data.get("current_topic", "arrays")
                data = update_progress(data, solved=item["solved"], topic=topic_for_update)
            save_data(data)

# --- Progress Analytics Section ---
elif section == "Progress Analytics":
    st.markdown('<div class="section-header">Progress Analytics</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("📈 Performance Metrics")
        
        # Create metrics in cards
        metrics_col1, metrics_col2, metrics_col3 = st.columns(3)
        
        with metrics_col1:
            st.markdown('<div class="metric-card">', unsafe_allow_html=True)
            st.metric("Total Solved", len(data["solved"]))
            st.markdown('</div>', unsafe_allow_html=True)
            
        with metrics_col2:
            st.markdown('<div class="metric-card">', unsafe_allow_html=True)
            st.metric("Total Attempted", len(data["solved"]) + len(data["failed"]))
            st.markdown('</div>', unsafe_allow_html=True)
            
        with metrics_col3:
            st.markdown('<div class="metric-card">', unsafe_allow_html=True)
            st.metric("Success Rate", 
                     f"{(len(data['solved']) / (len(data['solved']) + len(data['failed'])) * 100):.1f}%" 
                     if (len(data['solved']) + len(data['failed'])) > 0 else "0%")
            st.markdown('</div>', unsafe_allow_html=True)
        
        # Weak topics analysis
        st.subheader("🎯 Topic Analysis")
        if data["weak_topics"]:
            st.write("**Areas needing improvement:**")
            for topic in data["weak_topics"]:
                progress_val = random.randint(20, 70)  # Mock progress - replace with real data
                st.write(f"- {topic.title()}")
                st.progress(progress_val / 100)
        else:
            st.info("Continue practicing to identify areas for improvement!")
    
    with col2:
        st.subheader("🔥 Streak & Achievements")
        st.info(f"**Current Streak:** {data['streak']} days")
        
        # Mock achievements
        achievements = [
            ("🚀 First Problem Solved", True),
            ("📚 10 Problems Solved", len(data["solved"]) >= 10),
            ("🔥 7-Day Streak", data["streak"] >= 7),
            ("🏆 Contest Master", "contest" in st.session_state and any(item["solved"] for item in st.session_state.get("contest", []))),
        ]
        
        st.write("**Achievements:**")
        for achievement, unlocked in achievements:
            if unlocked:
                st.success(f"✓ {achievement}")
            else:
                st.write(f"○ {achievement}")

# --- Footer ---
st.markdown("---")
st.markdown("<div style='text-align: center; color: gray;'>Keep coding! 🚀 DSA Coach AI-Agent</div>", 
            unsafe_allow_html=True)
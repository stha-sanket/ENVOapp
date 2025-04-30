import streamlit as st
import random
import os  # Import the 'os' module
import google.generativeai as genai
from quiz_data import quiz_questions
from eco_alternatives import eco_alternatives
from ecobot_data import recycling_info, eco_tips, habit_changes, sustainability_faqs, should_i_questions, environmental_impacts

# Set page config
st.set_page_config(
    page_title="ENVOApp",
    page_icon="🌍",
    layout="wide"
)

# Initialize session state variables if they don't exist
if 'current_question' not in st.session_state:
    st.session_state.current_question = 0
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'quiz_completed' not in st.session_state:
    st.session_state.quiz_completed = False
if 'selected_alternative' not in st.session_state:
    st.session_state.selected_alternative = None
if 'daily_tip' not in st.session_state:
    st.session_state.daily_tip = random.choice(eco_tips)
if 'user_answered' not in st.session_state:
    st.session_state.user_answered = False
if 'last_answer_correct' not in st.session_state:
    st.session_state.last_answer_correct = None

# App header with custom styling
st.title("🌍 ENVOApp")
st.caption("Your guide to environmental sustainability and eco-friendly living")

# Main navigation
tab1, tab2, tab3 = st.tabs(["🎮 Quiz", "🌿 Eco-Alternatives", "💬 EcoBot"])

# Quiz Section
with tab1:
    st.header("🎮 Environmental Knowledge Quiz")
    st.write("Test your knowledge about environmental issues with this interactive quiz!")
    
    # Progress bar for quiz
    progress = (st.session_state.current_question) / len(quiz_questions)
    if not st.session_state.quiz_completed:
        st.progress(progress)
    
    if not st.session_state.quiz_completed:
        # Display current question
        current_q = quiz_questions[st.session_state.current_question]
        
        # Question card with Streamlit components
        st.subheader(f"Question {st.session_state.current_question + 1} of {len(quiz_questions)}")
        st.container().markdown(f"**{current_q['question']}**")
        
        # If user hasn't answered the current question yet, show the options
        if not st.session_state.user_answered:
            # Display options as buttons
            col1, col2 = st.columns(2)
            
            # Keep track of user selection
            user_answer = None
            
            with col1:
                if st.button(f"A. {current_q['options'][0]}", key="opt1", use_container_width=True):
                    user_answer = 0
                
                if st.button(f"C. {current_q['options'][2]}", key="opt3", use_container_width=True):
                    user_answer = 2
            
            with col2:
                if st.button(f"B. {current_q['options'][1]}", key="opt2", use_container_width=True):
                    user_answer = 1
                
                if st.button(f"D. {current_q['options'][3]}", key="opt4", use_container_width=True):
                    user_answer = 3
            
            # Process answer if user selected one
            if user_answer is not None:
                if user_answer == current_q["correct_answer"]:
                    st.session_state.last_answer_correct = True
                    st.session_state.score += 1
                else:
                    st.session_state.last_answer_correct = False
                
                st.session_state.user_answered = True
                st.rerun()
        
        # If user has answered, show the result and next button
        else:
            # Display options with highlighting for correct answer
            letters = ["A", "B", "C", "D"]
            options_container = st.container()
            
            for i, option in enumerate(current_q["options"]):
                option_letter = letters[i] if i < len(letters) else ""
                if i == current_q["correct_answer"]:
                    options_container.success(f"{option_letter}. {option} ✓")
                else:
                    options_container.write(f"{option_letter}. {option}")
            
            # Show feedback based on correctness
            st.write("---")
            if st.session_state.last_answer_correct:
                st.success(f"✅ Correct! {current_q['explanation']}")
            else:
                st.error(f"❌ Incorrect. {current_q['explanation']}")
                st.write(f"The correct answer was: **{current_q['options'][current_q['correct_answer']]}**")
            
            # Next question button with styling
            st.write("")  # Add some spacing
            
            if st.session_state.current_question < len(quiz_questions) - 1:
                if st.button("Next Question →", key="next_q", use_container_width=True):
                    st.session_state.current_question += 1
                    st.session_state.user_answered = False
                    st.session_state.last_answer_correct = None
                    st.rerun()
            else:
                if st.button("See Your Results →", key="see_results", use_container_width=True):
                    st.session_state.quiz_completed = True
                    st.rerun()
    
    else:
        # Quiz completed, show results with Streamlit components
        score_percent = (st.session_state.score / len(quiz_questions)) * 100
        
        # Results header
        st.subheader("Quiz Results")
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.metric("Your Score", f"{st.session_state.score}/{len(quiz_questions)}", f"{score_percent:.1f}%")
        
        # Feedback based on score with Streamlit components
        if score_percent >= 80:
            st.success("🌟 Excellent! You're an environmental expert! Your knowledge of environmental issues is impressive. Keep spreading awareness and making a positive impact!")
        elif score_percent >= 60:
            st.info("👍 Good job! You have solid environmental knowledge. You understand many key environmental concepts. Keep learning and growing your knowledge!")
        else:
            st.warning("🔍 You're on your way to learning more about environmental issues! This quiz highlights some areas where you can expand your knowledge. Every bit of learning helps create a more sustainable future.")
        
        # Option to retake quiz
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("Retake Quiz", key="retake", use_container_width=True):
                st.session_state.current_question = 0
                st.session_state.score = 0
                st.session_state.quiz_completed = False
                st.session_state.user_answered = False
                st.session_state.last_answer_correct = None
                st.rerun()

# Eco-Friendly Alternatives Section
with tab2:
    st.header("🌿 Eco-Friendly Alternatives")
    st.write("Click on common items to discover environmentally friendly alternatives!")
    
    # Create a grid of buttons for eco alternatives with improved styling
    with st.container():
        # Use expander to show instructions
        with st.expander("How to use this section"):
            st.write("""
            1. Click on any common household item in the list below
            2. View eco-friendly alternatives and their environmental impact
            3. Learn practical tips for making the switch
            """)
        
        # Create columns for the buttons with better layout
        cols = st.columns(3)
        
        # Distribute the alternatives across the columns
        for i, (item, details) in enumerate(eco_alternatives.items()):
            col_idx = i % 3
            with cols[col_idx]:
                # Create a button for each item with full width
                if st.button(item, key=f"alt_{i}", use_container_width=True):
                    st.session_state.selected_alternative = item
    
    # Display information about the selected alternative
    if st.session_state.selected_alternative:
        # Divider for visual separation
        st.divider()
        
        # Alternative section with styled container
        with st.container():
            alt_details = eco_alternatives[st.session_state.selected_alternative]
            
            # Header section
            st.subheader(f"Instead of {st.session_state.selected_alternative}, try:")
            
            # Create columns for layout
            col1, col2 = st.columns([1, 2])
            
            # Alternative name in first column
            with col1:
                st.markdown(f"### {alt_details['alternative']}")
            
            # Details in second column
            with col2:
                st.write(alt_details["description"])
                
                # Environmental impact with visual indicator
                impact_container = st.container()
                impact_container.write("**Environmental Impact**:")
                impact_container.success(alt_details["impact"])
            
            # Additional tips section if available
            if "additional_tips" in alt_details:
                st.info(f"**Pro Tip**: {alt_details['additional_tips']}")
            

# EcoBot Section
with tab3:
    st.header("💬 EcoBot")
    st.write("Ask me about sustainability, environmental issues, or if you should do something specific for the environment!")

    # Initialize Gemini API
                            
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel('gemini-2.0-flash')

    # Create two columns for layout
    tip_col, suggestion_col = st.columns([2, 1])

    # Display daily tip in main column
    with tip_col:
        st.subheader("Daily Eco Tip")
        tip_container = st.container(height=100)
        tip_container.info(st.session_state.daily_tip)

        # Refresh tip button
        if st.button("Get New Tip", use_container_width=True):
            st.session_state.daily_tip = random.choice(eco_tips)
            st.rerun()

    # Sample questions in second column
    with suggestion_col:
        st.subheader("Try asking about:")
        st.markdown("""
        - Climate change
        - Recycling batteries
        - Biggest environmental problems
        - Should I use plastic straws?
        """)

    # Divider for visual separation
    st.divider()

    # Chat interface with improved styling
    st.subheader("Ask EcoBot")

    # User input for chatbot with custom styling
    user_question = st.text_input(
        "Type your environmental question here:",
        placeholder="E.g., How do I recycle batteries? What is climate change? Should I use plastic?",
        key="ecobot_input"
    )

    # Create a chat container
    chat_container = st.container()

    if user_question:
        # Display user question
        with chat_container:
            st.write(f"**You**: {user_question}")

        # Call Gemini API
        try:
            with st.spinner("EcoBot is thinking..."):
                prompt = f"""
                You are EcoBot, a friendly and informative chatbot designed to help people learn about environmental sustainability.
                You have access to a knowledge base of recycling information, eco tips, habit changes, sustainability FAQs, should-I questions, and information about environmental impacts.
                Answer questions clearly, concisely, and in a friendly manner.  If you don't have a direct answer, provide general guidance or suggest related topics.  Do not claim expertise or knowledge you don't have.

                User Question: {user_question}
                """

                response = model.generate_content(prompt)

                # Display Gemini's response
                with chat_container:
                    if response.text:
                        st.write(f"**EcoBot**: {response.text}")
                    else:
                        st.error("**EcoBot**: I encountered an error generating a response.  Please try again.")

        except Exception as e:
            with chat_container:
                st.error(f"**EcoBot**: An error occurred: {e}. Please check your API key and try again.")

    else:
        # Initial state - show greeting
        with chat_container:
            st.write(
                "**EcoBot**: Hello! I'm here to help answer your environmental questions. What would you like to know about sustainability?")
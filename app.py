import streamlit as st
import pandas as pd
import random  # Add this import at the top
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from collections import defaultdict, Counter
from dataset import all_questions, scoring_keywords, purpose_mappings,static_questions, static_purpose_mappings
# Set page configuration
st.set_page_config(page_title="Enhanced Adaptive Mental Health & Wellness Screening Tool", layout="wide")

# Load model (will download on first run)
@st.cache_resource
def load_model():
    return SentenceTransformer('all-MiniLM-L6-v2')

model = load_model()


def classify_response(response_text):
    """Enhanced response classification with better matching"""
    response_text = response_text.lower()
    response_embedding = model.encode([response_text])[0]
    
    category_texts = []
    categories = []
    
    for category, data in scoring_keywords.items():
        category_text = " ".join(data["keywords"])
        category_texts.append(category_text)
        categories.append((category, data["score"]))
    
    category_embeddings = model.encode(category_texts)
    similarities = cosine_similarity([response_embedding], category_embeddings)[0]
    
    best_match_index = np.argmax(similarities)
    best_match_category, best_match_score = categories[best_match_index]
    
    return best_match_score, best_match_category

def analyze_response_for_new_domains(response_text, all_questions, threshold=0.3):
    """FIXED: Analyze a response to identify new relevant domains/purposes"""
    response_embedding = model.encode([response_text])[0]
    
    # Get unique purposes and their questions
    purpose_to_questions = defaultdict(list)
    domain_to_questions = defaultdict(list)  # ADDED: Also track by domain
    
    for q in all_questions:
        purpose_to_questions[q["purpose"]].append(q)
        domain_to_questions[q["domain"]].append(q)  # ADDED
    
    # Check similarity with all purposes AND domains
    all_categories = list(purpose_to_questions.keys()) 
    category_embeddings = model.encode(all_categories)
    
    similarities = cosine_similarity([response_embedding], category_embeddings)[0]
    
    # Find categories above threshold
    relevant_categories = []
    for i, (category, similarity) in enumerate(zip(all_categories, similarities)):
        if similarity >= threshold:
            relevant_categories.append((category, similarity))
    
    # Sort by similarity
    relevant_categories.sort(key=lambda x: x[1], reverse=True)
    
    return relevant_categories

def get_initial_relevant_domains(user_input, all_questions, top_k=3):
    """FIXED: Get initially relevant domains from user input"""
    user_embedding = model.encode([user_input])[0]
    
    # Group questions by BOTH purpose and domain
    purpose_to_questions = defaultdict(list)
    domain_to_questions = defaultdict(list)
    
    for q in all_questions:
        purpose_to_questions[q["purpose"]].append(q)
        domain_to_questions[q["domain"]].append(q)
    
    # Calculate similarity with both purposes and domains
    purposes = list(purpose_to_questions.keys())
    domains = list(domain_to_questions.keys())
    all_categories = purposes 
    
    category_embeddings = model.encode(all_categories)
    similarities = cosine_similarity([user_embedding], category_embeddings)[0]
    
    # Get top K most relevant categories
    category_similarities = list(zip(all_categories, similarities))
    category_similarities.sort(key=lambda x: x[1], reverse=True)
    
    return category_similarities[:top_k]

def get_questions_from_active_domains(active_domains, asked_questions, all_questions, max_per_category=3):
    """Get questions from currently active domains with permanent purpose limits"""
    available_questions = []
    asked_ids = set(asked_questions)
    
    # Track how many questions have been asked for each purpose historically
    purpose_asked_counts = defaultdict(int)
    for q_id in asked_ids:
        # Find the question in all_questions to get its purpose
        for q in all_questions:
            if q["id"] == q_id:
                purpose_asked_counts[q["purpose"]] += 1
                break
    
    # Group unasked questions by purpose and domain
    purpose_questions = defaultdict(list)
    domain_questions = defaultdict(list)
    
    # Only add questions from purposes that haven't reached their limit
    for q in all_questions:
        if q["id"] not in asked_ids and purpose_asked_counts[q["purpose"]] < max_per_category:
            purpose_questions[q["purpose"]].append(q)
            domain_questions[q["domain"]].append(q)

    used_questions = []

    # Process each active domain
    for category, score in active_domains:
        potential_questions = []
        
        # Get matching questions from both purpose and domain
        if category in purpose_questions:
            potential_questions.extend(purpose_questions[category])
        if category in domain_questions:
            potential_questions.extend(domain_questions[category])
        
        # Shuffle to randomize selection
        random.shuffle(potential_questions)
        
        # Add questions while checking against historical counts
        for q in potential_questions:
            if (q["id"] not in asked_ids and 
                q not in used_questions and 
                purpose_asked_counts[q["purpose"]] < max_per_category):
                
                used_questions.append(q)
                purpose_asked_counts[q["purpose"]] += 1
                
                # Stop if we've hit the limit for this purpose
                if purpose_asked_counts[q["purpose"]] >= max_per_category:
                    # Remove all remaining questions with this purpose
                    purpose_questions[q["purpose"]] = []
    
    return used_questions


# def get_questions_from_active_domains(active_domains, asked_questions, all_questions, max_per_category=3):
#     """Get questions from currently active domains plus exactly 2 questions from outside domains"""
#     available_questions = []
#     asked_ids = set(asked_questions)
    
#     # Track how many questions have been asked for each purpose historically
#     purpose_asked_counts = defaultdict(int)
#     for q_id in asked_ids:
#         for q in all_questions:
#             if q["id"] == q_id:
#                 purpose_asked_counts[q["purpose"]] += 1
#                 break
    
#     # Get active domain and purpose names for comparison
#     active_domain_names = {domain for domain, _ in active_domains}
    
#     # Group questions
#     active_domain_questions = []
#     outside_domain_questions = []
    
#     # First pass - separate questions into active and outside domains
#     for q in all_questions:
#         if q["id"] not in asked_ids and purpose_asked_counts[q["purpose"]] < max_per_category:
#             if q["domain"] in active_domain_names or q["purpose"] in active_domain_names:
#                 active_domain_questions.append(q)
#             else:
#                 outside_domain_questions.append(q)

#     used_questions = []

#     # Process active domain questions
#     for category, score in active_domains:
#         potential_questions = [q for q in active_domain_questions 
#                             if q["domain"] == category or q["purpose"] == category]
        
#         # Shuffle to randomize selection
#         random.shuffle(potential_questions)
        
#         # Add questions while checking against historical counts
#         for q in potential_questions:
#             if (q["id"] not in asked_ids and 
#                 q not in used_questions and 
#                 purpose_asked_counts[q["purpose"]] < max_per_category):
                
#                 used_questions.append(q)
#                 purpose_asked_counts[q["purpose"]] += 1
                
#                 # Stop if we've hit the limit for this purpose
#                 if purpose_asked_counts[q["purpose"]] >= max_per_category:
#                     break
    
#     # Add exactly 2 random questions from outside domains
#     if outside_domain_questions:
#         random.shuffle(outside_domain_questions)
#         outside_count = 0
#         for q in outside_domain_questions:
#             if q not in used_questions and q["id"] not in asked_ids:
#                 used_questions.append(q)
#                 outside_count += 1
#                 if outside_count >= 2:  # Stop after adding exactly 2 questions
#                     break
    
#     return used_questions

def select_next_question_intelligently(context_text, available_questions, diversification_factor=0.4):
    """FIXED: Select next question with better balancing of relevance and diversification"""
    if not available_questions:
        return None, 0
    
    context_embedding = model.encode([context_text])[0]
    
    # Create embeddings for available questions
    question_texts = []
    for q in available_questions:
        combined_text = f"{q['question']} {q['purpose']} {q['domain']}"
        question_texts.append(combined_text)
    
    question_embeddings = model.encode(question_texts)
    
    # Calculate base similarities
    similarities = cosine_similarity([context_embedding], question_embeddings)[0]
    
    # FIXED: Add diversification factor based on BOTH domain AND purpose variety
    domain_counts = Counter([q["domain"] for q in available_questions])
    purpose_counts = Counter([q["purpose"] for q in available_questions])
    
    adjusted_scores = []
    
    for i, q in enumerate(available_questions):
        base_score = similarities[i]
        
        # Boost questions from less represented domains AND purposes
        domain_boost = diversification_factor / max(domain_counts[q["domain"]], 1)
        purpose_boost = diversification_factor / max(purpose_counts[q["purpose"]], 1)
        
        # Combine boosts
        total_boost = (domain_boost + purpose_boost) / 2
        adjusted_score = base_score + total_boost
        adjusted_scores.append(adjusted_score)
    
    # Select question with highest adjusted score
    best_index = np.argmax(adjusted_scores)
    return available_questions[best_index], adjusted_scores[best_index]

def update_active_domains(active_domains, new_domains, max_active=6):
    """FIXED: Update the list of active domains with better management"""
    # Create a dictionary for easier management
    active_dict = {domain: score for domain, score in active_domains}
    
    # Add or update domains from new discoveries
    for domain, score in new_domains:
        if domain in active_dict:
            # Boost existing domain (average of old and new scores)
            active_dict[domain] = (active_dict[domain] + score) / 2
        else:
            # Add new domain
            active_dict[domain] = score
    
    # Sort by score and keep top domains
    updated_domains = sorted(active_dict.items(), key=lambda x: x[1], reverse=True)
    return updated_domains[:max_active]
def analyze_static_responses(static_responses, model):
    """Analyze all static responses to identify relevant purposes"""
    relevant_purposes = defaultdict(float)
    
    # Track weights for different question types
    weights = {
        "static1": 0.3,  # Priorities
        "static2": 0.3,  # Free text description
        "static3": 0.2,  # Symptoms
        "static4": 0.2   # Obstacles
    }
    
    for question_id, responses in static_responses.items():
        question_weight = weights.get(question_id, 0.25)  # Default weight if not specified
        
        if question_id == "static2":  # Free text response
            if responses:  # Only process if there's text
                response_embedding = model.encode([responses])[0]
                purposes = list(purpose_mappings.keys())
                purpose_texts = [" ".join(terms) for terms in purpose_mappings.values()]
                purpose_embeddings = model.encode(purpose_texts)
                similarities = cosine_similarity([response_embedding], purpose_embeddings)[0]
                
                for purpose, similarity in zip(purposes, similarities):
                    if similarity > 0.3:  # Threshold
                        relevant_purposes[purpose] += similarity * question_weight
        
        else:  # Multiple choice responses (static1, static3, static4)
            if isinstance(responses, list):
                for choice in responses:
                    mapped_purposes = static_purpose_mappings.get(choice, [])
                    score_per_purpose = question_weight / len(mapped_purposes) if mapped_purposes else 0
                    
                    for purpose in mapped_purposes:
                        relevant_purposes[purpose] += score_per_purpose
    
    # Normalize all scores to range 0-1
    max_score = max(relevant_purposes.values()) if relevant_purposes else 1.0
    if max_score > 0:
        for purpose in relevant_purposes:
            relevant_purposes[purpose] /= max_score
    
    # Convert to sorted list of tuples
    sorted_purposes = sorted(
        [(purpose, score) for purpose, score in relevant_purposes.items()],
        key=lambda x: x[1],
        reverse=True
    )
    
    return sorted_purposes
# Initialize enhanced session state
if 'stage' not in st.session_state:
    st.session_state.stage = 'intro'
if 'static_responses' not in st.session_state:
    st.session_state.static_responses = {}
if 'current_question' not in st.session_state:
    st.session_state.current_question = None
if 'asked_questions' not in st.session_state:
    st.session_state.asked_questions = []
if 'user_responses' not in st.session_state:
    st.session_state.user_responses = {}
if 'scores' not in st.session_state:
    st.session_state.scores = {}
if 'initial_input' not in st.session_state:
    st.session_state.initial_input = ""
if 'question_count' not in st.session_state:
    st.session_state.question_count = 0
if 'max_questions' not in st.session_state:
    st.session_state.max_questions = 15
if 'active_domains' not in st.session_state:
    st.session_state.active_domains = []
if 'discovered_domains' not in st.session_state:
    st.session_state.discovered_domains = []
if 'static_question_index' not in st.session_state:
    st.session_state.static_question_index = 0

# App header
st.title("Enhanced Adaptive Mental Health & Wellness Screening Tool")

# Introduction stage
if st.session_state.stage == 'intro':
    st.markdown("""
    ### Welcome to Your Truly Adaptive Health Assessment
    
    This enhanced tool provides intelligent adaptive assessment that:
    
    **Initially targets** multiple relevant areas based on your input  
    **Dynamically discovers** new relevant areas based on your responses  
    **Balances coverage** across different health domains  
    **Learns continuously** from each response to guide the next question  
    
    **Assessment Domains:**
     Mental Health |  Substance Use |  Social Wellbeing |  Physical Wellness |  Quality of Life | Risk Assessment
    """)

    # Show static questions first
    if st.session_state.static_question_index < len(static_questions):
        current_static = static_questions[st.session_state.static_question_index]
        st.subheader(f"Question {st.session_state.static_question_index + 1} of {len(static_questions)}")
        
        if current_static["type"] == "multiple_choice":
            selected = st.multiselect(
                current_static["question"],
                options=current_static["options"]
            )
            if st.button("Next"):
                if selected:
                    st.session_state.static_responses[current_static["id"]] = selected
                    st.session_state.static_question_index += 1
                    st.rerun()
                else:
                    st.warning("Please select at least one option to continue.")
                    
        elif current_static["type"] == "text":
            response = st.text_area(current_static["question"], height=100)
            if st.button("Next"):
                if response:
                    st.session_state.static_responses[current_static["id"]] = response
                    st.session_state.static_question_index += 1
                    st.rerun()
                else:
                    st.warning("Please provide a response to continue.")
                    
        elif current_static["type"] == "scale":
            response = st.slider(
                current_static["question"],
                min_value=current_static["min"],
                max_value=current_static["max"],
                value=(current_static["min"] + current_static["max"]) // 2
            )
            if st.button("Next"):
                st.session_state.static_responses[current_static["id"]] = response
                st.session_state.static_question_index += 1
                st.rerun()
    
    # After static questions, show initial concerns input
    else:
        st.subheader("Tell us about your current concerns")
        user_input = st.text_area(
            "Based on your previous answers, please share any additional concerns or how you've been feeling:",
            height=150,
            placeholder="Share any concerns, symptoms, or areas you'd like to explore. The assessment will adapt based on what you tell us..."
        )
        
        st.session_state.max_questions = st.slider("Number of questions to ask:", min_value=5, max_value=30, value=15)
        
        if st.button("Start My Adaptive Assessment", type="primary"):
            if user_input:
                # Replace the existing code with:
                # Analyze static responses
                static_purposes = analyze_static_responses(st.session_state.static_responses, model)
                
                # Analyze user input
                input_embedding = model.encode([user_input])[0]
                purposes = list(purpose_mappings.keys())
                purpose_texts = [" ".join(terms) for terms in purpose_mappings.values()]
                purpose_embeddings = model.encode(purpose_texts)
                input_similarities = cosine_similarity([input_embedding], purpose_embeddings)[0]
                
                # Combine static and input purposes
                combined_purposes = defaultdict(float)
                
                # Add static purposes (40% weight)
                for purpose, score in static_purposes:
                    combined_purposes[purpose] += score * 0.4
                
                # Add input text purposes (60% weight)
                for purpose, similarity in zip(purposes, input_similarities):
                    if similarity > 0.3:  # Threshold
                        combined_purposes[purpose] += similarity * 0.6
                
                # Convert to list of tuples and sort
                initial_domains = sorted(
                    [(purpose, score) for purpose, score in combined_purposes.items()],
                    key=lambda x: x[1],
                    reverse=True
                )[:5]  # Top 5 most relevant
                
                st.session_state.active_domains = initial_domains
                
                available_questions = get_questions_from_active_domains(
                    st.session_state.active_domains,
                    st.session_state.asked_questions,
                    all_questions,
                    max_per_category=4
                )
                
                if available_questions:
                    # Create combined context from static responses and user input
                    static_context = " ".join([
                        str(value) for value in st.session_state.static_responses.values()
                    ])
                    combined_context = f"{user_input} {static_context}"
                    st.session_state.initial_input = combined_context
                    
                    first_question, _ = select_next_question_intelligently(combined_context, available_questions)
                    st.session_state.current_question = first_question
                    st.session_state.stage = 'questions'
                    st.session_state.question_count = 0
                    st.rerun()
            else:
                st.warning("Please describe your concerns to begin your personalized assessment.")

# Enhanced questions stage
elif st.session_state.stage == 'questions':
    # Display progress
    progress_text = f"Question {st.session_state.question_count + 1} of {st.session_state.max_questions}"
    progress_value = float(st.session_state.question_count) / st.session_state.max_questions
    st.progress(progress_value)
    st.write(f"{progress_text}")
    
    # FIXED: Show currently active domains with better formatting
    if st.session_state.active_domains:
        with st.expander(" Currently Active Assessment Areas"):
            st.write("**Based on your input and responses, we're focusing on:**")
            for i, (domain, score) in enumerate(st.session_state.active_domains):
                # Clean up domain names for display
                display_name = domain.replace('_', ' ').title()
                st.write(f"{i+1}. **{display_name}** (Relevance: {score:.3f})")
            
            if st.session_state.discovered_domains:
                st.write("** Newly discovered areas from your responses:**")
                recent_discoveries = list(set([d[0] for d in st.session_state.discovered_domains[-5:]]))  # Show unique recent discoveries
                for domain in recent_discoveries:
                    display_name = domain.replace('_', ' ').title()
                    st.write(f"• **{display_name}**")
    
    # Display current question
    current_question = st.session_state.current_question
    
    if current_question:
        st.markdown(f"** Assessment Area:** {current_question['domain'].replace('_', ' ').title()}")
        st.markdown(f"** Purpose:** {current_question['purpose'].replace('_', ' ').title()}")
        st.markdown("---")
        
        st.subheader(f"Question {st.session_state.question_count + 1}")
        st.markdown(f"### {current_question['question']}")
        st.write("Please describe your experience with this in your own words:")
        
        user_response = st.text_area(" Your answer:", 
                                   key=f"response_{current_question['id']}", 
                                   height=100,
                                   placeholder="Share as much or as little detail as you're comfortable with...")
        
        col1, col2, col3 = st.columns([2, 2, 3])
        
        with col1:
            if st.button("Submit & Continue", type="primary"):
                if user_response:
                    # Classify the response
                    score, category = classify_response(user_response)
                    
                    # Store the response and score
                    st.session_state.user_responses[current_question["id"]] = user_response
                    st.session_state.scores[current_question["id"]] = {
                        "score": score,
                        "category": category,
                        "question": current_question["question"],
                        "domain": current_question["domain"],
                        "purpose": current_question["purpose"]
                    }
                    
                    # Analyze response for new relevant domains
                    new_relevant_domains = analyze_response_for_new_domains(user_response, all_questions, threshold=0.25)  # LOWERED threshold
                    
                    if new_relevant_domains:
                        # Update discovered domains
                        st.session_state.discovered_domains.extend(new_relevant_domains)
                        
                        # Update active domains
                        st.session_state.active_domains = update_active_domains(
                            st.session_state.active_domains,
                            new_relevant_domains,
                            max_active=8  # INCREASED
                        )
                    
                    # Add to asked questions
                    st.session_state.asked_questions.append(current_question["id"])
                    st.session_state.question_count += 1
                    
                    # Check if we should continue
                    if st.session_state.question_count >= st.session_state.max_questions:
                        st.session_state.stage = 'results'
                        st.rerun()
                    else:
                        # Get available questions from current active domains
                        available_questions = get_questions_from_active_domains(
                            st.session_state.active_domains,
                            st.session_state.asked_questions,
                            all_questions,
                            max_per_category=4  # INCREASED
                        )
                        
                        if available_questions:
                            # Create context from all responses
                            all_context = st.session_state.initial_input + " " + " ".join(st.session_state.user_responses.values())
                            
                            # Select next question intelligently
                            next_question, similarity = select_next_question_intelligently(
                                all_context, 
                                available_questions,
                                diversification_factor=0.5  # INCREASED diversification
                            )
                            
                            if next_question:
                                st.session_state.current_question = next_question
                                st.rerun()
                            else:
                                st.session_state.stage = 'results'
                                st.rerun()
                        else:
                            st.session_state.stage = 'results'
                            st.rerun()
                else:
                    st.warning("Please enter your response before continuing.")
        
        with col2:
            if st.button("Finish Assessment"):
                if user_response:
                    # Process current response
                    score, category = classify_response(user_response)
                    st.session_state.user_responses[current_question["id"]] = user_response
                    st.session_state.scores[current_question["id"]] = {
                        "score": score,
                        "category": category,
                        "question": current_question["question"],
                        "domain": current_question["domain"],
                        "purpose": current_question["purpose"]
                    }
                
                st.session_state.stage = 'results'
                st.rerun()
        
        # FIXED: Show assessment journey with better organization
        if st.session_state.user_responses:
            with st.expander("Assessment Journey (Previous Responses)"):
                # Group responses by domain for better organization
                domain_responses = defaultdict(list)
                for i, q_id in enumerate(st.session_state.asked_questions):
                    if q_id in st.session_state.user_responses:
                        data = st.session_state.scores.get(q_id, {})
                        domain_responses[data.get('domain', 'Unknown')].append((i+1, q_id, data))
                
                for domain, responses in domain_responses.items():
                    st.markdown(f"** {domain.replace('_', ' ').title()}**")
                    for q_num, q_id, data in responses:
                        response = st.session_state.user_responses[q_id]
                        st.markdown(f"*Q{q_num}:* {data.get('question', 'Question')}")
                        st.write(f"**Response:** {response[:100]}{'...' if len(response) > 100 else ''}")
                        if 'score' in data:
                            score_labels = {0: " Never/Not at all", 1: "Sometimes/Mild", 2: " Often/Moderate", 3: " Almost always/Severe"}
                            st.write(f"**Assessment:** {score_labels.get(data['score'], 'Unknown')}")
                    st.write("---")

# Results stage remains the same as original...
elif st.session_state.stage == 'results':
    st.title("Your Adaptive Assessment Results")
    
    if not st.session_state.scores:
        st.warning(" No responses recorded. Please start a new assessment.")
        if st.button(" Start New Assessment"):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()
    else:
        # Enhanced results processing
        domains = ["anxiety", "depression", "stress", "substance_use", "minority_stress", "social_support", 
                  "internalized_homophobia", "sleep", "physical_activity", "nutrition", "quality_of_life", 
                  "body_image", "sexual_health", "hiv_risk"]
        
        domain_scores = {domain: 0 for domain in domains}
        domain_counts = {domain: 0 for domain in domains}
        
        for q_id, data in st.session_state.scores.items():
            domain = data["domain"]
            score = data["score"]
            if domain in domain_scores:
                domain_scores[domain] += score
                domain_counts[domain] += 1
        
        # Calculate averages
        for domain in domain_scores:
            if domain_counts[domain] > 0:
                domain_scores[domain] = domain_scores[domain] / domain_counts[domain]
        
        # Show adaptive assessment summary
        st.markdown("## Adaptive Assessment Summary")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.info(f"**Initial Concerns:** {st.session_state.initial_input[:100]}...")
        with col2:
            st.info(f"**Total Questions:** {len(st.session_state.scores)}")
        with col3:
            st.info(f"** Domains Explored:** {len([d for d in domain_counts.values() if d > 0])}")
        
        # Show domain evolution
        if st.session_state.discovered_domains:
            with st.expander(" How Your Assessment Evolved"):
                st.write("**Initial Focus Areas:**")
                initial_domains = [d[0].replace('_', ' ').title() for d in st.session_state.active_domains[:3]]
                for domain in initial_domains:
                    st.write(f"• {domain}")
                
                st.write("**Areas Discovered During Assessment:**")
                discovered_set = set()
                for domain, score in st.session_state.discovered_domains:
                    display_name = domain.replace('_', ' ').title()
                    if display_name not in initial_domains and display_name not in discovered_set:
                        st.write(f"• {display_name} (Relevance: {score:.3f})")
                        discovered_set.add(display_name)
        
        # Display results by category
        st.markdown("## Mental Health Overview")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if domain_counts['anxiety'] > 0:
                st.metric(" Anxiety Level", f"{domain_scores['anxiety']:.1f}/3.0", 
                         f" {domain_counts['anxiety']} questions")

        with col2:
            if domain_counts['depression'] > 0:
                st.metric(" Depression Level", f"{domain_scores['depression']:.1f}/3.0", 
                         f" {domain_counts['depression']} questions")
            
        with col3:
            if domain_counts['stress'] > 0:
                st.metric(" Stress Level", f"{domain_scores['stress']:.1f}/3.0", 
                         f" {domain_counts['stress']} questions")
        
        # Enhanced recommendations
        st.markdown("##  Adaptive Insights & Recommendations")
        
        high_risk_domains = [domain for domain, score in domain_scores.items() 
                           if domain_counts[domain] > 0 and score >= 2.0]
        
        if high_risk_domains:
            st.warning(" **Areas of Concern Identified Through Adaptive Assessment**")
            for domain in high_risk_domains:
                domain_name = domain.replace('_', ' ').title()
                question_count = domain_counts[domain]
                st.write(f"• **{domain_name}**: Consider professional support (Based on {question_count} adaptive questions)")
        
        # Show assessment efficiency
        total_possible_questions = len(all_questions)
        questions_asked = len(st.session_state.scores)
        efficiency = (questions_asked / total_possible_questions) * 100
        
        st.success(f" **Assessment Efficiency**: Covered your key areas with only {questions_asked} out of {total_possible_questions} possible questions ({efficiency:.1f}% efficiency)")
        
        st.info(" **Important**: This adaptive assessment is for informational purposes only. If you're experiencing distress or having thoughts of self-harm, please contact a mental health professional immediately.")
        
        # Action buttons
        col1, col2 = st.columns(2)
        with col1:
            if st.button(" Start New Assessment", type="primary"):
                for key in list(st.session_state.keys()):
                    del st.session_state[key]
                st.rerun()
        
        with col2:
            if st.button("Download Results", type="secondary"):
                results_summary = f"""
ADAPTIVE HEALTH ASSESSMENT RESULTS
=================================

Initial Concerns: {st.session_state.initial_input}
Assessment Date: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M')}
Total Questions Answered: {len(st.session_state.scores)}
Assessment Efficiency: {efficiency:.1f}%

ADAPTIVE DOMAIN EXPLORATION:
Initial Focus: {', '.join([d[0].replace('_', ' ').title() for d in st.session_state.active_domains[:3]])}
Discovered Areas: {len(set([d[0] for d in st.session_state.discovered_domains]))}

DOMAIN SCORES (0-3 scale):
"""
                for domain, score in domain_scores.items():
                    if domain_counts[domain] > 0:
                        results_summary += f"{domain.replace('_', ' ').title()}: {score:.1f}/3.0 ({domain_counts[domain]} questions)\n"
                
                results_summary += "\n\nNote: This adaptive assessment is for informational purposes only."
                
                st.download_button(
                    label=" Download Adaptive Results",
                    data=results_summary,
                    file_name=f"adaptive_assessment_{pd.Timestamp.now().strftime('%Y%m%d_%H%M')}.txt",
                    mime="text/plain"
                )

# Footer
st.markdown("---")
st.caption("**Enhanced Adaptive Assessment** - Intelligently discovers and explores relevant health domains based on your unique responses. Questions are selected from validated instruments and adapt in real-time to your individual profile. **This tool is for educational and screening purposes only.**")
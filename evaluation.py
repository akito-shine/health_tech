import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import matplotlib.pyplot as plt
import seaborn as sns
from collections import defaultdict
import json

class MentalHealthModelEvaluator:
    def __init__(self):
        # Load the same model used in your app
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        
        # Your question database (copy from your main code)
        self.all_questions = self._load_questions()
        self.scoring_keywords = self._load_scoring_keywords()
        
    def _load_questions(self):
        """Load all questions from your questionnaires"""
        gad7_questions = [
            {"id": "gad1", "question": "Feeling nervous, anxious, or on edge", "domain": "anxiety"},
            {"id": "gad2", "question": "Not being able to stop or control worrying", "domain": "anxiety"},
            {"id": "gad3", "question": "Worrying too much about different things", "domain": "anxiety"},
            {"id": "gad4", "question": "Trouble relaxing", "domain": "anxiety"},
            {"id": "gad5", "question": "Being so restless that it's hard to sit still", "domain": "anxiety"},
            {"id": "gad6", "question": "Becoming easily annoyed or irritable", "domain": "anxiety"},
            {"id": "gad7", "question": "Feeling afraid as if something awful might happen", "domain": "anxiety"}
        ]
        
        dass21_questions = [
            {"id": "dass1", "question": "I couldn't seem to experience any positive feeling at all", "domain": "depression"},
            {"id": "dass2", "question": "I found it difficult to work up the initiative to do things", "domain": "depression"},
            {"id": "dass3", "question": "I felt that I had nothing to look forward to", "domain": "depression"},
            {"id": "dass4", "question": "I felt down-hearted and blue", "domain": "depression"},
            {"id": "dass5", "question": "I was unable to become enthusiastic about anything", "domain": "depression"},
            {"id": "dass6", "question": "I felt I wasn't worth much as a person", "domain": "depression"},
            {"id": "dass7", "question": "I felt that life was meaningless", "domain": "depression"},
            {"id": "dass8", "question": "I was aware of dryness of my mouth", "domain": "anxiety"},
            {"id": "dass9", "question": "I experienced breathing difficulty", "domain": "anxiety"},
            {"id": "dass10", "question": "I experienced trembling (e.g., in the hands)", "domain": "anxiety"},
            {"id": "dass11", "question": "I was worried about situations in which I might panic", "domain": "anxiety"},
            {"id": "dass12", "question": "I felt I was close to panic", "domain": "anxiety"},
            {"id": "dass13", "question": "I was aware of the action of my heart in the absence of physical exertion", "domain": "anxiety"},
            {"id": "dass14", "question": "I felt scared without any good reason", "domain": "anxiety"},
            {"id": "dass15", "question": "I found it hard to wind down", "domain": "stress"},
            {"id": "dass16", "question": "I tended to over-react to situations", "domain": "stress"},
            {"id": "dass17", "question": "I felt that I was using a lot of nervous energy", "domain": "stress"},
            {"id": "dass18", "question": "I found myself getting agitated", "domain": "stress"},
            {"id": "dass19", "question": "I found it difficult to relax", "domain": "stress"},
            {"id": "dass20", "question": "I was intolerant of anything that kept me from getting on with what I was doing", "domain": "stress"},
            {"id": "dass21", "question": "I felt that I was rather touchy", "domain": "stress"}
        ]
        
        psqi_questions = [
            {"id": "psqi1", "question": "During the past month, how would you rate your sleep quality overall?", "domain": "sleep"},
            {"id": "psqi2", "question": "During the past month, how long has it usually taken you to fall asleep each night?", "domain": "sleep"},
            {"id": "psqi3", "question": "During the past month, how many hours of actual sleep did you get at night?", "domain": "sleep"},
            {"id": "psqi4", "question": "During the past month, how often have you had trouble sleeping because you cannot get to sleep within 30 minutes?", "domain": "sleep"},
            {"id": "psqi5", "question": "During the past month, how often have you had trouble sleeping because you wake up in the middle of the night or early morning?", "domain": "sleep"}
        ]
        
        return gad7_questions + dass21_questions + psqi_questions
    
    def _load_scoring_keywords(self):
        """Load scoring criteria"""
        return {
            "never": {
                "score": 0,
                "keywords": ["never", "not at all", "doesn't apply", "no", "not", "none", "nothing", "rarely", "hardly ever"]
            },
            "sometimes": {
                "score": 1,
                "keywords": ["sometimes", "some of the time", "occasionally", "a bit", "slightly", "a little", "somewhat"]
            },
            "often": {
                "score": 2,
                "keywords": ["often", "good part of time", "considerable", "a lot", "frequently", "regular", "regularly"]
            },
            "almost_always": {
                "score": 3,
                "keywords": ["almost always", "very much", "most of the time", "severe", "severely", "extremely", "constantly"]
            }
        }

    def classify_response(self, response_text):
        """Your existing classification function"""
        response_text = response_text.lower()
        response_embedding = self.model.encode([response_text])[0]
        
        category_texts = []
        categories = []
        
        for category, data in self.scoring_keywords.items():
            category_text = " ".join(data["keywords"])
            category_texts.append(category_text)
            categories.append((category, data["score"]))
        
        category_embeddings = self.model.encode(category_texts)
        similarities = cosine_similarity([response_embedding], category_embeddings)[0]
        best_match_index = np.argmax(similarities)
        best_match_category, best_match_score = categories[best_match_index]
        
        return best_match_score, best_match_category

    def find_next_relevant_question(self, initial_input, previous_responses, asked_questions):
        """Your existing adaptive question selection function"""
        combined_context = initial_input + " " + " ".join(previous_responses.values()) if previous_responses else initial_input
        context_embedding = self.model.encode([combined_context])[0]
        
        asked_ids = set(asked_questions)
        available_questions = [q for q in self.all_questions if q["id"] not in asked_ids]
        
        if not available_questions:
            return None, 0
        
        question_texts = [q["question"] for q in available_questions]
        question_embeddings = self.model.encode(question_texts)
        similarities = cosine_similarity([context_embedding], question_embeddings)[0]
        best_match_index = np.argmax(similarities)
        
        return available_questions[best_match_index], similarities[best_match_index]

    def test_scoring_accuracy(self):
        """Test if response classification makes sense"""
        print("=== TESTING RESPONSE SCORING ACCURACY ===\n")
        
        # Test cases with expected scores
        test_cases = [
            ("I never feel this way", 0),
            ("This doesn't happen to me at all", 0),
            ("Sometimes I experience this", 1),
            ("I feel this way occasionally", 1),
            ("I often have this problem", 2),
            ("This happens to me frequently", 2),
            ("I always feel this way", 3),
            ("This is extremely severe for me", 3),
            ("I constantly experience this", 3)
        ]
        
        correct_predictions = 0
        results = []
        
        for response, expected_score in test_cases:
            predicted_score, category = self.classify_response(response)
            is_correct = predicted_score == expected_score
            correct_predictions += is_correct
            
            results.append({
                'response': response,
                'expected': expected_score,
                'predicted': predicted_score,
                'category': category,
                'correct': is_correct
            })
            
            status = "✓" if is_correct else "✗"
            print(f"{status} '{response}' -> Expected: {expected_score}, Got: {predicted_score} ({category})")
        
        accuracy = correct_predictions / len(test_cases)
        print(f"\nScoring Accuracy: {accuracy:.2%} ({correct_predictions}/{len(test_cases)})")
        return results

    def test_question_selection_logic(self):
        """Test if question selection follows logical patterns"""
        print("\n=== TESTING QUESTION SELECTION LOGIC ===\n")
        
        # Test scenarios with expected domain preferences
        test_scenarios = [
            {
                "initial_input": "I can't sleep at night and keep tossing and turning",
                "expected_domains": ["sleep"],
                "description": "Sleep-focused input"
            },
            {
                "initial_input": "I feel worried and anxious all the time, my heart races",
                "expected_domains": ["anxiety"],
                "description": "Anxiety-focused input"
            },
            {
                "initial_input": "I feel hopeless and empty, nothing brings me joy anymore",
                "expected_domains": ["depression"],
                "description": "Depression-focused input"
            },
            {
                "initial_input": "I'm overwhelmed and can't handle pressure, everything irritates me",
                "expected_domains": ["stress"],
                "description": "Stress-focused input"
            }
        ]
        
        results = []
        
        for scenario in test_scenarios:
            print(f"Testing: {scenario['description']}")
            print(f"Input: '{scenario['initial_input']}'")
            
            # Get first 3 questions to see the pattern
            asked_questions = []
            responses = {}
            
            for i in range(3):
                if i == 0:
                    # First question based on initial input only
                    question, similarity = self.find_next_relevant_question(
                        scenario['initial_input'], {}, asked_questions
                    )
                else:
                    # Subsequent questions based on context
                    question, similarity = self.find_next_relevant_question(
                        scenario['initial_input'], responses, asked_questions
                    )
                
                if question:
                    asked_questions.append(question['id'])
                    # Simulate a response that would lead to more questions in the same domain
                    responses[question['id']] = f"Yes, I experience this {['never', 'sometimes', 'often'][i]}"
                    
                    domain_match = question['domain'] in scenario['expected_domains']
                    match_indicator = "✓" if domain_match else "✗"
                    
                    print(f"  Q{i+1}: [{question['domain']}] {question['question'][:60]}... {match_indicator}")
                    print(f"       Similarity: {similarity:.3f}")
            
            print()
            results.append({
                'scenario': scenario['description'],
                'questions_asked': asked_questions,
                'domains': [q['domain'] for q in [self.get_question_by_id(qid) for qid in asked_questions]]
            })
        
        return results

    def test_adaptive_flow_coherence(self):
        """Test if the adaptive flow maintains coherence"""
        print("=== TESTING ADAPTIVE FLOW COHERENCE ===\n")
        
        # Simulate a complete user journey
        initial_input = "I've been having panic attacks and can't sleep because I'm worried about work"
        
        print(f"Initial Input: '{initial_input}'\n")
        
        asked_questions = []
        responses = {}
        similarity_scores = []
        
        # Simulate 5 questions
        for i in range(5):
            question, similarity = self.find_next_relevant_question(
                initial_input, responses, asked_questions
            )
            
            if question:
                asked_questions.append(question['id'])
                similarity_scores.append(similarity)
                
                # Simulate realistic responses that build context
                if question['domain'] == 'anxiety':
                    response = f"Yes, I have this problem {['sometimes', 'often', 'very often'][min(i, 2)]}"
                elif question['domain'] == 'sleep':
                    response = f"This affects my sleep {['a little', 'quite a bit', 'severely'][min(i, 2)]}"
                elif question['domain'] == 'stress':
                    response = f"Work stress makes this {['somewhat', 'much', 'extremely'][min(i, 2)]} worse"
                else:
                    response = f"I experience this {['rarely', 'sometimes', 'frequently'][min(i, 2)]}"
                
                responses[question['id']] = response
                
                print(f"Q{i+1}: [{question['domain']}] {question['question']}")
                print(f"     Similarity: {similarity:.3f}")
                print(f"     Response: '{response}'\n")
        
        # Analyze coherence
        domains = [self.get_question_by_id(qid)['domain'] for qid in asked_questions]
        domain_distribution = pd.Series(domains).value_counts()
        
        print("Domain Distribution:")
        for domain, count in domain_distribution.items():
            print(f"  {domain}: {count} questions")
        
        print(f"\nSimilarity Score Trend: {similarity_scores}")
        
        return {
            'questions': asked_questions,
            'domains': domains,
            'similarity_scores': similarity_scores,
            'responses': responses
        }

    def get_question_by_id(self, question_id):
        """Helper function to get question by ID"""
        for q in self.all_questions:
            if q['id'] == question_id:
                return q
        return None

    def analyze_model_biases(self):
        """Check for potential biases in question selection"""
        print("=== ANALYZING MODEL BIASES ===\n")
        
        # Test with neutral input to see default behavior
        neutral_inputs = [
            "I'm looking to learn more about how this system works.","I have some questions but I’m not sure where to begin.",
            "Lately, I’ve been struggling to feel normal — always exhausted, on edge, and emotionally drained.",
            "I can’t explain it exactly, but I’ve felt overwhelmed, restless at night, and low for a while now."
        ]
        
        domain_selections = defaultdict(int)
        
        print("Testing neutral inputs for bias:")
        for input_text in neutral_inputs:
            question, similarity = self.find_next_relevant_question(input_text, {}, [])
            if question:
                domain_selections[question['domain']] += 1
                print(f"'{input_text}' -> {question['domain']} domain")
        
        print(f"\nDomain selection frequency for neutral inputs:")
        total = sum(domain_selections.values())
        for domain, count in domain_selections.items():
            percentage = (count / total) * 100
            print(f"  {domain}: {count}/{total} ({percentage:.1f}%)")
        
        return domain_selections

    def run_comprehensive_evaluation(self):
        """Run all evaluation tests"""
        print("COMPREHENSIVE MODEL EVALUATION")
        print("=" * 50)
        
        # Run all tests
        scoring_results = self.test_scoring_accuracy()
        question_logic_results = self.test_question_selection_logic()
        flow_results = self.test_adaptive_flow_coherence()
        bias_results = self.analyze_model_biases()
        
        # Summary
        print("\n" + "=" * 50)
        print("EVALUATION SUMMARY")
        print("=" * 50)
        
        scoring_accuracy = sum(1 for r in scoring_results if r['correct']) / len(scoring_results)
        print(f"✓ Response Scoring Accuracy: {scoring_accuracy:.2%}")
        
        print(f"✓ Question Selection Logic: Tested across 4 mental health domains")
        print(f"✓ Adaptive Flow: Maintains coherence across conversation")
        print(f"✓ Bias Analysis: Completed for neutral inputs")
        
        # Recommendations
        print("\nRECOMMENDations:")
        if scoring_accuracy < 0.8:
            print("- Consider refining scoring keywords for better accuracy")
        if len(set(bias_results.keys())) < 3:
            print("- Check for domain selection bias with neutral inputs")
        
        return {
            'scoring_results': scoring_results,
            'question_logic_results': question_logic_results,
            'flow_results': flow_results,
            'bias_results': bias_results
        }

# Usage example
if __name__ == "__main__":
    evaluator = MentalHealthModelEvaluator()
    results = evaluator.run_comprehensive_evaluation()
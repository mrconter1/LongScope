import random
import string

class Fact:
    def __init__(self, name, emotion):
        self.name = name
        self.emotion = emotion

    def __str__(self):
        return f"{self.name} is {self.emotion}"

class Question:
    def __init__(self, facts, emotion, question_type="at_least_one"):
        self.facts = facts
        self.emotion = emotion
        self.question_type = question_type

    def is_claim_true(self):
        if self.question_type == "at_least_one":
            return any(fact.emotion == self.emotion for fact in self.facts)
        elif self.question_type == "all":
            return all(fact.emotion == self.emotion for fact in self.facts)
        elif self.question_type == "none":
            return all(fact.emotion != self.emotion for fact in self.facts)
        # Additional conditions can be added here

    def __str__(self):
        question_types = {
            "at_least_one": f"Is at least one out of {', '.join(fact.name for fact in self.facts)} {self.emotion}?",
            "all": f"Are all of {', '.join(fact.name for fact in self.facts)} {self.emotion}?",
            "none": f"Are none of {', '.join(fact.name for fact in self.facts)} {self.emotion}?"
            # Additional question formats can be added here
        }
        return f"Question: {question_types.get(self.question_type, 'Invalid question type')}"

def generate_random_string(min_length=6, max_length=15):
    length = random.randint(min_length, max_length)
    return ''.join(random.choices(string.ascii_uppercase, k=length))

def generate_random_fact():
    name = generate_random_string()
    emotion = random.choice(["happy", "sad", "angry"])  # Added another emotion
    return Fact(name, emotion)

def generate_question(facts, num_names, emotion, question_type):
    selected_facts = random.sample(facts, num_names)
    return Question(selected_facts, emotion, question_type)

# Usage
N = 10  # Number of facts to generate
facts_list = [generate_random_fact() for _ in range(N)]

# Generate a question
num_names_in_question = random.randint(2, 5)  # Vary the number of names
emotion_to_check = random.choice(["happy", "sad", "angry"])  # Vary the emotion
question_types = ["at_least_one", "all", "none"]  # Different types of questions
selected_question_type = random.choice(question_types)  # Randomly select question type

# Display the generated facts
for fact in facts_list:
    print(fact)

print("\n```\nAnswer: [True/False]\n```\n")

question = generate_question(facts_list, num_names_in_question, emotion_to_check, selected_question_type)
print(question)
answer = "Answer: " + ("True" if question.is_claim_true() else "False")
print(answer)

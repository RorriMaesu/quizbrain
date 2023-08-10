from flask import Flask, render_template, jsonify, request
import random
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'key1'

# Load questions from question data files
def load_questions():
    categories = [
        "Python", "Movies and TV Shows", "History", "Geography",
        "Pop Culture", "Sports", "Science", "Math"
    ]
    
    questions = []
    for category in categories:
        category_filename = category.lower().replace(' ', '_') + "_questions"
        question_module = __import__(category_filename)
        question_data = question_module.question_data
        questions.extend(question_data)
    
    return questions

def load_questions_by_category(category):
    category_filename = category.lower().replace(' ', '_') + "_questions"
    question_module = __import__(category_filename)
    return question_module.question_data

def get_random_questions_from_data(data, num_questions=5):
    random.shuffle(data)
    return data[:num_questions]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_questions')
def get_questions():
    num_questions = 5
    selected_category = request.args.get('category', type=str)
    asked_questions = request.args.get('askedQuestions', type=str)
    if asked_questions:
        asked_questions = json.loads(asked_questions)
    else:
        asked_questions = []

    if selected_category:
        question_data = load_questions_by_category(selected_category)
    else:
        question_data = load_questions()

    # Filter out already asked questions
    question_data = [q for q in question_data if q['question'] not in asked_questions]

    random_questions = get_random_questions_from_data(question_data, num_questions)
    formatted_questions = [
        {
            'question': question['question'],
            'correct_answer': question['correct_answer']
        }
        for question in random_questions
    ]
    return jsonify(questions=formatted_questions)

if __name__ == '__main__':
    app.run(debug=True)

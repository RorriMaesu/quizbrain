from flask import Flask, jsonify, request, send_from_directory, render_template
import random
import json
import os

app = Flask(__name__, static_folder="static", template_folder=".", static_url_path="")
app.config['SECRET_KEY'] = 'key1'

@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory(os.path.join(os.path.abspath("."), 'static'), filename)

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
    return render_template("index.html")

@app.route('/get_questions')
def get_questions():
    num_questions = 5
    selected_category = request.args.get('category', type=str)
    asked_questions = request.args.get('askedQuestions', type=str)
    if asked_questions:
        asked_questions = json.loads(asked_questions)
    else:
        asked_questions = []

    if selected_category == "Random":
        question_data = load_questions()
    elif selected_category:
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

# Load leaderboard data from JSON
def load_leaderboard():
    with open('leaderboard.json', 'r') as f:
        return json.load(f)

# Save leaderboard data to JSON
def save_leaderboard(data):
    with open('leaderboard.json', 'w') as f:
        json.dump(data, f, indent=4)

@app.route('/leaderboard')
def leaderboard():
    data = load_leaderboard()
    return render_template("leaderboard.html", leaderboard=data)

@app.route('/update_leaderboard', methods=['POST'])
def update_leaderboard():
    data = request.json
    category = data.get("category")
    name = data.get("name")
    score = data.get("score")
    
    leaderboard_data = load_leaderboard()
    scores = leaderboard_data.get("scores", [])

    # Append the new score only if it's not "Anonymous"
    if name != "Anonymous":
        scores.append({"name": name, "score": score, "category": category})
        
        # Sort scores in descending order
        scores.sort(key=lambda x: x['score'], reverse=True)
        
        # Trim to top 30 scores
        scores = scores[:30]
        
        leaderboard_data["scores"] = scores
        save_leaderboard(leaderboard_data)
    
    return jsonify(status="updated", message="Leaderboard updated!")

if __name__ == '__main__':
    app.run(debug=True)

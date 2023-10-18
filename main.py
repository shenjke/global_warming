from flask import Flask, render_template, request

app = Flask(__name__)

questions = [
    {"question": "Сортируете ли вы мусор?", "id": 1},
    {"question": "Используете ли вы велосипед или общественный транспорт?", "id": 2},
    {"question": "Сокращаете ли вы использование одноразовой посуды?", "id": 3},
    {"question": "Экономите ли вы воду в повседневной жизни?", "id": 4},
    {"question": "Используете ли вы энергоэффективные лампы и приборы?", "id": 5},
]

solutions = {
    1: "---",
    2: "---",
    3: "---",
    4: "---",
    5: "---",
}

@app.route('/')
def index():
    return render_template('index.html', questions=questions)

@app.route('/results', methods=['POST'])
def results():
    user_answers = {}
    for question in questions:
        question_id = question['id']
        user_answers[question_id] = request.form.get(str(question_id))

    user_solutions = [solutions[int(answer)] for answer in user_answers.values()]

    return render_template('results.html', user_solutions=user_solutions)

if __name__ == '__main__':
    app.run(debug=True)

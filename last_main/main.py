from flask import Flask, render_template, request

app = Flask(__name__)

questions = [
    {"question": "Сортируете ли вы мусор?", "id": "1"},
    {"question": "Используете ли вы велосипед или общественный транспорт?", "id": "2"},
    {"question": "Сокращаете ли вы использование одноразовой посуды?", "id": "3"},
    {"question": "Экономите ли вы воду в повседневной жизни?", "id": "4"},
    {"question": "Используете ли вы энергоэффективные лампы и приборы?", "id": "5"},
]

solutions = {
    "1": "Сортировка мусора помогает уменьшить загрязнение окружающей среды.",
    "2": "Использование велосипеда вместо автомобиля снижает выбросы углекислого газа.",
    "3": "Сокращение использования одноразовой посуды уменьшает отходы и пластиковое загрязнение",
    "4": "Экономия воды важна для уменьшения давления на водные ресурсы.",
    "5": "Использование энергоэффективных приборов уменьшает энергопотребление и выбросы парниковых газов."
}

@app.route('/')
def index():
    return render_template('index.html', questions=questions)

@app.route('/results', methods=['POST'])
def results():
    user_answers = {}
    for question in questions:
        question_id = question['id']
        user_answers[question_id] = request.form.get(question_id) 

    user_solutions = [solutions.get(answer, "Нет информации по этому вопросу.") for answer in user_answers.values()]

    return render_template('results.html', user_solutions=user_solutions)

@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

@app.route('/submit_feedback', methods=['POST'])
def submit_feedback():
    feedback_text = request.form.get('feedback')
    
    # Вместо этого места, можно сохранить обратную связь в базе данных или файле.
    # Например, feedback_text можно отправить на вашу почту или сохранить в базу данных.

    return render_template('submit_feedback.html')


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista pytań i odpowiedzi
questions = [
    {
        'question': 'Pytanie 1: Jakie jest twoje ulubione zwierzę?',
        'options': ['Kot', 'Pies', 'Rybka', 'Ptak'],
        'next_page': '/question/2'
    },
    {
        'question': 'Pytanie 2: Które jedzenie lubisz najbardziej?',
        'options': ['Pizza', 'Sushi', 'Burger', 'Sałatka'],
        'next_page': '/summary'
    }
]

# Inicjalizacja odpowiedzi (początkowo puste)
answers = {}

@app.route('/')
def index():
    return redirect(url_for('question', question_number=1))

@app.route('/question/<int:question_number>', methods=['GET', 'POST'])
def question(question_number):
    if request.method == 'POST':
        # Zapisz odpowiedź z formularza
        selected_option = request.form['answer']
        answers[question_number] = selected_option

        # Przekieruj do następnego pytania lub podsumowania
        next_question = questions[question_number - 1]['next_page']
        return redirect(next_question)

    if question_number <= len(questions):
        current_question = questions[question_number - 1]
        return render_template('question.html', question=current_question, question_number=question_number)
    else:
        return redirect(url_for('summary'))

@app.route('/summary')
def summary():
    return render_template('summary.html', answers=answers)

if __name__ == '__main__':
    app.run(debug=True)

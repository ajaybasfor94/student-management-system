from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add')
def add_student():
    return render_template('add_student.html')

@app.route('/students')
def view_students():
    return render_template('view_students.html')

if __name__ == '__main__':
    app.run(debug=True)
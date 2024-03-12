from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        id: 1,
        'title': 'Data Analyst',
        'location': 'Sans Fransisco, USA',
        'Salary': '$130000'
    },
    {
        id: 2,
        'title': 'Frontend Engineer',
        'location': 'Remote',
        'Salary': '$150000'
    },
    {
        id: 3,
        'title': 'Backend Engineer',
        'location': 'Remote',
        'Salary': '$250000'
    },
    {
        id: 4,
        'title': 'Data Scientist',
        'location': 'Sans Francisco, USA',
        'Salary': '$350000'
    }
]

@app.route('/')
def hello():
    return "Hello world!"

@app.route('/serve')
def greet():
    return render_template('index.html', jobs=JOBS)

@app.route('/api/jobs')
def list_jobs():
    return jsonify(JOBS)



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
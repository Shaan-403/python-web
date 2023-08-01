from flask import Flask, render_template, jsonify
app = Flask(__name__)


JOBS =[
    {
    'id':1,
    'title':'Data Analyst',
    'location': 'Bengaluru',
    'salary': "Rs. 10"
    },
    {
        'id':2,
        'title':'Data Scientist',
        'location': 'Pune',
        'salary': "Rs. 11"
    }
]


@app.route('/')
def hello_world():
    return render_template('home.html',jobs=JOBS)

@app.route('/api/jobs')
def list_jobs():
    return jsonify(JOBS)

if __name__ == "__main__":
    app.run(debug=True)
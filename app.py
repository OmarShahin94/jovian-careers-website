from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Amman, Jordan',
        'salary': 'JOD 800',
    },
    {
        'id': 2,
        'title': 'Data Scientist',
        'location': 'Amman, Jordan',
        'salary': 'JOD 1200',
    },
    {
        'id': 3,
        'title': 'Front-end Developer',
        'location': 'Amman, Jordan',
        'salary': 'JOD 900',
    },
    {
        'id': 4,
        'title': 'Back-end Developer',
        'location': 'Amman, Jordan',
        'salary': 'JOD 1000',
    },
    {
        'id': 5,
        'title': 'Full-stack Developer',
        'location': 'Amman, Jordan',
        'salary': 'JOD 1300',
    },
    {
        'id': 6,
        'title': 'Data Engineer',
        'location': 'Amman, Jordan',
        'salary': 'JOD 1000',
    },
]


@app.route("/")
def hello_jovian():
  return render_template("home.html", jobs=JOBS, company_name="Jovian")


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)

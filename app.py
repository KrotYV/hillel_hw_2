from flask import Flask, request
import requests
from faker import Faker
fake = Faker()

app = Flask(__name__)

@app.route('/requirements/')
def print_requirements():
    with open('requirements.txt') as f:
        answer = f.read()
    return f'Содержимое файла с пакетами: {answer}'


@app.route('/generate-users/')
def genereta_users():
    count = int(request.args.get('count', 100))
    answer = dict()
    for i in range(count):
        name = fake.name()
        email = fake.email()
        answer[name] = email
    return answer

@app.route('/mean/')
def avarage():
    with open('hw.csv') as f:
        list_1 = f.read().split('\n')
        height, weight = 0.0, 0.0
        count = 0

        for el in list_1[1:-2]:
            list_2 = el.split(',')
            height += float(list_2[1]) * 2.54
            weight += float(list_2[2]) * 0.453592
            count += 1
        answer_height = round(height / count, 2)
        answer_weight = round(weight / count, 2)
        answer = str(answer_height) + '<br>' + str(answer_weight)

    return answer

@app.route('/space/')
def astros():
    r = requests.get('http://api.open-notify.org/astros.json')
    answer = str(r.json()['number'])
    return answer


if __name__ == '__main__':
    app.run(debug=True)


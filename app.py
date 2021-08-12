from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home_page():
    return render_template('index.html')

@app.route('/math', methods=['POST'])
def math_operation():
    if request.method == 'POST':
        operation = request.form['operation']
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        if operation == 'add':
            r = num1+num2
            result = 'The sum of '+str(num1)+' and '+str(num2)+' is '+str(r)
        if operation == 'subtract':
            r = num1 - num2
            result = 'The difference of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if operation == 'multiply':
            r = num1 * num2
            result = 'The product of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if operation == 'divide':
            r = num1 / num2
            result = 'The quotient when ' + str(num1) + ' is divided by ' + str(num2) + ' is ' + str(r)
        return render_template('results.html', result=result)

@app.route('/via_postman', methods=['POST'])
def math_operation_via_postman():
    if request.method == 'POST':
        operation = request.json['operation']
        num1 = int(request.json['num1'])
        num2 = int(request.json['num2'])
        if operation == 'add':
            r = num1+num2
            result = 'The sum of '+str(num1)+' and '+str(num2)+' is '+str(r)
        if operation == 'subtract':
            r = num1 - num2
            result = 'The difference of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if operation == 'multiply':
            r = num1 * num2
            result = 'The product of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if operation == 'divide':
            r = num1 / num2
            result = 'The quotient when ' + str(num1) + ' is divided by ' + str(num2) + ' is ' + str(r)
        return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)

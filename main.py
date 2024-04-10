from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def calculator():
    num1 = int(request.args.get('num1'))
    num2 = int(request.args.get('num2'))
    operation = request.args.get('operation')

    if operation == '+':
        return str(num1 + num2)
    elif operation == '-':
        return str(num1 - num2)
    elif operation == '*':
        return str(num1 * num2)
    elif operation == '/':
        return str(num1 / num2)

if __name__ == '__main__':
    app.run(debug=True)
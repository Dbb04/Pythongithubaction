from flask import Flask
app = Flask(__name__)

def add(x, y):
    """This function will be tested by pytest."""
    return x + y

@app.route('/')
def hello_world():
    result = add(10, 5)
    return f'Hello from automated deploy! 10 + 5 = {result}.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
from flask import render_template
from flask import Flask
from pynput.keyboard import Key, Controller

keyboard = Controller()

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.get('/red')
def get_red():
    print('red')
    key = 'a'
    keyboard.press(key)
    return 'red', 200 

@app.get('/orange')
def get_orange():
    print('orange')
    key = 'b'
    keyboard.press(key)
    return 'orange', 200

@app.get('/yellow')
def get_yellow():
    print('yellow')
    key = 'c'
    keyboard.press(key)
    return 'yellow', 200

@app.get('/green')
def get_green():
    key = 'd'
    keyboard.press(key)
    print('green')
    return 'green', 200

@app.get('/cyan')
def get_cyan():
    key = 'e'
    keyboard.press(key)
    print('cyan')
    return 'cyan', 200  
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
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
    key = 's'
    keyboard.press(key)
    return 'red', 200 

@app.get('/blue')
def get_blue():
    print('blue')
    key = 'h'
    keyboard.press(key)
    return 'blue', 200 

@app.get('/yellow')
def get_yellow():
    print('yellow')
    return 'red', 200 

@app.get('/green')
def get_green():
    key = 'a'
    keyboard.press(key)
    print('green')
    return 'green', 200 

@app.get('/purple')
def get_purple():
    key = 'l'
    keyboard.press(key)
    print('purple')
    return 'purple', 200 

@app.route('/ashypurple')
def get_ashypurple():
    print('ashy purble')
    return 'ashypurple', 200 

@app.get('/orange')
def get_orange():
    key = 'o'
    keyboard.press(key)
    print('orange')
    return 'orange', 200 

@app.get('/white')
def get_white():
    key = 'm'
    keyboard.press(key)
    print('white')
    return 'white', 200

@app.get('/w0')
def get_w0():
    key = 'm'
    keyboard.press(key)
    print('w0')
    return 'w0', 200

@app.get('/w25')
def get_w25():
    key = 'm'
    keyboard.press(key)
    print('w25')
    return 'w25', 200 

@app.get('/w50')
def get_w50():
    key = 'm'
    keyboard.press(key)
    print('w50')
    return 'w50', 200

@app.get('/w75')
def get_w75():
    key = 'm'
    keyboard.press(key)
    print('w75')
    return 'w75', 200 

@app.get('/w100')
def get_w100():
    key = 'm'
    keyboard.press(key)
    print('w100')
    return 'w100', 200 

@app.get('/c0')
def get_c0():
    key = 'm'
    keyboard.press(key)
    print('c0')
    return 'c0', 200

@app.get('/c25')
def get_c25():
    key = 'm'
    keyboard.press(key)
    print('c25')
    return 'c25', 200 

@app.get('/c50')
def get_c50():
    key = 'm'
    keyboard.press(key)
    print('c50')
    return 'c50', 200

@app.get('/c75')
def get_c75():
    key = 'm'
    keyboard.press(key)
    print('c75')
    return 'c75', 200 

@app.get('/c100')
def get_c100():
    key = 'm'
    keyboard.press(key)
    print('c100')
    return 'c100', 200

@app.get('/kill')
def get_kill():
    key = 'k'
    keyboard.press(key)
    print('kill')
    return 'kill', 200 
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
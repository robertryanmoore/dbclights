from flask import render_template
from flask import Flask
from pynput.keyboard import Key, Controller

keyboard = Controller()

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/red')
def get_red():
    print('red')
    key = 'w'
    keyboard.press(key)
    return render_template('index.html')

@app.route('/blue')
def get_blue():
    print('blue')
    return render_template('index.html')

@app.route('/yellow')
def get_yellow():
    print('yellow')
    return render_template('index.html')

@app.route('/green')
def get_green():
    print('green')
    return render_template('index.html')

@app.route('/purple')
def get_purple():
    print('purple')
    return render_template('index.html')

@app.route('/ashypurple')
def get_ashypurple():
    print('ashy purble')
    return render_template('index.html')

    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
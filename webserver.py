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
    key = '1'
    keyboard.press(key)
    return 'red', 200 

@app.get('/orange')
def get_orange():
    print('orange')
    key = '2'
    keyboard.press(key)
    return 'orange', 200

@app.get('/yellow')
def get_yellow():
    print('yellow')
    key = '3'
    keyboard.press(key)
    return 'yellow', 200

@app.get('/green')
def get_green():
    key = '4'
    keyboard.press(key)
    print('green')
    return 'green', 200

@app.get('/cyan')
def get_cyan():
    key = '5'
    keyboard.press(key)
    print('cyan')
    return 'cyan', 200  

@app.get('/royalblue')
def get_royalblue():
    print('royalblue')
    key = '6'
    keyboard.press(key)
    return 'royalblue', 200

@app.get('/blue')
def get_blue():
    print('blue')
    key = '7'
    keyboard.press(key)
    return 'blue', 200

@app.get('/magenta')
def get_magenta():
    key = '8'
    keyboard.press(key)
    print('magenta')
    return 'magenta', 200

@app.get('/white')
def get_white():
    key = '0'
    keyboard.press(key)
    print('white')
    return 'white', 200   

@app.route('/rgbfade')
def get_rgbfade():
    print('rgbfade')
    key = 'z'
    keyboard.press(key)
    return 'rgbfade', 200

@app.route('/faderb')
def get_faderb():
    print('faderb')
    key = 'x'
    keyboard.press(key)
    return 'fade rb', 200

@app.route('/faderg')
def get_faderg():
    print('faderg')
    key = 'c'
    keyboard.press(key)
    return 'fade rg', 200

@app.route('/fadery')
def get_fadery():
    print('fadery')
    key = 'v'
    keyboard.press(key)
    return 'fade ry', 200

@app.route('/fadero')
def get_fadero():
    print('fadero')
    key = 'b'
    keyboard.press(key)
    return 'fade ro', 200

@app.route('/fadebg')
def get_fadebg():
    print('fade bg')
    key = 'n'
    keyboard.press(key)
    return 'fade bg', 200

@app.route('/fadebc')
def get_fadebc():
    print('fadebc')
    key = 'm'
    keyboard.press(key)
    return 'fade bc', 200

@app.route('/fadebm')
def get_fadebm():
    print('fadebm')
    key = ','
    keyboard.press(key)
    return 'fade bm', 200

@app.route('/bgtrainleft')
def get_bgtrainleft():
    print('bg train left')
    key = '.'
    keyboard.press(key)
    return 'bg train left', 200

@app.route('/bgtrainright')
def get_bgtrainright():
    print('bg train right')
    key = '/'
    keyboard.press(key)
    return 'bg train right', 200

@app.route('/rytrainleft')
def get_rytrainleft():
    print('ry train left')
    key = "'"
    keyboard.press(key)
    return 'ry train left', 200

@app.route('/rytrainright')
def get_rytrainright():
    print('ry train right')
    key = ";"
    keyboard.press(key)
    return 'ry train right', 200

@app.route('/fadepm')
def get_fadepm():
    print('fade pm')
    key = "l"
    keyboard.press(key)
    return 'fade pm', 200

@app.route('/bcgwipes')
def get_bcgwipes():
    print('bcg wipes')
    key = "j"
    keyboard.press(key)
    return 'bcg wipes', 200

@app.route('/rmhalffade')
def get_rmhalffadee():
    print('rm half fade')
    key = "h"
    keyboard.press(key)
    return 'rm half fade', 200

@app.route('/rmbhalffade')
def get_rmbhalffade():
    print('rmb half fade')
    key = "y"
    keyboard.press(key)
    return 'rmb half fade', 200

@app.route('/fadegy')
def get_fadegy():
    print('fade gy')
    key = "i"
    keyboard.press(key)
    return 'fade gy', 200

@app.route('/bcwave')
def get_bcwave():
    print('bc wave')
    key = "o"
    keyboard.press(key)
    return 'bc wave', 200

@app.route('/fadeyg')
def get_fadeyg():
    print('fadeyg')
    key = "p"
    keyboard.press(key)
    return 'fadeyg', 200

@app.route('/bluetoblackfade')
def get_bluetoblackfade():
    print('blue to black fade')
    key = "["
    keyboard.press(key)
    return 'blue to black fade', 200

@app.route('/fadeyb')
def get_fadeyb():
    print('fade yb')
    key = "]"
    keyboard.press(key)
    return 'fade yb', 200

@app.route('/fadeyw')
def get_fadeyw():
    print('fade yw')
    key = "\\"
    keyboard.press(key)
    return 'fade yw', 200

@app.route('/bmtrainright')
def get_bmtrainright():
    print('bm train right')
    key = "-"
    keyboard.press(key)
    return 'bm train right', 200

@app.route('/bmtrainleft')
def get_bmtrainleft():
    print('bm train left')
    key = "*"
    keyboard.press(key)
    return 'bm train left', 200

@app.route('/bmwipe')
def get_bmwipe():
    print('bm wipe')
    key = "`"
    keyboard.press(key)
    return 'bm wipe', 200

@app.route('/fadeoy')
def get_fadeoy():
    print('fade oy')
    key = "~"
    keyboard.press(key)
    return 'fade oy', 200

@app.route('/bcalt')
def get_bcalt():
    print('BC Alt')
    key = "!"
    keyboard.press(key)
    return 'BC Alt', 200

@app.route('/rmalt')
def get_rmalt():
    print('RM Alt')
    key = "@"
    keyboard.press(key)
    return 'RM Alt', 200

@app.route('/bmalt')
def get_bmalt():
    print('BM Alt')
    key = "#"
    keyboard.press(key)
    return 'BM Alt', 200        

@app.route('/bgalt')
def get_bgalt():
    print('BG Alt')
    key = "$"
    keyboard.press(key)
    return 'BG Alt', 200

@app.route('/gyalt')
def get_gyalt():
    print('gy Alt')
    key = "%"
    keyboard.press(key)
    return 'gy Alt', 200

@app.route('/randomrainbow')
def get_randomrainbow():
    print('random rainbow')
    key = "^"
    keyboard.press(key)
    return 'random rainbow', 200

@app.route('/rainbow')
def get_rainbow():
    print('rainbow')
    key = "&"
    keyboard.press(key)
    return 'rainbow', 200

@app.route('/redwave')
def get_redwave():
    print('red wave')
    key = "("
    keyboard.press(key)
    return 'red wave', 200

@app.route('/goldwave')
def get_goldwave():
    print('gold wave')
    key = ")"
    keyboard.press(key)
    return 'gold wave', 200

@app.route('/greens')
def get_greens():
    print('greens')
    key = "+"
    keyboard.press(key)
    return 'greens', 200

@app.route('/ashypurple')
def get_ashypurple():
    print('ashy purple')
    key = "{"
    keyboard.press(key)
    return 'ashy purple', 200

@app.route('/peach')
def get_peach():
    print('peach')
    key = "}"
    keyboard.press(key)
    return 'peach', 200

@app.route('/blues')
def get_blues():
    print('blues')
    key = ":"
    keyboard.press(key)
    return 'blues', 200

@app.route('/reds')
def get_reds():
    print('reds')
    key = '"'
    keyboard.press(key)
    return 'reds', 200

@app.route('/mint')
def get_mint():
    print('mint')
    key = '<'
    keyboard.press(key)
    return 'mint', 200

@app.route('/lightpurple')
def get_lightpurple():
    print('light purple')
    key = '>'
    keyboard.press(key)
    return 'light purple', 200

@app.route('/bluepurple')
def get_bluepurple():
    print('blue purple')
    key = '?'
    keyboard.press(key)
    return 'blue purple', 200

@app.route('/cyangreen')
def get_cyangreen():
    print('cyan green')
    key = '|'
    keyboard.press(key)
    return 'cyan green', 200

@app.route('/yelloworange')
def get_yelloworange():
    print('yellow orange')
    key = 'Z'
    keyboard.press(key)
    return 'yellow orange', 200

@app.route('/redorange')
def get_redorange():
    print('red orange')
    key = 'X'
    keyboard.press(key)
    return 'red orange', 200

@app.route('/easterwhite')
def get_easterwhite():
    print('easter white')
    key = 'C'
    keyboard.press(key)
    return 'easter white', 200

@app.route('/bluewave')
def get_bluewave():
    print('blue wave')
    key = 'V'
    keyboard.press(key)
    return 'blue wave', 200

@app.route('/4pascals')
def get_4pascals():
    print('4 pascals')
    key = 'B'
    keyboard.press(key)
    return '4 pascals', 200

@app.route('/christmasservice')
def get_christmasservice():
    print('christmas service')
    key = 'N'
    keyboard.press(key)
    return 'christmas service', 200

@app.route('/purpleblues')
def get_purpleblues():
    print('purple blues')
    key = 'M'
    keyboard.press(key)
    return 'purple blues', 200

@app.route('/sunrise')
def get_sunrise():
    print('sunrise')
    key = 'P'
    keyboard.press(key)
    return 'sunrise', 200

@app.route('/easter')
def get_easter():
    print('easter')
    key = 'O'
    keyboard.press(key)
    return 'easter', 200

@app.route('/easterfriday')
def get_easterfriday():
    print('easter friday')
    key = 'J'
    keyboard.press(key)
    return 'easter friday', 200

@app.route('/faderm')
def get_faderm():
    print('fade rm')
    key = 'L'
    keyboard.press(key)
    return 'fade rm', 200

@app.get('/w0')
def get_w0():
    key = 'A'
    keyboard.press(key)
    print('w0')
    return 'w0', 200

@app.get('/w25')
def get_w25():
    key = 'S'
    keyboard.press(key)
    print('w25')
    return 'w25', 200 

@app.get('/w50')
def get_w50():
    key = 'D'
    keyboard.press(key)
    print('w50')
    return 'w50', 200

@app.get('/w75')
def get_w75():
    key = 'F'
    keyboard.press(key)
    print('w75')
    return 'w75', 200 

@app.get('/w100')
def get_w100():
    key = 'G'
    keyboard.press(key)
    print('w100')
    return 'w100', 200 

@app.get('/c0')
def get_c0():
    key = 'Q'
    keyboard.press(key)
    print('c0')
    return 'c0', 200

@app.get('/c25')
def get_c25():
    key = 'W'
    keyboard.press(key)
    print('c25')
    return 'c25', 200 

@app.get('/c50')
def get_c50():
    key = 'E'
    keyboard.press(key)
    print('c50')
    return 'c50', 200

@app.get('/c75')
def get_c75():
    key = 'R'
    keyboard.press(key)
    print('c75')
    return 'c75', 200 

@app.get('/c100')
def get_c100():
    key = 'T'
    keyboard.press(key)
    print('c100')
    return 'c100', 200

@app.get('/kill')
def get_kill():
    key = 'K'
    keyboard.press(key)
    print('kill')
    return 'kill', 200 
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play')  #This route is never accessed! How do we complete this assignment using only 1 template?
def play():
    return render_template('play.html')

@app.route('/play/<num>')
def num(num):
    return render_template('play_num.html', num=int(num))

@app.route('/play/<num>/<color>')
def num_color(num,color):
    return render_template('play_num_color.html', num=int(num), color=str(color))

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',num=3, color='cadetblue')

@app.route('/play')  #This route is never accessed! How do we complete this assignment using only 1 template?
def play():
    return render_template('index.html', num=3, color='cadetblue')

@app.route('/play/<num>')
def num(num = 3):
    return render_template('index.html', num=int(num), color='cadetblue')

@app.route('/play/<int:num>/<string:color>')
def num_color(num=3,color='cadetblue'):
    return render_template('index.html', num=int(num), color=str(color))

if __name__ == '__main__':
    app.run(debug=True)

## To only use 1 template, set default values for arguments passed. Default value of 0 to start with nothing.
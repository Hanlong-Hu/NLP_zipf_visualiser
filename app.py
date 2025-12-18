from flask import Flask, render_template, request, redirect, url_for

import os 

app = Flask(__name__)

@app.route('/')
def home ():
    techs = ['HTML', 'Flask', 'CSS', 'Python']
    name = '30 Days of Python Programming'
    return render_template('home.html', techs=techs, name=name, title='home')

@app.route('/about')
def about():
    name = '30 Days Of Python Programming'
    return render_template('about.html', name = name, title = 'About Us')

@app.route('/post', methods = ['GET', 'POST'])
def post():
    name = 'Text Analyzer'
    if request.method == 'POST':
        return render_template('post.html', name = name, title = name)
    if request.method == 'GET':
        content = request.form['content']
        print(content)
        return redirect(url_for('post'))

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

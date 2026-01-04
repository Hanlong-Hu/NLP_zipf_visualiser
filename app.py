from flask import Flask, render_template, request, redirect, url_for
from services.processor import run_pipeline
from services.steps import filter_alpha_step, lowercase_step, remove_stop_words_step
from services.metrics import get_word_count, get_unique_word_count
import os 

app = Flask(__name__)

@app.route('/')
def home ():
    techs = ['HTML', 'Flask', 'CSS', 'Python']
    name = 'Text Analyzer'
    return render_template('home.html', techs=techs, name=name, title='home')

@app.route('/about')
def about():
    name = 'Text Analyzer'
    return render_template('about.html', name = name, title = 'About Us')

@app.route('/post', methods = ['GET', 'POST'])
def post():
    name = 'Text Analyzer'
    if request.method == 'GET':
        return render_template('post.html', name = name, title = name)
    if request.method == 'POST':
        content = request.form['content']
        
        # Build the pipeline based on toggles
        steps = [filter_alpha_step] # Basic cleaning always
        
        if request.form.get('case_sensitive') != 'on':
            steps.append(lowercase_step)
            
        if request.form.get('remove_stop_words') == 'on':
            steps.append(remove_stop_words_step)
            
        # Process the text
        processed_words = run_pipeline(content, steps)
        
        # Get metrics
        word_count = get_word_count(processed_words)
        unique_word_count = get_unique_word_count(processed_words)
        
        return render_template('post.html', 
                               name=name, 
                               title=name, 
                               content=content, 
                               word_count=word_count,
                               unique_word_count=unique_word_count)
        
        # return redirect(url_for('post'))

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

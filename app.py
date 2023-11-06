from flask import Flask, render_template, request
from processor import postfix, constructTree, evalRegex, generateTransitionTable

app = Flask(__name__)

@app.route('/')
def index():

    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    regexp = request.form['user_input']
    dot = generateTransitionTable(evalRegex(constructTree(postfix(regexp))))
    dot.write_png(r'C:\Users\priya\Downloads\FLA\static\automaton.png')
    # No need to generate a data URI; we'll serve the image directly
    return render_template('result.html')

if __name__ == '__main__':
    app.run(debug=True)

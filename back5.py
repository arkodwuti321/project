from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('practice5.html')

@app.route('/yes')
def yes_page():
    return render_template('practice6.html')

@app.route('/okay')
def okay_page():
    return render_template('practice7.html')

@app.route('/notokay')
def notokay_page():
    return render_template('notokay.html')

if __name__ == '__main__':
    app.run(debug=True)


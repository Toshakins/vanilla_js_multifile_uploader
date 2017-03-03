from flask import (Flask, render_template, request)
from flask import redirect
from flask import url_for

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        print(request.files.getlist('doc'))
        return redirect(url_for('posted'))
    return render_template('form_page.html')


@app.route('/posted')
def posted():
    return 'You redirected here, lol'


if __name__ == '__main__':
    app.run()

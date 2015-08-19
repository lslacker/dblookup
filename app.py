__author__ = 'LMai'
from flask import Flask, render_template, g, request, flash, redirect, url_for, session
from mssqlwrapper import DB, TempTable
from forms import SearchForm
import utils

app = Flask(__name__)
app.config.from_pyfile('config.py')


@app.before_request
def before_request():
    g.db = DB.from_connection_string(app.config['CONNECTION_STRINGS'])


@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    del db


@app.route('/view/<name>')
def view(name):
    definition = utils.get_definition(g.db, name)
    return render_template('view_def.html', name=definition)


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = SearchForm()

    if request.method == 'POST':
        if form.validate():
            print(form.query.data)
            data = utils.find_me(g.db, form.query.data)
            for a in data:
                print(a
                      )
            session['data'] = data
            return redirect(url_for('index'))
    return render_template('index.html', form=form, data=session.get('data'))

if __name__ == '__main__':
    app.run(debug=True)

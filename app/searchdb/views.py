__author__ = 'LMai'
from flask import render_template, g, request, redirect, url_for, session
from . import searchdb
from .forms import SearchForm
from app import utils


@searchdb.route('/view/<name>')
def view(name):
    definition = utils.get_definition(g.db, name)
    return render_template('view_def.html', name=definition)


@searchdb.route('/', methods=['GET', 'POST'])
@searchdb.route('/index', methods=['GET', 'POST'])
def index():
    form = SearchForm()

    # get all databases
    if request.method == 'POST':
        if form.validate():
            data = utils.find_me(g.db, form.query.data)
            for row in data:
                print(row)
            session['data'] = data
            return redirect(url_for('searchdb.index'))
    return render_template('index.html', form=form, data=session.get('data'))

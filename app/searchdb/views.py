__author__ = 'LMai'
from flask import render_template, g, request, redirect, url_for, session
from app.searchdb import searchdb
from app.searchdb.forms import SearchForm
from app import utils


@searchdb.route('/view/<name>')
def view(name):
    definition = utils.get_definition(g.db, name)
    return render_template('view_def.html', name=definition)


@searchdb.route('/', methods=['GET', 'POST'])
@searchdb.route('/index', methods=['GET', 'POST'])
def index():
    form = SearchForm()

    if request.method == 'POST':
        if form.validate():
            print(form.query.data)
            #data = utils.find_me(g.db, form.query.data)
            #session['data'] = data
            return redirect(url_for('searchdb.index'))
    return render_template('index.html', form=form, data=None)

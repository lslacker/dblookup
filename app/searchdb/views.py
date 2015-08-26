__author__ = 'LMai'
from flask import render_template, g, request, redirect, url_for, session
import json
from . import searchdb
from .forms import SearchForm
from app import utils
from manage import app
from mssqlwrapper import DB


@searchdb.route('/view/<schema>/<name>')
def view(schema, name):
    g.db = DB.from_connection_string(app.config['CONNECTION_STRING'].format(server=session.get('server'), database=schema))
    definition = utils.get_definition(g.db, name)
    return render_template('view_def.html', name=definition)


@searchdb.route('/', methods=['GET', 'POST'])
@searchdb.route('/index', methods=['GET', 'POST'])
def index():
    form = SearchForm(server=request.cookies.get('server') or app.config['SERVER']
                      , databases=request.cookies.get('databases') or app.config['DATABASES']
                      , query=request.cookies.get('query')
                      , containing_text=request.cookies.get('containing_text'))

    # get all databases
    if request.method == 'POST':
        if form.validate():
            databases = form.databases.data.split(",")
            main_database = databases[0]   # with sql server, you can access other databases using database.dbo.tables
            g.db = DB.from_connection_string(app.config['CONNECTION_STRING'].format(server=form.server.data
                                                                                    , database=main_database))
            data = utils.find_me(g.db, form.query.data, databases, form.containing_text.data)

            redirect_to_index = redirect(url_for('searchdb.index'))
            response = app.make_response(redirect_to_index)
            # store form values in cookie
            # for redirect to remember
            response.set_cookie('server', value=form.server.data)
            response.set_cookie('databases', value=form.databases.data)
            response.set_cookie('query', value=form.query.data)
            response.set_cookie('containing_text', value='1' if form.containing_text.data else '')
            response.set_cookie('data', value=json.dumps(data))
            return response

    return render_template('index.html', form=form
                           , data=json.loads(request.cookies.get('data')) if request.cookies.get('data') else None)

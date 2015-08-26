__author__ = 'LMai'


def find_me(db, query, databases, containing_text):

    sub_query = '''\
    SELECT '{database}' as dbname, OBJECT_NAME(object_id, db_id('{database}')) as name, [definition]
    FROM {database}.sys.sql_modules
    '''

    sub_queries = [sub_query.format(database=database.strip()) for database in databases]


    search_query = '''
    with t1 as (
        {sub_queries}
    )
    select * from t1
    where {field} like '%{query}%'
    order by dbname, name
    '''.format(query=query, sub_queries='\nUNION\n'.join(sub_queries), field='definition' if containing_text else 'name')

    data = db.get_data(search_query)

    return [(row[0], row[1]) for row in data]


def get_definition(db, name):
    search_query = '''
    with t1 as (

        SELECT OBJECT_NAME(object_id) as name, [definition]
        FROM sys.sql_modules

    )
    select definition from t1
    where name = ?
    '''
    definition = db.get_one_value(search_query, name)

    return definition
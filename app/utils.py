__author__ = 'LMai'


def find_me(db, query):
    search_query = '''
    with t1 as (

        SELECT 'LonsecLogin' as dbname, OBJECT_NAME(object_id) as name, [definition] FROM sys.sql_modules

    )
    select * from t1
    where name like '%{query}%'
    order by name
    '''.format(query=query)
    print(search_query)
    data = db.get_data(search_query)
    return [(row[0], row[1]) for row in data]


def get_definition(db, name):
    search_query = '''
    with t1 as (

        SELECT 'LonsecLogin' as dbname, OBJECT_NAME(object_id) as name, [definition] FROM sys.sql_modules

    )
    select definition from t1
    where name = ?
    '''
    definition = db.get_one_value(search_query, name)

    return definition
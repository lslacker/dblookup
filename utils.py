__author__ = 'LMai'


def find_me(db, query):
    search_query = '''
        with t1 as (
    SELECT OBJECT_NAME(object_id) as name, [definition] FROM sys.sql_modules
    )
    select * from t1
    where name like '%{query}%'
    '''.format(query=query)
    data = db.get_data(search_query)
    #for row in data:
    #    print(row)
    return [row[0] for row in data]


def get_definition(db, name):
    search_query = '''
        with t1 as (
    SELECT OBJECT_NAME(object_id) as name, [definition] FROM sys.sql_modules
    )
    select definition from t1
    where name = ?
    '''
    definition = db.get_one_value(search_query, name)

    return definition
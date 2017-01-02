# @author : coenni
# @date   : Jan 03 2017
# @brief  : a simple application to migrate database from pg to mysql

import os, pprint
from sqlalchemy import create_engine, exc
from sqlalchemy.orm import sessionmaker

model_file = 'db.py'
model_file_parse = 'db2.py'
db_name = 'socarho'

def clean_next_val():
    with open(model_file, "rt") as fin:
        with open(model_file_parse, "wt") as fout:
            for line in fin:
                if 'server_default' in line:
                    line = line.split(', server_default', 1)[0] + ')\n'
                fout.write(line)


def create_mysql():
    engine = create_engine('mysql+pymysql://username_mysql:password_mysql@127.0.0.1:3306')
    connection = engine.connect()
    result_create = connection.execute("create database IF NOT EXISTS "+db_name)
    connection.close()
    engine = create_engine('mysql+pymysql://username_mysql:password_mysql@127.0.0.1:3306/'+db_name)
    connection = engine.connect()
    try:
        import db2
        db2.Base.metadata.create_all(engine)
    except exc.SQLAlchemyError as err:
        print("Unexpected error:", err)


def get_class_by_tablename(tablename):
  """Return class reference mapped to table.

  :param tablename: String with name of table.
  :return: Class reference or None.
  """
  import db2
  for c in db2.Base._decl_class_registry.values():
    if hasattr(c, '__tablename__') and c.__tablename__ == tablename:
      return c


def move_data():
    engine_pg = create_engine('postgresql://postgres:rootroot@192.168.0.205:5432/ICM_DB_K_New')
    engine_pg.connect()
    Session_pg = sessionmaker(bind=engine_pg)
    session_pg = Session_pg()
    import db2
    for table in db2.metadata.tables:
        print(table)
        table_class = get_class_by_tablename(table)
        result_pg = session_pg.query(table_class).all()
        engine_mysql = create_engine('mysql+pymysql://root:timetodo@127.0.0.1:3306/socarho')
        engine_mysql.connect()
        Session_mysql = sessionmaker(bind=engine_mysql)
        session_mysql = Session_mysql()
        for row in result_pg:
            session_mysql.merge(row)
            pprint.pprint(row)
        session_mysql.commit()
        print(table+' finished')


os.system('sqlacodegen postgresql://postgres:rootroot@192.168.0.205/ICM_DB_K_New --outfile '+model_file)
clean_next_val()
create_mysql()
move_data()
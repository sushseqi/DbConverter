# <h1>DbConverter<h1> is simple tool to migrate database from PostgreSQL to mysql developed by me & teammate Tarlan.

It has three steps:
Firstly, it generates models from pg tables using sqlacodegen library and sqlalchemy technology.(<b>Models generation</b>)
In second step, with simple string replacing it arranges models suitable for mysql and generates schema and tables from models.(<b>DDL</b>)
And finally in the last step, it moves data information from pg to mysql by selecting rows from mysql, and iterating cursor 
and row by row saving information in newly created mysql tables.(<b>DML</b>)

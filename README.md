# <h1>DbConverter</h1> <h4>is simple tool to migrate database from PostgreSQL to MySQL developed by me & teammate Tarlan.</h4>

It has three steps:
<br/>Firstly, it generates models from pg tables using sqlacodegen library and sqlalchemy technology.(<b>Models generation</b>)
<br/>In second step, with simple string replacing it arranges models suitable for MySQL and generates schema and tables from models.(<b>DDL</b>)
<br/>And finally in the last step, it moves data information from pg to mysql by selecting rows from mysql, and iterating cursor 
and row by row saving information in newly created mysql tables.(<b>DML</b>)

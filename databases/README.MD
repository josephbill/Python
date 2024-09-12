### Databases 
- structured : (table format arrangement (rows/columns)) collections of organized data stored in tables where the tables are related. Data is easily accessed , managed , updated and retrieved.  

### Key Concepts 
1. Data : raw facts and figures stored in databases 
2. DBMS : software tools that enables the creation, maintenance and management of databases 
: RDBMS (MySQL,SQlite,PostgreSQL, Oracle, SQL Server) / NoSQL, (firebase (nodes: key-value), MongoDB, Cassandra, Redis ) , In-memory db : data is stored in RAM , Redis , Distributed databases : Google spanner 
3. Tables : each table represents a collection of related data 
4. Fields (columns of the table) : In ORM (OOP) fields = attributes 
5. Records (rows of the table)
6. Primary Key : A unique identifier for each record in the table (id attribute)
7. Foriegn Keys : This is a field in a table that creates the relationships between two tables , 
users -> id, name 
posts -> id, content , user_id (PRIMARY KEY RECORD OF THE USERS TABLE)
8. Queries : requests to DBMS , (SQL (structured query language)) : CRUD 
9. Indexes : Data structures that improve the speed of data retrieval operations on a db table 
10. Relationships : Logical connections between tables in a db , defined using keys 

### Functions 
1. Data storage , retrieval, and manipulations 
2. Concurrency : handling multiple users accessing data simultaneously
3. Data integrity : ensure accuracy and consistency of data 
4. Security : Control access of the database via user permissions 


### SQL 
standard language for interacting with relational dbs.  
- create tables and databases 
- insert records in tables 
- update or modify existing data 
- delete data 
- Join tables to retrieve related data 
- Enforce data integrity (constraints) (PK, FK,UNIQUE)

### KEY SQL OPERATIONS 
- DDL (Data definition language) : SQL Query commands that manipulate the structure of our dbs
CREATE , ALTER , DROP (delete db tables , databases)
- DML (data manipulation language) : SQL Query commands to manipulate data in the db. 
INSERT , SELECT , UPDATE , DELETE , GROUP_BY , WHERE 
- DQL (data query language ) : SELECT 
- DCL (data control language) : SQL commands that grant control over access to data in db 
GRANT , REVOKE 

### ORM 
Object Relational Mapping 
A programming technique used to map db tables to python classes , Instead of writing raw SQL queries we use python objects to interact to our dbs 

1. Objects have attributes , blueprints methods 
Objects - represents 'entities'-> tables in our application 
2. Relational tables in db , Corressponds to objects , with rows representing individual objects and columns representing attributes to these objects 

ORM will abstract away SQL, allows us to interact with db using python code instead of SQL raw commands. 





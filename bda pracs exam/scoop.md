# Scoop commands

1. `mysql -u root -p root`
2. ```
    >show databases;
    >use db;
    >create table demo(id int primary key, name varchar(20));  
    >insert into demo values(1, 'anam')
    >select * from demo;
    >grant all privileges *.* to 'root'@'localhost'
    ```
3. `sqoop import --connect jdbc:mysql://127.0.0.1:3306/db --username root --password root --table demo -m 1`
4. `hdfs dfs -cat /demo/output_file_name`

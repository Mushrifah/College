## Directly get the program by using:
1. For largest: `curl -o mm.java https://transfer.sh/PHgkP/Mainmapper.java`
2. For wordcount: `curl -o wct.java https://transfer.sh/4q8Fi/wordcount.java`
3. For Bloom Filter: `curl -o bf.py https://transfer.sh/M4xfL/bloom.py`

# steps to execute hadoop programs
1. `su -root` <br>
2. `export CLASSPATH='hadoop classpath'`<br>
3. Make a directory with wordcount and in it there are 3 folders input- data, class-executed file and wordcount.java file<br>
4. `javac -d /class /prg.java`<br>
5. `jar -cvf filename -C /class/ .`<br>
6. `start-all.sh` and `jps`<br>
7. `hdfs dfs -mkdir /wordount` `hdfs dfs -mkdir /wordcount/input` <br>
8. `hdfs dfs -copyFromLocal /input.txt /wordcount/input`<br>
9. `hadoop jar /jarfile main_class_name /wordcount/input /wordcount/output`<br>
10. `hadoop dfs -cat wordcount/output/part-m-00000`<br>

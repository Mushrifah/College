# Hadoop commands

## Hadoop on ubuntu:
To first start using hadoop on ubuntu type the following commands as shown below: <br>
1. Format the namenode:  `$hdfs namenode -format`<br>
2. Start hadoop: `$start-dfs.sh` `$start-yarn.sh` or use `$start-all.sh`<br>
3. check working of all components: `$jps`<br>

## List of Hadoop Commands
1. `$hdfs fsck /` is used to check health of hadoop file system<br>
2. `$hdfs dfs -ls /` is used to display list of files<br>
3. `$hdfs dfs -touchz /dir/file.txt` is used to create a file in hdfs <br>
4. `$hdfs dfs -mkdir /` is used to make a directory in hdfs<br>
5. `$hdfs dfs -copyToLocal /mush/a.txt /home/Documents` is used to copy from hdfs to local file system<br>
6. `$hdfs dfs -copyFromLocal /home/Documents/a.txt /mush` is used to copy from local to hdfs<br>
7. `$hdfs dfs -put /local_src /hdfs_dest` is used to copy from local to hdfs<br> 
8. `$hdfs dfs -get /hdfs_src /local-dest` is used to copy from hdfs to local<br>
9. `$hdfs dfs -count /mush` is used to count no. of dirs, files or bytes in hdfs<br>
10. `$hdfs dfs -cp /src /dest` is used to copy files within hdfs<br>
11. `$hdfs dfs -rm /path`  is used to remove file from hdfs <br>
12. `$hdfs dfs -rm -r /path` is used to remove dir from hdfs  <br>
13. `$hdfs dfs -mv /src /dest` is used to move files within hdfs <br>

Note: If permission denied then do `chmod 777 /folder_name`

#Apache Hadoop and Apache Flume environment setup
- Assuming that Apache Hadoop and Flume are installed on a system
- ~/.bashrc has entries for $HADOOP_HOME, $FLUME_HOME
- the user has appropriate permissions for access. (Tip: If something fails, first cross check the permissions.)

##For Hadoop:
- followed the tutorial from tutorials point.
- but their solution didn't workout, I tried everything from blogs to stackoverflow. Got to learn a lot about Hadoop.
- finally downloaded a virtual machine from Coursera, provided by cloudera. I knew where the fault was and looked 
for it specifically. Got it!
- Ultimately, got Hadoop working in a pseudo-distributed mode!
 
 #####Files:
 - *.xml are the changed files, specifying the configuration of Hadoop. There exist a lot of other customization options
 in hadoop but I have sticked to the basics for this project.
 
 #####Commands:
 - formatting namenode: hdfs dfs namenode -format
 - starting/stopping the namenodes, datanodes,nodemanager, resourcemanager:
 start-dfs.sh, start-yarn.sh, start-all.sh, stop-all.sh
 - Hadoop features linux like commands, eg. hadoop dfs -ls, hadoop dfs -cat
 
##For Flume:
- things seemed simpler this time, but problems did creep up.
- did the app setup on twitter to use its API
- Important: *I have stripped my twitter app keys from the files, following twitter guidelines.*
- familiarised myself with Flume concepts of sink, channel, source, avro among others.

#####Files:
- twitter.conf: Configuration of source, sink, channel, etc. is done in this. *The Twitter keys have been removed.*

#####Commands:
- tutorials point failed me again, Then figured out a command which works:
 *$FLUME_HOME/bin/flume-ng agent –conf ./conf/ -f conf/twitter.conf -Dflume.root.logger=DEBUG,console -n TwitterAgent*

# kafka-python-twitter

Step 1:
Make sure that you have necessary python modules and kafka installed

python modules
pip install kafka-python
pip install tweepy

kafka
https://kafka.apache.org/downloads

Step 2:
#start zookeeper
.\bin\windows\zookeeper-server-start.bat .\config\zookeeper.properties

#start kafka
.\bin\windows\kafka-server-start.bat .\config\server.properties

#create topic
kafka-topics.bat --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic SuriyaTweet

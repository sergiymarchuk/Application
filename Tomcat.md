<pre>
1. # wget -c http://apache.volia.net/tomcat/tomcat-8/v8.0.36/bin/apache-tomcat-8.0.36.zip -P /opt/

Change default listening port 
2. # vim /opt/tomcat/conf/server.xml
...  <Connector port="8585" ...
3. # /opt/tomcat/bin/catalina.sh start
4. #lsof -i: 8585
5. #
6. # 

</pre>

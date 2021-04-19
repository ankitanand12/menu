#!/usr/bin/python3
import cgi
import subprocess as sp
import json
print("Conten-type: text/html")
print()

cmd=cgi.FieldStorage()
ip=cmd.getvalue('ip')
fname=cmd.getvalue('fname') 
sp.getoutput('python3 /var/www/cgi-bin/test.py ')
def hdfs():
        hout=sp.getoutput(f"""
echo \'<?xml version=\"1.0\"?>
<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>dfs.name.dir</name>
<value>/{fname}</value>
</property>
</configuration>\' | sudo tee /etc/hadoop/hdfs-site.xml > /dev/null """)

def nformat():
    #fcmd = "echo Y | hadoop namenode -format"
    nformat=sp.getoutput('sudo echo Y | hadoop namenode -format')
    print(nformat)

def nstart():
    #scmd = "hadoop-daemon.sh start namenode"
    sp.getoutput('sudo hadoop-daemon.sh start namenode')
    #print(nstart)

#  LOCAL Name and Data Node "core-site.xml" file

def coresite():
        cout=sp.getoutput(f"""
echo \'<?xml version=\"1.0\"?>
<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>fs.default.name</name>
<value>hdfs://{ip}:9001</value>
</property>
</configuration>\' | sudo tee /etc/hadoop/core-site.xml > /dev/null """)

#coresite()
#hdfs()
#nformat()
#nstart()
#print("Thank you Task Done")

#output=subprocess.getstatusoutput('sudo '+myx)
#status=output[0]
#cmdout=output[1]
#db={"output":cmdout,"status":status}
#js=json.dumps(db)
#print(js)

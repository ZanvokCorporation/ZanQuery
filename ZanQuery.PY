import os

print("ZanQuery Technical Preview 4")
print("Zanvok Query ")
print("Zanvok Corporation")
print()
print("*"*20)
print()

def ver():
    print("ZanQuery 1.0 Technical Preview")

def version():
    print("ZanQuery 1.0 Technical Preview")

def v():
    print("ZanQuery 1.0 Technical Preview")


v = "ZanQuery 1.0 Technical Preview"
ver = "ZanQuery 1.0 Technical Preview"
version = "ZanQuery 1.0 Technical Preview"

print()
act_file = open("C:/ZanQuery/Data/Activation/activation.dat","r")
act_file2 = act_file.read()
if act_file2 == "DEAFULT":
    act_core = ""
    while act_core != "exit":
        act_core = input("> ")
        if act_core == "activate":
            print("Activating ZanQuery")
            activate = open("C:/ZanQuery/Data/Activation/activation.dat","r")
            act_read = activate.read()
            if act_read == "DEAFULTTP5":
                print("Product Activated")
                os.system('cd C:/ZanQuery/')
                os.system('del activate.exe')
                os.system('cls')

                ZanQuery = ""
                while ZanQuery != "EXIT":
                    ZanQuery = input("ZanQuery> ").upper()
                    if ZanQuery == "VER" or ZanQuery == "VERSION" or ZanQuery == "V":
                        print()
                        print("Zanvok Query Language 1.0")
                        print("Technical Preview")
                        print()
                        print("*"*20)
                        print("This product is only for Zanvok Insiders, and therefore cannot share this build to others")
                        print()

                    elif  ZanQuery == "QUERY.DATABASE.SHOW" or ZanQuery == "SHOW DATABASES" or ZanQuery == "SHOW CREATED DATABASES" or ZanQuery == "DISPLAY DATABASES" or ZanQuery == "QUERY.DATABASE.DISPLAY":
                        print("ZanQuery>DATABASES>")
                        file_show = open("C:\ZanQuery\Data\ZanQuery.dat","r")
                        print()
                        print(file_show.read())
                        print()

                    elif ZanQuery == "CLS" or ZanQuery == "CLEAR":
                        os.system('cls')

                    elif ZanQuery == "CMD":
                        os.system('cmd')

                    elif ZanQuery == "":
                        print()

                    elif ZanQuery == " ":
                        print()

                    elif ZanQuery == "   ":
                        print()

                    elif "                                                                                                                 " in ZanQuery:
                        print()

                    elif ZanQuery == "EXIT" or ZanQuery == "QUIT":
                        print("GoodBye!")
                        break

                    elif ZanQuery == "README":
                        os.system('cd /')
                        os.system('cd C:/ZanQuery')
                        os.system('readme.pdf')

                    elif ZanQuery == "ABOUT":
                        print("Zanvok Query Language")
                        print("Gautham Nair")
                        print("Zanvok Corporation")

                    elif ZanQuery == "ZDB":
                        import mysql.connector
                        import os
                        print("ZanvokDB 1.0 Beta")
                        print("Interface for RDBMS(Client/Server)")
                        print("Supported and tested on MySQL and MariaDB")
                        print("=" * 45)
                        print()
                        mydb = mysql.connector.connect(
                            host = input("Enter host: "),
                            user = input("Enter user: "),
                            password = input("Enter your password: "),
                            database = input("Connect a DataBase if you want: ")
                        )


                        mycursor = mydb.cursor()
                        command = ""
                        while command != "quit":
                            command = input("ZanvokDB> ")
                            if command == "zdb help":
                                print("Use basic and general SQL commands")
                                print("ZanvokDB uses MySQL as its base")
                            elif command == "zdb version":
                                print("ZanvokDB v1.0 BETA")
                                print("Zanvok Corporation")
                                print("=" * 10)
                                print("MySQL Python Connector")
                            elif command == "shell":
                                print("Shell under development")
                            elif command == "ping":
                                os.system('ping localhost')
                            elif command == "db":
                                print("Popular DBMSs and RDBMs")
                                print("\t PostgreSQL")
                                print("\t MariaDB")
                                print("\t MySQL")
                                print("\t MongoDB")
                                print("\t Microsoft SQL Server")
                                print("\t Microsoft Access")
                                print("\t LibreOffice/OpenOffice/ApacheOffice DataBase")
                            elif command == "zdb developers" or command == "zdb developer":
                                print("Gautham Nair")
                            elif command == "commit":
                                mydb.commit()
                                print(mycursor.rowcount, "record(s) affected")
                            elif command == "zdb":
                                print("Available ZanvokDB commands:")
                                print("\t 1) 'zdb help' - This displays ZanvokDB Help")
                                print("\t 2) 'zdb version' - This displays the ZanvokDB version")
                                print("\t 3) 'quit' - Quits the ZanvokDB")
                                print("\t 4) 'exit' - Quits the ZanvokDB")
                            elif command == "exit":
                                break
                            elif command == "quit":
                                break
                            elif command == "cmd":
                                cmd = ""
                                while cmd != "quit":
                                    cmd = input("> ")
                                    if cmd == "quit":
                                        break
                                    os.system(cmd)
                            else:
                                mycursor.execute(command)

                                for x in mycursor:
                                    print(x)

                    elif ZanQuery == "DEVELOPER":
                        print("Gautham Nair")
                        print("Zanvok Corporation")

                    elif ZanQuery == "HELP":
                        print()
                        print("*"*20)
                        print("ZanQuery 1.0 Help")
                        print("*"*20)
                        print()
                        print("ZanQuery Commands")
                        print()
                        print("QUERY.DATABASE.SHOW")
                        print("QUERY.DATABASE.DISPLAY")
                        print("QUERY.DATABASE.CREATE")
                        print("QUERY.DATABASE.TABLE.CREATE")
                        print("VER")
                        print("VERSION")
                        print("V")
                        print("ABOUT")
                        print("DEVELOPER")
                        print("CLS")
                        print("EXIT")
                        print("QUIT")
                        print()

                    elif ZanQuery == "CREATE DATABASE" or ZanQuery == "INIT DATABASE" or ZanQuery == "INITIALIZE DATABASE" or ZanQuery == "QUERY.DATABASE.CREATE":
                        create_dbs = input("ZanQuery.DATABASE.CREATE.NAME> ")
                        create_db_dat = "\n"+create_dbs
                        create_dbc = "C:/ZanQuery/DB/"+create_dbs+".ZanQuery"
                        file = open(create_dbc,"w")
                        file.close()
                        file2 = open("C:\ZanQuery\Data\ZanQuery.DAT","a")
                        file2.write(create_db_dat)
                        file2.close()
                        print("DataBase ",create_dbs," created successfully..")
                        file.close()

                    elif ZanQuery == "QUERY.DATABASE.TABLE.CREATE" or ZanQuery == "CREATE TABLE":
                        db_select = input("Select Database: ")
                        db_use = "C:/ZanQuery/DB/"+db_select+".ZanQuery"
                        table_file = open(db_use,"a")
                        table_format = str("+----------------------------------+ \n | "+ db_use+ " |")
                        table_file.write(table_format)
                        table_file.close()
                        table_file2 = open(db_use,"a")
                        table_file3 = input("Enter Columns: ")
                        table_file2.write(table_file3)
                        table_file2.close()

                    elif ZanQuery == "QUERY.DATABASE.CONTENT.SHOW" or ZanQuery == "QUERY.DATABASE.CONTENT.DISPLAY" or ZanQuery == "SHOW DATABASE CONTENTS":
                        db_content = input("Enter Database Name: ")
                        db_content2 = db_content+".ZanQuery"
                        db_view = open(db_content2,"r")
                        db_view.read()
                        print()
                        print(db_view.read())
                        print()

                    elif "#" in ZanQuery:
                        print()

                    elif "/*" in ZanQuery:
                        print()

                    elif "--" in ZanQuery:
                        print()

                    elif "<>" in ZanQuery:
                        print()

                    elif "<" in ZanQuery:
                        print()

                    elif ">" in ZanQuery:
                        print()

                    elif ZanQuery == "PING":
                        os.system('ping localhost')

                    else:
                        print()
                        print("You have an error in your Query syntax: check the manual that corresponds to your ZanQuery version for the right syntax to use..!")
                        print()

            else:
                print("Product Not Vaild / Installed ")

        else:
            print("Invalid!")
else:
    os.system('cd /')
    os.system('cd C:/ZanQuery')
    os.system('del activate.exe')
    ZanQuery = ""
    while ZanQuery != "EXIT":
        ZanQuery = input("ZanQuery> ").upper()
        if ZanQuery == "VER" or ZanQuery == "VERSION" or ZanQuery == "V":
            print()
            print("Zanvok Query Language 1.0")
            print("Technical Preview")
            print()
            print("*"*20)
            print("This product is only for Zanvok Insiders, and therefore cannot share this build to others")
            print()

        elif  ZanQuery == "QUERY.DATABASE.SHOW" or ZanQuery == "SHOW DATABASES" or ZanQuery == "SHOW CREATED DATABASES" or ZanQuery == "DISPLAY DATABASES" or ZanQuery == "QUERY.DATABASE.DISPLAY":
            print("ZanQuery>DATABASES>")
            file_show = open("C:\ZanQuery\Data\ZanQuery.dat","r")
            print()
            print(file_show.read())
            print()

        elif ZanQuery == "CLS" or ZanQuery == "CLEAR":
            os.system('cls')

        elif ZanQuery == "CMD":
            os.system('cmd')

        elif ZanQuery == "":
            print()

        elif ZanQuery == " ":
            print()

        elif ZanQuery == "   ":
            print()

        elif "                                                                                                                 " in ZanQuery:
            print()

        elif ZanQuery == "EXIT" or ZanQuery == "QUIT":
            print("GoodBye!")
            break

        elif ZanQuery == "README":
            os.system('cd /')
            os.system('cd C:/ZanQuery')
            os.system('readme.pdf')

        elif ZanQuery == "ABOUT":
            print("Zanvok Query Language")
            print("Gautham Nair")
            print("Zanvok Corporation")

        elif ZanQuery == "ZDB":
            import mysql.connector
            import os
            print("ZanvokDB 1.0 Beta")
            print("Interface for RDBMS(Client/Server)")
            print("Supported and tested on MySQL and MariaDB")
            print("=" * 45)
            print()
            mydb = mysql.connector.connect(
                host = input("Enter host: "),
                user = input("Enter user: "),
                password = input("Enter your password: "),
                database = input("Connect a DataBase if you want: ")
            )


            mycursor = mydb.cursor()
            command = ""
            while command != "quit":
                command = input("ZanvokDB> ")
                if command == "zdb help":
                    print("Use basic and general SQL commands")
                    print("ZanvokDB uses MySQL as its base")
                elif command == "zdb version":
                    print("ZanvokDB v1.0 BETA")
                    print("Zanvok Corporation")
                    print("=" * 10)
                    print("MySQL Python Connector")
                elif command == "shell":
                    print("Shell under development")
                elif command == "ping":
                    os.system('ping localhost')
                elif command == "db":
                    print("Popular DBMSs and RDBMs")
                    print("\t PostgreSQL")
                    print("\t MariaDB")
                    print("\t MySQL")
                    print("\t MongoDB")
                    print("\t Microsoft SQL Server")
                    print("\t Microsoft Access")
                    print("\t LibreOffice/OpenOffice/ApacheOffice DataBase")
                elif command == "zdb developers" or command == "zdb developer":
                    print("Gautham Nair")
                elif command == "commit":
                    mydb.commit()
                    print(mycursor.rowcount, "record(s) affected")
                elif command == "zdb":
                    print("Available ZanvokDB commands:")
                    print("\t 1) 'zdb help' - This displays ZanvokDB Help")
                    print("\t 2) 'zdb version' - This displays the ZanvokDB version")
                    print("\t 3) 'quit' - Quits the ZanvokDB")
                    print("\t 4) 'exit' - Quits the ZanvokDB")
                elif command == "exit":
                    break
                elif command == "quit":
                    break
                elif command == "cmd":
                    cmd = ""
                    while cmd != "quit":
                        cmd = input("> ")
                        if cmd == "quit":
                            break
                        os.system(cmd)
                else:
                    mycursor.execute(command)

                    for x in mycursor:
                        print(x)

        elif ZanQuery == "DEVELOPER":
            print("Gautham Nair")
            print("Zanvok Corporation")

        elif ZanQuery == "HELP":
            print()
            print("*"*20)
            print("ZanQuery 1.0 Help")
            print("*"*20)
            print()
            print("ZanQuery Commands")
            print()
            print("QUERY.DATABASE.SHOW")
            print("QUERY.DATABASE.DISPLAY")
            print("QUERY.DATABASE.CREATE")
            print("QUERY.DATABASE.TABLE.CREATE")
            print("VER")
            print("VERSION")
            print("V")
            print("ABOUT")
            print("DEVELOPER")
            print("CLS")
            print("EXIT")
            print("QUIT")
            print()

        elif ZanQuery == "CREATE DATABASE" or ZanQuery == "INIT DATABASE" or ZanQuery == "INITIALIZE DATABASE" or ZanQuery == "QUERY.DATABASE.CREATE":
            create_dbs = input("ZanQuery.DATABASE.CREATE.NAME> ")
            create_db_dat = "\n"+create_dbs
            create_dbc = "C:/ZanQuery/DB/"+create_dbs+".ZanQuery"
            file = open(create_dbc,"w")
            file.close()
            file2 = open("C:\ZanQuery\Data\ZanQuery.DAT","a")
            file2.write(create_db_dat)
            file2.close()
            print("DataBase ",create_dbs," created successfully..")
            file.close()

        elif ZanQuery == "QUERY.DATABASE.TABLE.CREATE" or ZanQuery == "CREATE TABLE":
            db_select = input("Select Database: ")
            db_use = "C:/ZanQuery/DB/"+db_select+".ZanQuery"
            table_file = open(db_use,"a")
            table_format = str("+----------------------------------+ \n | "+ db_use+ " |")
            table_file.write(table_format)
            table_file.close()
            table_file2 = open(db_use,"a")
            table_file3 = input("Enter Columns: ")
            table_file2.write(table_file3)
            table_file2.close()

        elif ZanQuery == "QUERY.DATABASE.CONTENT.SHOW" or ZanQuery == "QUERY.DATABASE.CONTENT.DISPLAY" or ZanQuery == "SHOW DATABASE CONTENTS":
            db_content = input("Enter Database Name: ")
            db_content2 = db_content+".ZanQuery"
            db_view = open(db_content2,"r")
            db_view.read()
            print()
            print(db_view.read())
            print()

        elif "#" in ZanQuery:
            print()

        elif "/*" in ZanQuery:
            print()

        elif "--" in ZanQuery:
            print()

        elif "<>" in ZanQuery:
            print()

        elif "<" in ZanQuery:
            print()

        elif ">" in ZanQuery:
            print()

        elif ZanQuery == "PING":
            os.system('ping localhost')

        else:
            print()
            print("You have an error in your Query syntax: check the manual that corresponds to your ZanQuery version for the right syntax to use..!")
            print()

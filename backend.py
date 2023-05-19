import sqlite3


#function to create a new table in database
def crt_table():
    connect = sqlite3.connect("students.db")
    cursor = connect.cursor()
    c = ""
    
    while(c != 'n'):
        n = input("Name for new table: ")
        num = int(input("How many columns do you want in your table: "))
        l1 = []
                
        for i in range(num):
            l1.append( input(f"Enter column {i+1} name:"))
        
        s1 = f'CREATE TABLE {n} (\n'
        
        s2 = ""
        
        for item in range(len(l1)):
            if item < (len(l1) - 1):
                s2 = s2 +  "\t" + f"{l1[item]}" + ",\n"
            else:
                s2 = s2 + "\t" + f"{l1[item]}" + "\n"
        
        s3 = ');'
        
        query = s1 + s2 + s3
        
        cursor.execute(query)
        
        connect.commit()
        c = input("Do you want to add another table: ")
        
    connect.close()


#function to add new records to table in database
def add_data(tb_nm):
    l = get_nm(tb_nm)
    
    connect = sqlite3.connect("students.db")
    cursor = connect.cursor()
    
    c = ""
    
    while(c != 'n'):
        inp = []
        inp2 = []
        for i in range(len(l)):
            inp2.append(input(f"Enter the value for {l[i][0]} column:"))
        
        tu = tuple(inp2)
        inp.append(tu)
            
        #creating a query string
        s1 = f"INSERT INTO {tb_nm} VALUES ("
        s2 = ""
        
        for i in range(len(l)):
            if i < (len(l) - 1):
                s2 = s2 + "?" + ", "
            else:
                s2 = s2 + "?);"
            
        query = s1 + s2

        #executing query
        cursor.executemany(query,inp)  
        connect.commit()
        print("\n")
        c = input("Do you want to add another record? : ")

    
    connect.close()


#function to get column names of specified table
def get_nm(tb_nm):
    connect = sqlite3.connect("students.db")
    cursor = connect.cursor()
    
    query = f"SELECT name FROM pragma_table_info('{tb_nm}')"
    
    cursor.execute(query)
    
    l = cursor.fetchall()
    
    connect.commit()
    connect.close()
    return l


#this function displays the whole table i.e. specified
def show_tb():
    connect = sqlite3.connect("students.db")
    cursor = connect.cursor()
    c = ""
    
    while(c != "n"):
        print("\n\n")
        tb_nm = input("Enter the name of the table you want to see: ")
        l = get_nm(tb_nm)
        
        cursor.execute(f"SELECT * FROM {tb_nm}")
        l1 = cursor.fetchall()
        
        print(f"\nHere is your {tb_nm} table:")

        s1 = ""
        
        for i in range(len(l)):
            s1 = s1 + l[i][0] + "\t\t"
        
        s2 = ""
        
        for i in l1:
            for j in range(len(i)):
                s2 = s2 + i[j] + "\t\t"
            s2 = s2 + "\n"
        
        print(s1) 
        print(s2)
        connect.commit()
        
        c = input("Do you want to see another table: ")
        
    connect.close()


#function to query a database
def query_tb():
    connect = sqlite3.connect("students.db")
    cursor = connect.cursor()
    c = ""
    
    while(c != "n"):
        q = input("Enter the query you want to execute: ")

        cursor.execute(q)
        
        items = cursor.fetchall()
        
        if items:
            print(items)
        
        connect.commit()
        c = input("Do you want to execute another query: ")
        
    connect.close()
    

#function to delete a whole table
def del_tb():
    connect = sqlite3.connect("students.db")
    cursor = connect.cursor()
    c = ""
    
    while(c !='n'):
        tb_nm = input("Name of the table you want to delete: ")
    
        cursor.execute(f"DROP TABLE {tb_nm}")
    
        connect.commit()
        c = input("Do you want to delete another table?")
        
    connect.close()


if __name__ == "__main__":
    crt_table("nothing", [1,2,3,4,5])
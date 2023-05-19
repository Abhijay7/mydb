import backend as bk
import os, time


while(True):
    os.system("cls")
    print("Hello! Admin.\nYou are here to:\n")
    print("""
            1. Create a new table.\n
            2. Add new record to the table.\n
            3. Query a table.\n
            4. Show whole table\n
            5. Drop a table.\n
            ** Press 0 to exit **\n
            *** Use 'y' for yes and 'n' for no ***\n""")

    x = int(input("Enter your choice: "))

    match x:
        case 1:
            bk.crt_table()
            
        case 2:
            tb1 = input("Enter the name of the table in which you want to add record: ")
            bk.add_data(tb1) 
        
        case 3:
            bk.query_tb()
        
        case 4:
            bk.show_tb()
        
        case 5:
            bk.del_tb()
            
        case 0:
            break
            
        case _:
            print("Invalid option")
            time.sleep(5)
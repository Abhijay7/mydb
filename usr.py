import backend as bk
import os, time


while(True):
    os.system("cls")
    print("Hello! User.\nYou are here to:\n")
    print("""
            1. Add new record to the table.\n
            2. Query a table.\n
            3. See whole table\n
            ** Press 0 to exit **\n
            *** Use 'y' for yes and 'n' for no ***\n""")

    x = int(input("Enter your choice: "))

    match x:
        case 1:
            tb1 = input("Enter the name of the table in which you want to add record: ")
            bk.add_data(tb1)
            
            
        case 2:
            bk.query_tb()
        
        case 3:
            bk.show_tb()
            
        case 0:
            break
            
        case _:
            print("Invalid option")
            time.sleep(5)
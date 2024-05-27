import os

print(f"Hello. You are currently at '{os.getcwd()}'.\nYou can create thousands of folders here\n","-- "*20)

def taking_count():
    try:
        m = int(input("Enter Thousands = "))
        if m>9:
            print("Kindly enter upto 9 in thousands\n","-- "*20)
            taking_count()
        n = int(input("Enter Hundreds = "))
        o = int(input("Enter Tens = "))
        p = int(input("Enter Ones = "))
    except:
        print("Ohho..You entered a wrong value. Kindly enter valid integer.\n", "-- "*20)
        return taking_count()
        
    if (m >= 0 and n >= 0 and o >= 0 and p >= 0) and (m < 10 and n < 10 and o < 10 and p < 10):
        folder_count = 1000 * m + 100 * n + 10 * o + p
        if folder_count == 0:
            print("No folder to be created. Kindly enter again.\n", "-- "*20)
            return taking_count()
        else:
            print('Total folders Required =', folder_count)
            return folder_count
    else:
        print("Mis-entered?? Kindly enter digits from 0 to 9\n", "-- "*20)
        return taking_count()

folder_count = taking_count()

def creating_folders(folder_count):
    print(f"Please Wait! {folder_count} folders will be created. Thank you.\n", "-- "*20)
    p_folder_name = input("Enter Parent folder name :")
    
    def parent_child_same_name(p_folder_name):
        proceed = input("Do you want child-folders with the same name? :Y/N\n").strip()

        if proceed in ('Y','y','Yes','yes'):
            os.mkdir(p_folder_name)
            for i in range(folder_count):
                c_folders_name = os.path.join(p_folder_name, f"{p_folder_name} {i+1}")
                os.mkdir(c_folders_name)
        elif proceed in ('N','n','No','no'):
            c_start = input("Ok. Enter Child folders name starts with :")
            os.mkdir(p_folder_name)
            for i in range(folder_count):
                c_folders_name = os.path.join(p_folder_name, f"{c_start} {i+1}")
                os.mkdir(c_folders_name)
        else:
            print("Oops. Kindly enter valid input")
            parent_child_same_name(p_folder_name)
            
    parent_child_same_name(p_folder_name)


def taking_confirmation():
    proceed = input('Confirm : Y/N\n').strip()
    if proceed in ('N','n','No','no'):
        print('No Problem! Kindly re-enter\n')
        global folder_count
        folder_count = taking_count()

        taking_confirmation()
    elif proceed in ('Y','y','Yes','yes'):
        creating_folders(folder_count)
        print(f'Congratulations! {folder_count} folders created at path {os.getcwd()}.')
    else:
        print("Ohho. Kindly enter valid input")
        taking_confirmation()

taking_confirmation()
#AML1214 PYTHON PROJECT - DEVICE MANAGEMENT SYSTEM applying Functions and Files
def view_function(): #VIEW function by RAGHAV
    print('DEVICE LIST CONTENTS ARE:')
    with open("devicelist.txt", 'r') as f:
        lines = f.read()
        print(lines)
#ADD function by VENGIE
def write_to_file(text):
    with open('devicelist.txt', 'a') as file:
        file.writelines('\n' + text)
#ADD function by VENGIE
def add_function():
    with open('devicelist.txt') as file:
        text = input("Add new device NAME and CODE separated by a SPACE: ")
        fileList = file.read().split()
        if text not in fileList:
            fileList.append(text)
            write_to_file(text)
            print('New device {} was ADDED!'.format(text))
            view_function()
        else:
            msg = input('You have entered device {} that is already existed in device list.'
                        'Do you want to continue adding? ')
            if msg == "Yes" or "YES":
                write_to_file(text)
                print('New device {} was ADDED!'.format(text))
            else:
                msg == "No" or "NO"
            print(fileList)
#DELETE function by HETVI, NEIL, VENGIE
def delete_function(string):
    delete = string
    with open("devicelist.txt", "r+") as f:
        mylist = []
        for line in f:
            mylist.append(line.strip())
        if delete in mylist:
            mylist.remove(delete)
            print("Device was DELETED!")
            f.seek(0)
            f.truncate()
            f.write('\n'.join(mylist))
        else:
            print("The device do not exist, or in UPPER/lower case form!")
#Update function by NEIL
def update_function(string):
    to_update = string
    with open("devicelist.txt", 'r+') as f:
        mylist = []
        for line in f:
            mylist.append(line.strip())
        if to_update in mylist:
            while to_update in mylist:
                    index = mylist.index(to_update)
                    update = input("Enter UPDATED device NAME and CODE: ")
                    print("Device was UPDATED!")
                    mylist = mylist[:index] + [update] + mylist[index+1:]
                    f.seek(0)
                    f.truncate()
                    f.write('\n'.join(mylist))
        else:
            print("The device do not exist, or in UPPER/lower case form!")
#RUBYLYN - main, repetition, options, integration and compilation of all functions
def main():
    ans = 'y'
    print('=================Welcome to PYTEAM Device Management System 2022===============')
    print('\t1.  View all devices') #Raghav, github
    print('\t2.	Add a device')      #Vengie
    print('\t3.	Delete a device')   #Hetvi
    print('\t4.	Update a device')   #Neil
    print('\t5.	Exit the program')  #SEARCH for Bashir
    print('===============================================================================')
    while ans.lower() == 'y':
        option = input('Select one option to Execute(1-View, 2-Add, 3-Delete, 4-Update, or 5-Exit): ')
        if option == '1':
            print('=======================VIEWING ALL DEVICES FROM THE FILE=======================')
            view_function()
            ans = input('Do you want to execute again?(y/n):')
        elif option == '2':
            print('=======================ADDING NEW DEVICE TO THE FILE==========================')
            add_function()
            ans = input('Do you want to execute again?(y/n):')
        elif option == '3':
            print('========================DELETING A DEVICE FROM THE FILE========================')
            view_function()
            string1 = input("Enter device NAME and CODE to be DELETED: ")
            delete_function(string1)
            ans = input('Do you want to execute again?(y/n):')
        elif option == '4':
            print('=========================UPDATING A DEVICE IN THE FILE=========================')
            view_function()
            string1 = input("Enter device NAME and CODE to be UPDATED: ")
            update_function(string1)
            ans = input('Do you want to execute again?(y/n):')
        elif option == '5':
            print('.....Program Terminated!!!')
            print('\nGoodbye!THANKS FOR USING PYTEAM\'S DEVICE MANAGEMENT SYSTEM...')
            break
        else:
            print('Invalid Choice! Please choose only 1 to 5 options!!!')
            ans = input('Do you want to execute again?(y/n):')
    else:
        print('\nGoodbye!THANKS FOR USING PYTEAM\'S DEVICE MANAGEMENT SYSTEM...')
    print('Programmed by:\n\tRubylyn Padillo\n\tNeil Discaya\n\tVengie Dinampo\n\tRaghavendra Kavalur\n\tHetvi Patel\n\tBashir Ahmed')
    print('AML1214 - Python Programming Students\nLAMBTON COLLEGE, BIG DATA ANALYTICS ')
    print('Submitted to: DR. RAED KARIM, Spring 2022')

main()



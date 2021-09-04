import re
import os
import no_of_lines
import check_file_present


class Node:
    def __init__(self, ac_no=None, nme=None, ag=None, add=None, ph_no=None, bal=None):
        # def __init__(self):
        self.acc_no = ac_no
        self.name = nme
        self.age = ag
        self.address = add
        self.phone_no = ph_no
        self.balance = bal
        self.next = None


def fetch_name():
    while True:
        nme = input("Enter account holders name :")
        nme = nme.replace(" ", "_")
        if nme.replace("_", "").isalpha():
            break
        else:
            print("Enter a valid name")

    return nme


def fetch_age():
    while True:
        try:
            ages = int(input("Enter the age:"))
            if ages > 0:
                break
            else:
                print("Age should be greater than zero")
        except ValueError:
            print(" Enter number for age")
            continue
    return ages


def fetch_address():
    while True:
        addresses = input("Enter the address:")
        addresses = addresses.replace(" ", "_")
        if addresses.replace("_", "").isalpha():
            break
        else:
            print("Enter a valid address")

    return addresses


def fetch_phone_no():
    while True:
        try:
            ph_no = input("Enter the phone number which starts with 9 and is of 10 digits:")
            pattern = re.compile("(0/91)?[7-9][0-9]{9}")
            match = re.match(pattern, ph_no)
            if match and len(ph_no) == 10:
                break
            else:
                print("Invalid Phone number")
                print("Please enter a valid phone number ")
                continue
        except ValueError:
            print(" Enter number for Phone number ")
            continue
        except TypeError:
            print(" Enter number greater than zero for Phone number ")
            continue
    return ph_no


def read_accounts_from_file():
    file_size = os.path.getsize("bank_record")
    output = check_file_present.check_file("bank_record")
    if output is True:
        print("File is present")
    else:
        print("File not present")

    if file_size < 5:
        print("The file is empty ")
        print("Create new accounts")
    else:
        list1 = []
        #    file = open("bank_record", "r")
        with open("bank_record", "r") as file:
            for line in file:
                list1.clear()
                for word in line.split():
                    list1.append(word)
                my_list.create_account_from_file(int(list1[0]), list1[1], int(list1[2]),
                                                 list1[3], int(list1[4]), int(list1[5]))
            print()
            file.close()


class LinkedList:
    def __init__(self):
        self.head = None

    def display_all(self):
        cur = self.head

        if cur is None:
            print("There are no accounts created")
        else:
            print("ACC_NO  NAME\t   AGE  ADDRESS \t PHONE_NO \t BALANCE")
            while cur is not None:
                print(str(cur.acc_no) + "\t\t" + cur.name.replace("_", " ") +
                      "   " + str(cur.age) + "   " +
                      cur.address.replace("_", " ")
                      + " \t " + str(
                    cur.phone_no) + " \t " +
                      str(cur.balance))
                cur = cur.next

    def create_account(self, acc_num, nme, years, addresses, ph_no, bal):
        new_node = Node(acc_num, nme, years, addresses, ph_no, bal)

        if self.head is None:
            self.head = new_node
            print()
            print("!!!!!!!!!!!!!!!!!!!Account created successfully!!!!!!!!!!!!!!")
            print()
            print("The account number allocated is " + str(acc_num))
            print()
            print("*********************************************************")
            return

        last = self.head

        while last.next:
            last = last.next
        last.next = new_node

        print()
        print("Account created successfully!!!!!!!!!!!!!!")
        print()
        print("The account number allocated is " + str(acc_num))
        print()
        print("********************************"
              "*************************")

    def create_account_from_file(self, acc_num, nme, years, addresses, ph_no, bal):
        new_node = Node(acc_num, nme, years, addresses, ph_no, bal)

        if self.head is None:
            self.head = new_node
            return

        last = self.head

        while last.next:
            last = last.next
        last.next = new_node

    def deposit(self, acc_num, amount):
        print("*************DEPOSIT AMOUNT***************")
        first = self.head

        if self.head is None:
            print("NO ACCOUNTS EXITS!!!!!!!!!!")
            return

        if acc_num <= 0 or amount <= 0:
            print("PLEASE ENTER VALID INPUT!!!!!!!!!!")
            return

        while first is not None and (first.acc_no != acc_num):
            first = first.next

        if first is None:
            print("Account number entered does not exist!!!!!!!!!")
            return

        first.balance = first.balance + amount
        print("Amount deposit successful!!!!!!!!")
        print("Current balance is " + str(first.balance))
        print("*********************************************************")
        return

    def withdraw(self, acc_num, amount):
        print("*************DEPOSIT AMOUNT***************")
        first = self.head

        if self.head is None:
            print("NO ACCOUNTS EXITS!!!!!!!!!!")
            return

        if acc_num <= 0 or amount <= 0:
            print("PLEASE ENTER VALID INPUT!!!!!!!!!!")
            return

        while first is not None and first.acc_no != acc_num:
            first = first.next

        if first is None:
            print("Account number entered does not exist!!!!!!!!!")
            return

        if amount <= first.balance:
            first.balance = first.balance - amount
            print("Withdraw of " + str(amount) + " amount from account "
                  + str(first.acc_no) + " successful!!!!!")
            print()
            print()
            print("Remaining balance is " + str(first.balance) + " !!!!!!!!!!!")

        else:
            print("Insufficient funds cancelling transaction!!!!!!!!!!!!")
            print("*********************************************************")

        return

    def get_account_balance(self, acc_num):
        print("*************Get account balance***************")
        cur = self.head

        if self.head is None:
            return -1

        while cur is not None and cur.acc_no != acc_num:
            cur = cur.next

        if cur is None:
            return -1

        if cur.acc_no == acc_num:
            return cur.balance

        return -1

    def write_to_file(self):
        file = open("bank_record", "w")
        cur = self.head

        if cur is None:
            print("There is nothing to write to file")

        while cur is not None:
            file.write(str(cur.acc_no) + "\t\t" + cur.name + "\t\t" + str(cur.age) + "\t\t" + cur.address + "\t\t" + str(cur.phone_no) + "\t\t" + str(cur.balance) + "\n")
            cur = cur.next


my_list = LinkedList()
my_list.head = None
with open("bank_record", "+a") as fp:
    fp.close()
# check_file_present.check_file("bank_record")
ACCOUNT_NUM = no_of_lines.no_of_lines('bank_record')
# account_number = no_of_lines.no_of_lines('bank_record')
if ACCOUNT_NUM != 0:
    ACCOUNT_NUM += 1
read_accounts_from_file()
while True:
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~MENU~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("1. CREATE ACCOUNT ")
    print("2. VIEW ALL ACCOUNTS ")
    print("3. DEPOSIT AMOUNT ")
    print("4. WITHDRAW AMOUNT ")
    print("5. GET ACCOUNT BALANCE ")
    print("6. EXIT")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    try:
        choice = int(input("Enter your Choice from options 1-6: "))
        if choice == 1:
            if ACCOUNT_NUM == 0:
                ACCOUNT_NUM = 1
                ACC_NO = 1
                # acc_no = 1
            else:
                ACC_NO = ACCOUNT_NUM
            # acc_no = ACCOUNT_NUM

            name = fetch_name()
            age = fetch_age()
            address = fetch_address()
            phone_no = fetch_phone_no()
            BALANCE = 0
            ACCOUNT_NUM = ACCOUNT_NUM + 1
            my_list.create_account(ACC_NO, name, age, address, phone_no, BALANCE)

        elif choice == 2:
            my_list.display_all()

        elif choice == 3:
            acc = int(input("Enter the account number: "))
            amt = int(input("Enter amount to deposit : "))
            my_list.deposit(acc, amt)

        elif choice == 4:
            acc = int(input("Enter the account number: "))
            amt = int(input("Enter amount to withdraw : "))
            my_list.withdraw(acc, amt)

        elif choice == 5:
            acc = int(input("Enter the account number: "))
            account_balance = my_list.get_account_balance(acc)

            if account_balance == -1:
                print("Account number doesnt exist!!!!")
            else:
                print("Account balance is " + str(account_balance) + "!!!!!!")

        elif choice == 6:
            break

        else:
            print("Invalid Choice")
            print("Input correct choice ...(1-6)")

    except NameError:
        print("Input correct choice ...(1-6")

    except ValueError:
        print("Input correct choice ...(1-6)")

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    my_list.write_to_file()

import random

accounts = {}

def strength_check(pwd):
    up = low = spec = num = 0
    specials = "!@#$%^&*()_+-={}[]:;,.><?/"
    for c in pwd:
        if c.isupper() == True:
            up += 1
        elif c.islower() == True:
            low += 1
        elif c.isdigit() == True:
            num += 1
        elif c in specials:
            spec += 1
    stat = [up, low, num, spec]
    if len(pwd) >= 12 and up >= 1 and low >= 1 and spec >= 1 and num >= 1:
        print("Password strength: Strong")
    elif 8 <= len(pwd) <= 11:
        a = 0
        for i in range(4):
            if stat[i] >= 1:
                a += 1
        if a >= 3:
            print("Password strength: Medium")
        else:
            print("Password strength: Weak")
    else:
        print("Password strength: Weak")

def add_account():
    site = input("\nWebsite: ")
    if site in accounts:
        print("Account for this website already exists")
    else:
        usr = input("Username: ")
        pwd = input("Password: ")
        accounts[site] = [usr, pwd]
        strength_check(pwd)

def reveal_pass():
    while True:
        print("\nUse: show <website> to reveal an account or press enter to go to menu.")
        show = input("> ").lower()
        l = show.split()
        if len(l) == 0 or len(l) == 1:
            break
        i = 0
        for key in accounts:
            if l[1] in key:
                i += 1
        if i > 1:
            print()
            j = 1
            results = []
            for key in accounts:
                if l[1] in key:
                    print(f"{j}. {key}")
                    j += 1
                    results.append(key)
            print("\nPlease choose from the results.")
            try:
                choice = int(input("> "))
                for k in range(1, len(results)+1):
                    if choice == k:
                        print(f"\nWebsite: {results[choice-1]}")
                        print(f"Username: {accounts[results[choice-1]][0]}")
                        print(f"Password: {accounts[results[choice-1]][1]}")
            except ValueError:
                pass
        elif i == 0:
            print("No accounts found")
        elif i == 1:
            for key in accounts:
                if l[1] in key.lower():
                    print(f"\nWebsite: {key}")
                    print(f"Username: {accounts[key][0]}")
                    print(f"Password: {accounts[key][1]}")

def view_accounts():
    print("\n"+"="*5+" ACCOUNTS "+"="*5)
    i = 1
    blank = " "
    if len(accounts) == 0:
        print("No accounts found")
    else:
        for key in accounts:
            star = "*"
            print(f"\n{i}. Website: {key}")
            print(f"{blank*(len(str(i))+2)}Username: {accounts[key][0]}")
            print(f"{blank*(len(str(i))+2)}Password: {star*len(accounts[key][1])}")
            i += 1
    reveal_pass()
    
def search_account():
    term = input("\nSearch website: ").lower()
    i = 1
    c = 1
    blank = " "
    if len(accounts) == 0:
        print("No accounts found")
    elif len(term) == 0:
        print("Empty input")
    else:
        print("\nMatches:")
        for key in accounts:
            if term in key.lower():
                i += 1
        if i == 1:
            print("No matches found")
        else:
            for key in accounts:
                if term in key.lower():
                    star = "*"
                    print(f"\n{c}. Website: {key}")
                    print(f"{blank*(len(str(i))+2)}Username: {accounts[key][0]}")
                    print(f"{blank*(len(str(i))+2)}Password: {star*len(accounts[key][1])}")
                    c += 1
            reveal_pass()

def del_account():
    term = input("\nEnter website to delete: ").lower()
    i = 1
    c = 1
    if len(accounts) == 0:
        print("No accounts found")
    else:
        for key in accounts:
            if term in key.lower():
                i += 1
        if i == 1:
            print("No matches found")
        elif i == 2:
            for key in accounts:
                if term in key.lower():
                    print("Website to be deleted: ", key)
            ans = input("Are you sure? (yes/no): ").lower()
            if ans == 'yes':
                del accounts[key]
                print(key, " deleted")
            else:
                pass
        else:
            options = []
            for key in accounts:
                if term in key.lower():
                    print(f"\n{c}. Website: {key}")
                    options.append(key)
                    c += 1
            try:
                option = int(input("\nWhich option number account to delete? Press enter to cancel operation: "))
                if option > 0 and option <= len(options):
                    print(options[option - 1], " deleted")
                    del accounts[options[option - 1]]
            except ValueError:
                pass

def pass_gen():
    l = int(input("\nEnter length for the password: "))
    if l < 12:
        print("Password should be atleast 12 characters long")
    else:
        password = ""
        lows = "abcdefghijklmnopqrstuvwxyz"
        highs = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"    
        nums = "0123456789"
        specials = "!@#$%^&*()_+-={}[]:;,.><?/"
        total = lows + highs + nums + specials
        # to ensure password contains atleast one character of each type
        password += random.choice(lows) + random.choice(highs) + random.choice(nums) + random.choice(specials)
        for i in range(l-4):
            password += random.choice(total)
        print("\nGenerated password:")
        print(password)
    
while True:
    print("\n"+"="*5+" PASSWORD MANAGER "+"="*5)
    print("1. Add account\n2. View accounts\n3. Search account\n4. Delete account\n5. Generate password\n6. Exit")
    try:
        choice = int(input("> "))
        if choice == 1:
            add_account()
        elif choice == 2:
            view_accounts()
        elif choice == 3:
            search_account()
        elif choice == 4:
            del_account()
        elif choice == 5:
            pass_gen()
        elif choice == 6:
            break
    except ValueError:
        pass

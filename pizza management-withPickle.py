import pickle

customerid = "CUSTOMER"
customerpass = "PASSWORD"

cart = {'vegp':0,'nonvegp':0}

coupon = {'DISCOUNT50':50 ,'DISCOUNT25': 25}

adminid = "ADMIN"
adminpass = "ADMIN"
try:
    m = pickle.load(open("Stocks.pkl", 'rb'))
except:
    m = {'Veg': {'Stocks': 50, 'Price': 350}, 'nonveg': {'Stocks': 50, 'Price': 450}}

while True:
    print("------------------Welcome to pizza console app------------------")
    print("Press:\n\
        1. For Customer Login\n\
        2. For Admin Login\n\
        3. For Exit\n\
    ")
    main_ch = input()
    if main_ch == "3":
        break
    elif main_ch == "2":
        adid = input("Enter admin id: ").upper()
        if adid == adminid:
            apwd = input("Enter Password: ").upper()
            if apwd == adminpass:
                print("Login Successful")
                while True:
                    print(f"Welcome {adminid}")
                    print("Press: \n\
                        1. To View Menu\n\
                        2. To Manage Stock\n\
                        3. To Manage Prices\n\
                        4. To Logout\n\
                        ")
                    adch = input()
                    if adch == "4":
                        break
                    elif adch == "1":
                        print(f"Here is the menu\n\
                            Veggie Pizza: {m['Veg']['Price']}Rs And Stocks: {m['Veg']['Stocks']}\n\
                            Non veg Pizza: {m['nonveg']['Price']}Rs And Stocks: {m['nonveg']['Stocks']}\n\
                            ")
                    elif adch == "2":
                        print(f"Current Stocks:\n\
                            Press to update\n\
                            1. Veg Pizza: {m['Veg']['Stocks']}\n\
                            2. Non-Veg Pizza: {m['nonveg']['Stocks']}\n\
                            ")

                        sch = input()
                        if sch == "1":
                            print("Press:\n\
                                1. To Add\n\
                                2. To Reduce\n\
                                ")
                            uch = input()
                            if uch == "1":
                                n = input("Enter no of veg pizzas to be added: ")
                                try:
                                    n = int(n)
                                except:
                                    print("Only integers accepted")
                                    break
                                if n > 0:
                                    m['Veg']['Stocks'] += n
                                    print(n, "Veg pizzas added\nCurrent Veg Pizza Stock:", m['Veg']['Stocks'])
                                    pickle.dump(m, open('Stocks.pkl', 'wb'))
                                else:
                                    print("Negative additon not allowed please go to reduce")
                                    break
                            elif uch == "2":
                                n = input("Enter no of Veg pizzas to be reduced: ")
                                try:
                                    n = int(n)
                                except:
                                    print("Only integers accepted")
                                    break
                                if n >= m['Veg']['Stocks']:
                                    m['Veg']['Stocks'] = 0
                                    print("Updated Veg:", m['Veg'], ['Stocks'])
                                    pickle.dump(m, open('Stocks.pkl', 'wb'))
                                else:
                                    m['Veg']['Stocks'] -= n
                                    print(n, "Veg pizzas reduced\nCurrent Veg Pizza Stock:", m['Veg']['Stocks'])
                                    pickle.dump(m, open('Stocks.pkl', 'wb'))

                            else:
                                print("Invalid Choice")
                        elif sch == "2":
                            print("Press:\n\
                                1. To Add\n\
                                2. To Reduce\n\
                                ")
                            uch = input()
                            if uch == "1":
                                n = input("Enter no of nonveg pizzas to be added: ")
                                try:
                                    n = int(n)
                                except:
                                    print("Only integers accepted")
                                    break
                                if n > 0:
                                    m['nonveg']['Stocks'] += n
                                    pickle.dump(m, open('Stocks.pkl', 'wb'))
                                    print(n, "Non veg pizzas added\nCurrent Non-Veg Pizza Stock:",
                                          m['nonveg']['Stocks'])
                                else:
                                    print("Negative additon not allowed please go to reduce")
                                    break
                            elif uch == "2":
                                n = input("Enter no of nonveg pizzas to be reduced: ")
                                try:
                                    n = int(n)
                                except:
                                    print("Only integers accepted")
                                    break
                                if n >= m['nonveg']['Stocks']:
                                    m['nonveg']['Stocks'] = 0
                                    pickle.dump(m, open('Stocks.pkl', 'wb'))
                                    print("Updated Non-Veg Pizza Stock:", m['nonveg']['Stocks'])
                                else:
                                    m['nonveg']['Stocks'] -= n
                                    print(n, "Non veg pizzas reduced\nCurrent Non-Veg Pizza Stock:",
                                          m['nonveg']['Stocks'])
                                    pickle.dump(m, open('Stocks.pkl', 'wb'))
                            else:
                                print("Invalid Choice")
                    elif adch == "3":
                        print(f"Current Price:\n\
                            Press to update\n\
                            1. Veg Pizza : {m['Veg']['Price']}\n\
                            2. Non-Veg Pizza : {m['nonveg']['Price']}\n\
                            ")

                        sch = input()
                        if sch == "1":
                            print("Press:\n\
                                1. To Increase Price\n\
                                2. To Reduce Price\n\
                                ")
                            uch = input()
                            if uch == "1":
                                p = input("Enter rs of veg pizzas to be added: ")
                                try:
                                    p = int(p)
                                except:
                                    print("Only integers accepted")
                                    break
                                if p > 0:
                                    m['Veg']['Price'] += p
                                    print(p, "Veg pizzas Price Updated\nCurrent Veg Pizza Stock:", m['Veg']['Price'])
                                    pickle.dump(m, open('Stocks.pkl', 'wb'))
                                else:
                                    print("Negative additon not allowed please go to reduce")
                                    break
                            elif uch == "2":
                                p = input("Enter rs of Veg pizzas to be reduced: ")
                                try:
                                    p = int(p)
                                except:
                                    print("Only integers accepted")
                                    break
                                if p >= m['Veg']['Price']:
                                    m['Veg']['Price'] = 0
                                    print("Updated Veg:", m['Veg'], ['Price'])
                                    pickle.dump(m, open('Stocks.pkl', 'wb'))
                                else:
                                    m['Veg']['Stocks'] -= p
                                    print(p, "Veg pizzas reduced Price\nCurrent Veg Pizza Price:", m['Veg']['Price'])
                                    pickle.dump(m, open('Stocks.pkl', 'wb'))

                            else:
                                print("Invalid Choice")
                        elif sch == "2":
                            print("Press:\n\
                                1. To Increase prices\n\
                                2. To Reduce Price\n\
                                ")
                            uch = input()
                            if uch == "1":
                                p = input("Enter the rs of nonveg pizzas to be Increased: ")
                                try:
                                    p = int(p)
                                except:
                                    print("Only integers accepted")
                                    break
                                if p > 0:
                                    m['nonveg']['Price'] += p
                                    pickle.dump(m, open('Stocks.pkl', 'wb'))
                                    print(p, "Non veg pizzas added\nCurrent Non-Veg Pizza Stock:",
                                          m['nonveg']['Price'])
                                else:
                                    print("Negative additon not allowed please go to reduce")
                                    break
                            elif uch == "2":
                                p = input("Enter rs of nonveg pizzas to be reduced: ")
                                try:
                                    p = int(p)
                                except:
                                    print("Only integers accepted")
                                    break
                                if p >= m['nonveg']['Price']:
                                    m['nonveg']['Price'] = 0
                                    pickle.dump(m, open('Stocks.pkl', 'wb'))
                                    print("Updated Non-Veg Pizza Stock:", m['nonveg']['Price'])
                                else:
                                    m['nonveg']['Price'] -= p
                                    print(p, "Non veg pizzas reduced\nCurrent Non-Veg Pizza Price:",
                                          m['nonveg']['Price'])
                                    pickle.dump(m, open('Stocks.pkl', 'wb'))
                            else:
                                print("Invalid Choice")
                    else:
                        print("Invalid Choice")
            else:
                print("Invalid Password")
        else:
            print("Invalid Id")
    elif main_ch == "1":
        cusid = input("Enter customer id: ").upper()
        if cusid == customerid:
            pwd = input("Enter your password: ").upper()
            if pwd == customerpass:
                print("Login Successful")
                while True:
                    print(f"Welcome {customerid}")
                    print("Press:\n\
                        1. To View Menu\n\
                        2. Place Order\n\
                        3. View Cart\n\
                        4. To Logout\n\
                        ")
                    cust_ch = input()
                    if cust_ch == "1":
                        print(f"Here is the menu\n\
                            Veggie Pizza: {m['Veg']['Price']}Rs\n\
                            Non veg Pizza: {m['nonveg']['Price']}Rs\n\
                            ")
                    elif cust_ch == "2":
                        v = input(f"Enter no of veg pizza's to be ordered within {m['Veg']['Stocks']}: ")
                        try:
                            v = int(v)
                            if v <= m['Veg']['Stocks']:
                                pass
                            else:
                                print("Not enough supplies try later")
                                break
                        except:
                            print("Numbers only accepted")
                            break
                        non = input(f"Enter no of non veg pizza's to be ordered within {m['nonveg']['Stocks']}: ")
                        try:
                            non = int(non)
                            if non <= m['nonveg']['Stocks']:
                                pass
                            else:
                                print("Not enough supplies try later")
                                break
                        except:
                            print("Numbers only accepted")
                            break
                        total = (non * m['nonveg']['Price']) + (v * m['Veg']['Price'])
                        print(f"Total Amount: {total}")
                        cart['vegp'] += v
                        cart['nonvegp'] += non
                        confirm = input(" 1. To continue order \n 2. To go to Cart \n Anything else to dismiss: ")
                        if confirm == "1":
                            print(" 1. To Apply Discount Coupon \n 2. To Place order Without Coupon")
                            coup = input()
                            if coup == "1":
                                code = input("Enter Your Coupon Code : ").upper()
                                try:
                                    discount = coupon[code]
                                    if discount:
                                        wo_disc = (non * m['nonveg']['Price']) + (v * m['Veg']['Price'])
                                        print(
                                            f"Total Amount after {discount}% Discount: {wo_disc - wo_disc * (discount / 100)}")
                                        c = input(" 1. To Confirm order Anything else to exit")
                                        if c == "1":
                                            m['Veg']['Stocks'] -= v
                                            m['nonveg']['Stocks'] -= non
                                            pickle.dump(m, open('Stocks.pkl', 'wb'))
                                            print("Order Successful")

                                            cart["vegp"] = 0
                                            cart["nonvegp"] = 0
                                        else:
                                            break
                                except:
                                    print("Wrong Coupon Code")
                                    break;
                            elif coup == "2":
                                m['Veg']['Stocks'] -= v
                                m['nonveg']['Stocks'] -= non
                                pickle.dump(m, open('Stocks.pkl', 'wb'))
                                print("Order Successful")

                                cart["vegp"] = 0
                                cart["nonvegp"] = 0
                            else:
                                break

                        elif confirm == "2":
                            print('-------->CART<--------\n')
                            print("                  Qty    Sub-Total")
                            print(f" Veg Pizza         {cart['vegp']}        {cart['vegp'] * m['Veg']['Price']}")
                            print(f" Non veg Pizza     {cart['nonvegp']}        {cart['vegp'] * m['nonveg']['Price']}")
                            print(f"\n -------------      Total = {cart['vegp'] * m['Veg']['Price'] + cart['vegp'] * m['nonveg']['Price']}")
                            if not (cart['vegp'] == 0 | cart['nonvegp'] == 0):
                                inp = input("Press 1 To Continue order Anything else to exit from Cart : ")
                                if inp == "1":
                                    print(" 1. To Apply Discount Coupon \n 2. To continue Without Coupon")
                                    coup = input()
                                    if coup == "1":
                                        code = input("Enter Your Coupon Code : ").upper()
                                        try:
                                            discount = coupon[code]
                                            if discount:
                                                wo_disc = (non * m['nonveg']['Price']) + (v * m['Veg']['Price'])
                                                print(f"Total Amount after {discount}% Discount: {wo_disc - wo_disc * (discount / 100)}")
                                                c = input(" 1. To Confirm order Anything else to exit")
                                                if c == "1":
                                                    m['Veg']['Stocks'] -= v
                                                    m['nonveg']['Stocks'] -= non
                                                    pickle.dump(m, open('Stocks.pkl', 'wb'))
                                                    print("Order Successful")

                                                    cart["vegp"] = 0
                                                    cart["nonvegp"] = 0
                                                else:
                                                    break
                                        except:
                                            print("Wrong Coupon Code")


                                    elif coup == "2":
                                        m['Veg']['Stocks'] -= v
                                        m['nonveg']['Stocks'] -= non
                                        pickle.dump(m, open('Stocks.pkl', 'wb'))
                                        print("Order Successful")

                                        cart["vegp"] = 0
                                        cart["nonvegp"] = 0
                                else:
                                    break

                        else:
                            break
                    elif cust_ch == "3":
                        print('-------->CART<--------\n')
                        print("                  Qty    Sub-Total")
                        print(f" Veg Pizza         {cart['vegp']}        {cart['vegp']* m['Veg']['Price']}")
                        print(f" Non veg Pizza     {cart['nonvegp']}        {cart['vegp']* m['nonveg']['Price']}")
                        print(f"\n -------------      Total = {cart['vegp']* m['Veg']['Price']+cart['vegp']* m['nonveg']['Price']}")
                        if not(cart['vegp'] ==0 | cart['nonvegp'] ==0):
                            inp = input("Press 1 To Continue order Anything else to exit from Cart : ")
                            if inp == "1":
                                print(" 1. To Apply Discount Coupon \n 2. To continue Without Coupon")
                                coup = input()
                                if coup == "1":
                                    code = input("Enter Your Coupon Code : ").upper()
                                    try:
                                        discount = coupon[code]
                                        if discount:
                                            wo_disc = (non * m['nonveg']['Price']) + (v * m['Veg']['Price'])
                                            print(
                                                f"Total Amount after {discount}% Discount: {wo_disc - wo_disc * (discount / 100)}")
                                            c = input(" 1. To Confirm order Anything else to exit")
                                            if c == "1":
                                                m['Veg']['Stocks'] -= v
                                                m['nonveg']['Stocks'] -= non
                                                pickle.dump(m, open('Stocks.pkl', 'wb'))
                                                print("Order Successful")

                                                cart["vegp"] = 0
                                                cart["nonvegp"] = 0
                                            else:
                                                break
                                    except:
                                        print("Wrong Coupon Code")
                                        break;


                            elif coup == "2":
                                m['Veg']['Stocks'] -= v
                                m['nonveg']['Stocks'] -= non
                                pickle.dump(m, open('Stocks.pkl', 'wb'))
                                print("Order Successful")

                                cart["vegp"] = 0
                                cart["nonvegp"] = 0
                            else:
                                break
                    elif cust_ch == "4":
                        break
                    else:
                        print("Invalid Choice")
            else:
                print("Incorrect password")
        else:
            print("Invalid Id")
    else:
        print("Invalid Choice")
from TicketBooth import *


opus0= OpusCard("STM", "Ramy", 3, 2021)
opus1= OpusCard("STL", "Tarek", 4, 2021)
opus2= OpusCard("REM", "Turing", 5, 2021)
opus3= OpusCard("REM", "Turing", 5, 2021)
opus4= OpusCard("REM", "Turing", 5, 2021)

tk0= Tickets(2, 2, 2, 2, 2)
tk1= Tickets(2, 2, 2, 10, 0)
tk2=Tickets(2, 2, 2, 2, 2)
tk3= Tickets(3, 2, 1, 5, 0)
tk4= Tickets(3, 2, 1, 5, 0)

opus_lst_0=[opus0, opus1]
opus_lst_1=[opus0, opus1]
opus_lst_2=[opus0, opus1, opus2]
opus_lst_3= []

tb0= TicketBooth(tk0, opus_lst_0)
tb1= TicketBooth(tk2, opus_lst_1)
tb2= TicketBooth(tk1, opus_lst_2)
tb3= TicketBooth(tk3, opus_lst_3)
tb4= TicketBooth(tk4, opus_lst_3)

lst_tb= [tb0, tb1, tb2, tb3, tb4]

message_menu= """ What would you like to do?
                    1. See content of all Ticketbooths
                    2. See content of one Ticketbooth
                    3. List Ticketbooths with same amount of tickets' values
                    4. List ticketbooths with same tickets amount
                    5. List ticketbooths with same amount of tickets values and same number of opus cards
                    6. Add a opus card to an existing ticketbooth
                    7. Remove an existing opus card from a ticketbooth
                    8. Update the exppiry date of an existing Opus card
                    9. Add tickets to a ticketbooth
                    0. TO quit """

header="===============================\n\tWelcome to my Program\n==============================="

option=-1

while option!=0:
    print(header)
    print(message_menu)

    option= int(input("Enter option: "))
    while 0>option or option>9:
        option=int(input("Enter a valid option: "))

    if option==1:
        for tb in lst_tb:
            print(tb)

    elif option==2:
        tb= int(input("Which ticketbooth? "))
        print(lst_tb[tb])

    elif option==3:
        equals=[]
        for x in range(len(lst_tb)):
            y=x+1
            for z in range(y,len(lst_tb)):
                if lst_tb[x].equal_val_tickets(lst_tb[z]):
                    equals.append(tuple((x,z)))
        for tpl in equals:
            print("Ticketbooth ", tpl[0], "and", tpl[1])

    elif option==4:
        equals=[]
        for x in range(len(lst_tb)):
            y=x+1
            for z in range(y,len(lst_tb)):
                if lst_tb[x].equal_tick_dis(lst_tb[z]):
                    equals.append(tuple((x,z)))
        for tpl in equals:
            print("Ticketbooth ", tpl[0], "and", tpl[1])

    elif option==5:
        equals = []
        for x in range(len(lst_tb)):
            y = x + 1
            for z in range(y, len(lst_tb)):
                if lst_tb[x]==lst_tb[z]:
                    equals.append(tuple((x, z)))
        for tpl in equals:
            print("Ticketbooth ", tpl[0], "and", tpl[1])

    elif option==6:
        def option_6():
            try:
                tb= int(input("Which ticketbooth?"))
                card_type= input("Type of card?")
                if card_type.isdigit():
                    print("Enter a literal")
                    option_6()
                name= input("Name on card?")
                if name.isdigit():
                    print("Enter a literal")
                    option_6()
                month= int(input("Expiry month?"))
                year= int(input("Expiry year"))
                new_card=OpusCard(card_type,name,month,year)
                lst_tb[tb].add_opus(new_card)
            except ValueError:
                print("Enter a valid value")
                option_6()

        option_6()

    elif option==7:
        def option_7():
            try:
                tb = int(input("Which ticketbooth?"))
                card = int(input("Which card?"))
                lst_tb[tb].remove_opus(card)
            except ValueError:
                print("Enter valid values ")
                option_7()
        option_7()

    elif option==8:
        def option_8():
            try:
                tb = int(input("Which ticketbooth?"))
                card = int(input("Which card?"))
                month = int(input("Expiry month?"))
                year = int(input("Expiry year"))
                lst_tb[tb].update_expiry(card, month,year)
            except ValueError:
                print("Enter a valid card and ticketbooth")
                option_8()
        option_8()

    elif option==9:
        def option_9():
            try:
                tb = int(input("Which ticketbooth?"))
                reg = int(input("Regular?"))
                jun = int(input("Junior?"))
                sen = int(input("Senior?"))
                week = int(input("Weekly?"))
                daily = int(input("Daily?"))
                lst_tb[tb].update_tickets(reg, jun, sen, daily, week)
            except ValueError:
                print("Enter valid values ")
                option_9()
        option_9()


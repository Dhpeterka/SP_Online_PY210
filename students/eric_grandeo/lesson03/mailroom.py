#!/usr/bin/env python3

donors = [("Bill Gates", [653772.32, 12.17]),
          ("Jeff Bezos", [877.33]),
          ("Paul Allen", [663.23, 43.87, 1.32]),
          ("Mark Zuckerberg", [1663.23, 4300.87, 10432.0]),
          ("Tim Cook", [1563.32, 8976.54])]

prompt = "\n".join(("Welcome to the mailroom!",
          "Please choose from below options:",
          "1 - Send a thank you",
          "2 - Create a report",
          "3 - Quit",
          ">>> "))


def donor_list():
    donor_names = [i[0] for i in donors]
    print(donor_names)
    thank_you()

def add_donation(name):
    donation = float(input("Please enter in a donation: "))
    for i in donors:
        if name in i:
            place = donors.index(i)
    donors[place][1].append(donation)


def thank_you():
    thanks = input("Please enter full name, or type 'list' to see all names: ").title()
    complete = False
    
    while not complete:
        if thanks == 'List':
            donor_list()
            continue
        else:
            if thanks not in [x[0] for x in donors]:
                donors.append((thanks,list()))
        add_donation(thanks)
        complete = True

    print(donors)
    '''    
    #donation = float(input("Please enter in a donation: "))
    #donors.append(thanks[1])
    
    print(donors)
    '''
        
        





def create_report():
    pass



def main():
    response = input(prompt)
    if response == '1':
        thank_you()





if __name__ == "__main__":
    main()


from datetime import datetime

class User:
    #takes a command from a user and compares it to a valid match
    def user_selection(self, command, chain, total_miles):
        match command:
            #looks up a package by ID
            case '1':
                package_id = input("Enter Package ID: ")
                try:
                    return print(chain.search(int(package_id)))
                except:
                    print("No package with that ID")
            #looks up a package(s) with an address
            case '2':
                address = input("Enter Address: ")
                try:
                    package = []
                    rowLen = len(chain.table)
                    for row in range(rowLen):
                        colLen = len(chain.table[row])
                        for col in range(colLen):
                            if chain.table[row][col][1] == address:
                                package.append(chain.table[row][col])
                    if bool(package):
                        return print(package)
                    else:
                        print("Input error or wrong address")
                except:
                    print("Input error or no packages with that address")
            #looks up a package(s) by deadline
            case '3':
                time = input("Enter a time: ")
                try:
                    package = []
                    rowLen = len(chain.table)
                    for row in range(rowLen):
                        colLen = len(chain.table[row])
                        for col in range(colLen):
                            if chain.table[row][col][2] == time:
                                package.append(chain.table[row][col])
                    if bool(package):
                        return print(package)
                    else:
                        print("Input error or no packages with that deadline")
                except:
                    print("Input error or no packages with that deadline")
            #look up package(s) by city
            case '4':
                city = input("Enter a city: ")
                try:
                    package = []
                    rowLen = len(chain.table)
                    for row in range(rowLen):
                        colLen = len(chain.table[row])
                        for col in range(colLen):
                            if chain.table[row][col][3] == city:
                                package.append(chain.table[row][col])
                    if bool(package):
                        return print(package)
                    else:
                        print("Input error or no packages in that city")
                except:
                    print("Input error or no packages in that city")
            #look up package(s) by zipcode
            case '5':
                zip = input("Enter a zipcode: ")
                try:
                    package = []
                    rowLen = len(chain.table)
                    for row in range(rowLen):
                        colLen = len(chain.table[row])
                        for col in range(colLen):
                            if chain.table[row][col][4] == int(zip):
                                package.append(chain.table[row][col])
                    if bool(package):
                        return print(package)
                    else:
                        print("Input error or no packages with that zipcode")
                except:
                    print("Input error or no packages with that zipcode")
            #look up package(s) by weight
            case '6':
                weight = input("Enter package weight: ")
                try:
                    package = []
                    rowLen = len(chain.table)
                    for row in range(rowLen):
                        colLen = len(chain.table[row])
                        for col in range(colLen):
                            if chain.table[row][col][5] == int(weight):
                                package.append(chain.table[row][col])
                    if bool(package):
                        return print(package)
                    else:
                        print("Input error or no packages with that weight")
                except:
                    print("Input error or no packages with that weight")
            #look up package(s) by status
            case '7':
                status = input("Enter package status: ")
                try:
                    package = []
                    rowLen = len(chain.table)
                    for row in range(rowLen):
                        colLen = len(chain.table[row])
                        for col in range(colLen):
                            if status == "delivered":
                                substr = chain.table[row][col][6][0:9]
                                print(substr)
                                if substr == status:
                                    package.append(chain.table[row][col])
                            elif chain.table[row][col][6] == status:
                                package.append(chain.table[row][col])
                    if bool(package):
                        return print(package)
                    else:
                        print("Input error or no packages with that status")
                except:
                    print("Input error or no packages with that status")
            #look up a package at a certain time
            case '8':
                id = input("Enter package id: ")
                at_time = input("Enter a time and date ex HH:MM:SS: ")
                try:
                    start_time = datetime.strptime("08:00:00", '%H:%M:%S').time()
                    package = chain.search(int(id))
                    if bool(package):
                        at_time = datetime.strptime(at_time, '%H:%M:%S').time()
                        package_time = package[6]
                        package_time = datetime.strptime(package_time[21:29], '%H:%M:%S').time()
                        if at_time >= package_time:
                            print('delivered at ' + str(package_time))
                        elif at_time < package_time and at_time >= start_time:
                            print("en route")
                        else:
                            print("at the hub")
                    else:
                        print("Couldn't find package with that ID")

                except:
                    print("Input error")
            #print total miles traveled by all trucks
            case '9':
                print("Total miles traveled by all three trucks: " + str(total_miles))
            #help user with each command
            case 'h':
                print("1: make sure to use an integer for id numbered 1-40")
                print("2: make sure you have the correct address capitalize the first letter if abreviation doesn't work try to spell it out. Ex. South instead of S")
                print("3: EOD for end of day, 10:30 AM or 9:00 AM are the current deadlines")
                print("4: Case sensitive Ex. Salt Lake City")
                print("5: Area code is 5 Digit integer")
                print("6: No units included. Ex. 21 ")
                print("7: Your options are- at the hub, en route, delivered. All lower case")
                print("8: Enter package ID 1-40 inclusive. Then enter a time HH:MM:SS in 24 hour format")
                print("9: total miles includes the first trucks trip back to the hub so driver can switch to truck 3")
            #exit the program
            case 'q':
                print("Thank you for using the program")




        

        
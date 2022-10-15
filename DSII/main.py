#Nathanial Toti
#ID: 002147225 
from Hash import Hash
from LoadTruck import LoadTruck
from Deliver import Dijkstra
from Data import Data
from Time import Time
from User import User
import datetime


def main():
    #start time is 8:00 Am
    time = Time()
    start_time = time.time
    
    #create empty hash table
    chain = Hash()
    
    #load package data
    data = Data()
    package = data.data()
    
    #hash the packages 
    for row in package:
        chain.insert(str(row[0]), row)   
    
    #create graph and vertex
    g = data.create_graph()
    
    #create an empty truck and load them
    truck = LoadTruck()
    truck.load_truck(chain)
    truck.load_truck_two(chain)
    truck.load_truck_three(chain)
    
    #to call dijkstra algorithm and deliver packages
    d = Dijkstra()
    
    #deliver the first truck and second truck
    time, route = d.deliver(g,truck.truck_one,chain, start_time)
    truck_two_time, route2 = d.deliver(g,truck.truck_two, chain, start_time)
    
    #wait for truck one to return and the packages that are delayed till 9:05 
    time += datetime.timedelta(minutes=9)
    
    #deliver truck 3
    time, route3 = d.deliver(g, truck.truck_three, chain, time)

    #calulate the trip back to the hub for the first truck    
    total_miles = route[len(route)-1][2]
    total_miles += route2[len(route2)-2][2] 
    total_miles += route3[len(route3)-2][2]

    #########################################################
    ################### User Interface ######################
             
              # press ENTER after your selection #
    # To look up a package with Package ID press ---------> 1
    # To look up packages with an Address press ----------> 2
    # To look up packages by delivery deadline press -----> 3
    # To look up packages by delivery city press ---------> 4
    # To look up packages by delivery zip code press -----> 5
    # To look up packages by package weight press --------> 6
    # To look up packages by delivery status press -------> 7
    # To look up a package at a certain time press -------> 8
    # To look up the total miles of all trucks press -----> 9
    # For help press -------------------------------------> h
    # To exit press---------------------------------------> q

    #########################################################
    #########################################################

    
    #user input valid commands and user object
    acceptable = ('1', '2', '3', '4', '5', '6', '7', '8', '9', 'h', 'q')
    u = User()
    command = ""
    
    #get users input. verify the command and execute
    while not command == "q" or command not in acceptable:
        
        command = input("Enter a command as listed above: ")
        #if command not in acceptable:
        #    raise Exception("Not a valid command")
        #else:
        u.user_selection(command, chain, total_miles)
        print("\n")
    



main()
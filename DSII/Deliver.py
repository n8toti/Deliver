from Time import Time
import operator
import datetime
import copy

class Vertex:
    def __init__(self, label):
        self.label = label
        self.distance = float('inf')
        self.pred_vertex = None
    

class Graph:
    def __init__(self):
        self.adjaceny_list = {}
        self.edge_weights = {}

    def add_vertex(self, new_vertex):
        self.adjaceny_list[new_vertex] = []
    
    def add_directed_edge (self, vertex, to_vertex, weight=1.0):
        self.edge_weights[(vertex, to_vertex)] = weight
        self.adjaceny_list[vertex].append(to_vertex)

    def add_undirected_edge(self, vertex_a, vertex_b, weight=1.0):
        self.add_directed_edge(vertex_a, vertex_b, weight)
        self.add_directed_edge(vertex_b, vertex_a, weight)
    
    def get_vertex(self, label):
        for i in self.adjaceny_list:
            if i.label == label:
                return i
    def get_edge_weight(self, vertex_a, vertex_b):
        return self.edge_weights[(vertex_a,vertex_b)]

class Dijkstra:
    def __init__(self):
        self.tovisit_queue = []

    def shortest_path(self, graph, start):
        for current in graph.adjaceny_list:
            current.distance = float('inf')
            self.tovisit_queue.append(current)
            
    
        start.distance = 0
        
        while len(self.tovisit_queue) > 0:
            
            smallest_index = 0

            for i in range(1, len(self.tovisit_queue)):
                if self.tovisit_queue[i].distance < self.tovisit_queue[smallest_index].distance:
                    smallest_index = i
            current = self.tovisit_queue.pop(smallest_index)

            for adjacent_vertex in graph.adjaceny_list[current]:
                edge_w = graph.edge_weights[(current, adjacent_vertex)]
                alternative_path_distance = current.distance + edge_w
                  
                # If shorter path from start_vertex to adjacent_vertex is found,
                # update adjacent_vertex's distance and predecessor
                if alternative_path_distance < adjacent_vertex.distance:
                    adjacent_vertex.distance = alternative_path_distance
                    adjacent_vertex.pred_vertex = current


    def get_shortest_path(self, start_vertex, end_vertex):
    # Start from end_vertex and build the path backwards.
        path = ""
        current_vertex = end_vertex
        while current_vertex is not start_vertex:
            path = " -> " + current_vertex.label + path
            current_vertex = current_vertex.pred_vertex
        path = start_vertex.label + path
        
        return path

        
    def deliver(self, graph, truck, chain, time):
        route = []
        i = 0
        smallest = 0.0
        delpos=[]
        totaldist = 0.0
        start = graph.get_vertex("HUB")
        
        #time variable to track packages delivered at a certain time and calculate when delivered
        t = Time()
        eight = datetime.datetime(2022, 9, 2, 8, 35, 0)
        nine = datetime.datetime(2022, 9, 2, 9, 25, 0)
        nine_thirty = datetime.datetime(2022, 9, 2, 9, 35, 0)
        ten = datetime.datetime(2022, 9, 2, 10, 25, 0)
        twelve = datetime.datetime(2022, 9, 2, 12, 3, 0)
        one = datetime.datetime(2022, 9, 2, 13, 12, 0)
        screen_shot_one = {}
        screen_shot_two = {}
        screen_shot_three = {}
        #wrong address
        change_address_time = datetime.datetime(2022, 9, 2, 10, 20, 0)
        change = [9, "300 State St", "EOD", "Salt Lake City", 84103, 2, "en route"]
        right_address = False
        

        # deliver the packages in the truck
        while i < len(truck):
            
            #find package with the wrong address and hold it until 10:20 AM till flag is triggered
            if truck[i] == change and not right_address:
                truck.remove(truck[i])
                chain.delete(str(change[0]), change)
            if time >= change_address_time and not right_address:
                    change[1] = "410 S State St"
                    change[4] = 84103
                    chain.insert(str(change[0]), change)
                    truck.append(change)
                    right_address = True
            
            #when i is zero find the next shortest path from previous 
            if i == 0:
                self.shortest_path(graph, start)
            for v in graph.adjaceny_list:
                if v.label == truck[i][1]:                 
                    if smallest == 0.0:
                        smallest = v.distance
                        pack = v 
                        delpos = truck[i]
                    elif v.distance < smallest:
                        smallest = v.distance
                        pack = v 
                        delpos = truck[i]

            #when i is at the end of truck the shortest path is found
            if (i == len(truck)-1):
                #take the next smallest path information
                totaldist += smallest
                temp = pack
                pack = self.get_shortest_path(start, pack)
                start = temp
                
                #remove from truck
                truck.remove(delpos)

                
                # delete from hash and rehash with new value
                chain.delete(str(delpos[0]), delpos)
                time = t.delivered_at(time, smallest)
                delpos[6] = 'delivered ' + str(time)
                chain.insert(str(delpos[0]), delpos)

                #create route path with distance and total distance
                templist = [pack, smallest, totaldist]
                route.append(templist)
                smallest = 0.0    
                i = 0
       
                #return to the hub
                if len(truck) == 0:
                    self.shortest_path(graph, start)
                    for v in graph.adjaceny_list:
                        if v == graph.get_vertex("HUB"):
                            foo = self.get_shortest_path(start, v)
                            totaldist += v.distance
                            templ = [foo, v.distance, totaldist]
                            route.append(templ) 
        
            else:
                i += 1


        return time, route

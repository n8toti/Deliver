import operator


class LoadTruck():
    def __init__(self, capacity=16):
        self.truck_one = []
        self.truck_two = []
        self.truck_three = []
        self.sorted_list = []

    
    def sort(self, hash):
        hlen = len(hash.table)
        for i in range(hlen):
            collen = len(hash.table[i])
            for j in range(collen):
                self.sorted_list.append(hash.table[i][j])
        self.sorted_list = sorted(self.sorted_list, key=operator.itemgetter(1,2,0))

    def load_truck(self, hash):
        deliver_together = (13, 14, 15, 16, 19, 20)
        self.sort(hash)
        check_address = []
        
        #for row in self.sorted_list:
        #    print(row)
        for row in self.sorted_list[:]:
            if len(self.truck_one) < 16:
                if row[0] in deliver_together:
                #add to truck1 and remove from sorted_list
                    self.truck_one.append(row)
                    check_address = row
                #change status to en route delete and rehash
                    hash.delete(str(row[0]), row)
                    row[6] = 'en route'
                    hash.insert(str(row[0]), row)
                    self.sorted_list.remove(row)
                elif bool(check_address):
                    if check_address[1] == row[1]:
                        self.truck_one.append(row)
                        hash.delete(str(row[0]), row)
                        row[6] = 'en route'
                        hash.insert(str(row[0]), row)
                        self.sorted_list.remove(row)
    
    def load_truck_two(self, hash):
        check_address = []
        truck_two_only = (3, 18, 36, 38)
        truck_three = (6, 25, 9)
        for row in self.sorted_list[:]:
            if len(self.truck_two) < 16:
                if row[0] in truck_two_only:
                    check_address = row
                    self.truck_two.append(row)
                    hash.delete(str(row[0]), row)
                    row[6] = 'en route'
                    hash.insert(str(row[0]), row)
                    self.sorted_list.remove(row)
                elif bool(check_address):
                    if check_address[1] == row[1] and check_address[0] not in truck_three:
                        self.truck_two.append(row)
                        hash.delete(str(row[0]), row)
                        row[6] = 'en route'
                        hash.insert(str(row[0]), row)
                        self.sorted_list.remove(row)
        
        for row in self.sorted_list[:]:
            if len(self.truck_two) < 16 and row[0] not in truck_three:
                if row[2] == '10:30 AM':
                    check_address = row
                    self.truck_two.append(row)
                    hash.delete(str(row[0]), row)
                    row[6] = 'en route'
                    hash.insert(str(row[0]), row)
                    self.sorted_list.remove(row)
                elif bool(check_address):
                    if check_address[1] == row[1]:
                        self.truck_two.append(row)
                        hash.delete(str(row[0]), row)
                        row[6] = 'en route'
                        hash.insert(str(row[0]), row)
                        self.sorted_list.remove(row)  

    def load_truck_three(self, hash):
        for row in self.sorted_list[:]:
            if len(self.truck_three) < 16:
                check_address = row
                self.truck_three.append(row)
                hash.delete(str(row[0]), row)
                row[6] = 'en route'
                hash.insert(str(row[0]), row)
                self.sorted_list.remove(row)


                    
                    
        
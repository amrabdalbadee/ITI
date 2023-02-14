#lab 5
def knapsack(mode='manually'):
    if mode =='manually':
        no_of_items = int(input("please enter number of items: "))
        items = []
        for i in range(no_of_items):
            item_string= input(f"please enter item{i+1} (name,weight,value) ").strip().split(",")
            #item = tuple(map(int, item_string.split(',')))
            item_name = item_string[0]
            item_weight = int(item_string[1])
            item_value = int(item_string[1])
            item = (item_name,item_weight,item_value)
            items.append(item)
            #print(item)
    elif mode == 'default':
        items = [('i1', 5, 50), ('i2', 10, 60) ,('i3', 20, 140),('i4',40,40)]

    print("1-minimum weight \n")
    print("2-maximum weight \n")
    print("3-maximum value \n")
    print("4-maximum value/weight \n")
    knapsack_size = int(input("please enter knapsack maximum weight limit "))
    x = int(input("please enter operation umber: "))
    capacity = knapsack_size
    #print(sorted_items)
    match x:
        case 1:
            sorted_items = sorted(items, key=lambda x: x[1])
            taken_items = []
            counter = 0
            for item in sorted_items:
                if capacity != 0:
                    if item[1] > capacity:
                        remain = abs(capacity-item[1])
                        fraction = item[1]//capacity
                        new_item = (item[0],remain,item[2]/fraction)
                        capacity -= remain
                        counter += 1
                        taken_items.append(new_item)
                    else:
                        capacity -= item[1]
                        counter += 1
                        taken_items.append(item)
                else:
                    print("list is Full!")
                    continue
            print(taken_items)

        case 2:

            sorted_items = sorted(items, key=lambda x: x[1],reverse=True)
            taken_items = []
            counter = 0
            for item in sorted_items:
                if capacity != 0:
                    if item[1] > capacity:
                        remain = abs(capacity - item[1])
                        fraction = item[1] // capacity
                        new_item = (item[0], remain, item[2] / fraction)
                        capacity -= remain
                        counter += 1
                        taken_items.append(new_item)
                    else:
                        capacity -= item[1]
                        counter += 1
                        taken_items.append(item)
                else:
                    print("list is Full!")
                    continue
            print(taken_items)
        case 3:
            sorted_items = sorted(items, key=lambda x: x[2], reverse=True)
            taken_items = []
            counter = 0
            for item in sorted_items:
                if capacity != 0:
                    if item[1] > capacity:
                        remain = abs(capacity - item[1])
                        fraction = item[1] // capacity
                        new_item = (item[0], remain, item[2] / fraction)
                        capacity -= remain
                        counter += 1
                        taken_items.append(new_item)
                    else:
                        capacity -= item[1]
                        counter += 1
                        taken_items.append(item)
                else:
                    print("list is Full!")
                    continue
            print(taken_items)
        case 4:
            sorted_items = sorted(items, key=lambda x: x[2]/x[1], reverse=True)
            taken_items = []
            counter = 0
            for item in sorted_items:
                if capacity != 0:
                    if item[1] > capacity:
                        remain = abs(capacity - item[1])
                        fraction = item[1] // capacity
                        new_item = (item[0], remain, item[2] / fraction)
                        capacity -= remain
                        counter += 1
                        taken_items.append(new_item)
                    else:
                        capacity -= item[1]
                        counter += 1
                        taken_items.append(item)
                else:
                    print("list is Full!")
                    continue
            print(taken_items)

knapsack('default')

print ("Welcome to the Food Spot")

Grocery = ["Milk", "Cheese", "Bread"]

max_inven = 20
min_inven = 10
cur_inven = max_inven - min_inven

# "max_inven" is the maximum limit of inventory for that particular item
# "min_inven" is the minimum limit of inventory for that particular item
# "cur_inven" is current inventory of that particular item

    
if (max_inven < min_inven) and (cur_inven > min_inven):
    print "Next Item"

elif ( min_inven < max_inven):
    print "Reorder"

print ("Quantity remains ="),cur_inven








    

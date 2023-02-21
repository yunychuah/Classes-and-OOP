import FoodClass as fc

# this dictionary represents transactions. The key of the dictionary is the transaction identifier.
# The Value of the dictionary is a list. The elements in each list are -
# ['Date', 'Name of item', 'Cost', 'customerid' ]

dict = {'trans1':['2/15/2023','The Lone Patty',17,569],
                'trans2':['2/15/2023','The Octobreakfast',18,569],
                'trans3':['2/15/2023','The Octoveg',16,570],
                'trans4':['2/15/2023','The Octoburger',20,570],
}

order_total = 0

#create customer instance using info here

customer = fc.Customer(570,'Danni Sellyar','97 Mitchell Way Hewitt Texas 76712','dsellyarft@gmpg.org','254-555-9362', False)
#customer = fc.Customer(569,'Aubree Himsworth','1172 Moulton Hill Waco Texas 76710','ahimsworthfs@list-manage.com','254-555-2273', True)

print(f"Customer Name: {customer.get_name()}")
print(f"Phone: {customer.get_phone()}")

#create trasaction instances based on info in dict
for i in dict:
    i = fc.Transaction(dict[i][0], dict[i][1], dict[i][2], dict[i][3])

#display report
    if int(i.get_customerid()) == int(customer.get_customerid()):
        cost = int(i.get_cost())
        order_total += cost
        print(f"Order Item:{i.get_item_name()} Price: $ {(format(i.get_cost(), '.2f'))}")

print(f"Total cost: ${format(order_total,'.2f')}")

if customer.get_member_status() == True:
    discount = .2 * order_total
    discounted_total = order_total - discount
    print(f"Member Discount: ${format(discount, '.2f')}")
    print(f"Total cost after Discount: ${format(discounted_total, '.2f')}")


#display report showing customer info & order info

#customer should only be charged for items they ordered(match customer_id)
#if customer is reward member(member_status) get 20% discount
#don't create 2 customer instances
#run program twice, once for each customer






#create 2 classes:customer class, transaction class
import random 

class Customer:
    def __init__(self,customerid,name,address,email,phone,memberstatus):
        self.customerid = customerid
        self.name = name
        self.address = address
        self.email = email
        self.phone = phone
        self.member_status = memberstatus

    def get_customerid(self):
        return self.customerid
    
    def get_name(self):
        return self.name 
    
    def get_address(self):
        return self.address
    
    def get_email(self):
        return self.email 
    
    def get_phone(self):
        return self.phone
    
    def get_member_status(self):
        return self.member_status

class Transaction:
    def __init__(self,date,itemname,cost,customerid):
        self.date = date
        self.item_name = itemname
        self.cost = cost
        self.customerid = customerid
    
    def get_date(self):
        return self.date 
    
    def get_item_name(self):
        return self.item_name

    def get_cost(self):
        return self.cost
    
    def get_customerid(self):
        return self.customerid 

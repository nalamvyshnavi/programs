class electronic:
    def __init__(self,name,price,deal_price,rating):
        self.name=name
        self.price=price
        self.deal_price=deal_price
        self.rating=rating

    def display_product_details(self):
        print(self.name)
        print(self.price)
        print(self.deal_price)
        print(self.rating)
    def get_deal_price(self):
        return self.deal_price
class product(electronic):
    def __init__(self,name,price,deal_price,rating,warranty):
        electronic.__init__(name,price,deal_price,rating)
        self.warranty = warranty
    def get_warranty(self):
        return self.warranty
class grocery(electronic):
    pass
    #def __init__(self,name,price,deal_price,rating,exipydate,packagedate):
           # super().__init__(name,price,deal_price,rating)
            #self.exipydate = exipydate
            #self.packagedate = packagedate

    #def get_exipydate(self):
        #print(self.exipydate,self.packagedate)
class order:
    def __init__(self,type,address):
        self.type=type
        self.address=address
        self.items=[]
    def add_item(self,electronic,quantity):
        self.items.append((electronic,quantity))
    def display_order_details(self):
        for electronic,quantity in self.items:
            electronic.display_product_details()
            print("quantity:{}".format(quantity))
    def display_total_bill(self):
        total_bill=0
        for electronics,quantity in self.items:
            price=electronic.get_deal_price()*quantity
            total_bill+=price
            print("totalbill:{}".format(total_bill))
mk=grocery("milk",40,25,3.5)
te=product("tv",45000,40000,3.4,12)
order=order("primedelivery","vijayawada")
order.add_item(mk,2)
order.add_item(te,1)
print("+++++")
order.display_order_details()
print("+++++")
order.display.total_bill()
#elobj=electronic("bottle",200,100,5)
#elobj.display_product_details()
#e1obj=product("2years")
#e1obj.get_warranty()
#e2obj=grocery("bed",20000,10000,5,"10/11/2000","12/11/2000")
#e2obj.display_product_details()
#e2obj.get_exipydate()








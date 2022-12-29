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
    def __init__(self,warranty):
        self.warranty = warranty
    def get_warranty(self):
        return self.warranty

class grocery(electronic):

    def __init__(self,name,price,deal_price,rating,exipydate,packagedate):
        super().__init__(name,price,deal_price,rating)
        self.exipydate = exipydate
        self.packagedate = packagedate

    def get_exipydate(self):
        print(self.exipydate,self.packagedate)

elobj=electronic("bottle",200,100,5)
elobj.display_product_details()
e1obj=product("2years")
e1obj.get_warranty()
e2obj=grocery("bed",20000,10000,5,"10/11/2000","12/11/2000")
e2obj.display_product_details()
e2obj.get_exipydate()








#dictionaries
#val_1=input()
#val_2=int(input())
#msg="hi{0}.you are{1} years."
#print(msg.format(val_1,val_2))

dict_a={'name':'hi','age':10}
#print(dict_a.get('name'))
#result='name'in dict_a
#print(dict_a)
dict_a['age']=15
#print(dict_a.keys())
#print(dict_a.values())
#print(dict_a.items())
for key in dict_a.keys():
    print(dict_a[key])
    print(key)

#list_a=[("name","vyshu"),["age",10],("roll_no",10)]
dict_a={'name':'hello','age':10}
print(len(dict_a))
if 'name' in dict_a:
    print("true")
dict_a.clear()
print(dict_a)

list_a=['hi',10]
list_b=list_a.copy()
list_b.extend([20])
print(list_b)
print(id(list_a))
print(id(list_b))

list_a=[("name","hi"),["age",10],("rollno",100)]
dict_a=dict(list_a)

print(dict_a)

m=int(input())
n=int(input())
mat=[]
for i in range(m):
    row=input().split()
    for j in range row:
        mat.append(j)
mat.sort()
k=0
for i in range(m):
    for j in range(n):
        print(mat[k],end=' ')
        k=k+1
    print()

def greet():
    print("hi")
greet()
name=input()
greet()
print(name)
def greet(word):
    print("hello"+word)

name=input()
greet(word=name)
def get_list(string_a):
    list_a=string_a.split(',')
    len_list_a=len(list_a)
    for i in range (len_list_a):
        list_a[i]=int(list_a[i])
    return list_a
string_a=input()
numbers_list=get_list(string_a)
print(numbers_list)
def greet():
    print("hi")
greet()
def greet(word):
    print("welcome"+word)
name="hcl"
greet(word=name)
def square(list):
    list_a=list.split(',')
    for i in range (list_a):
        list_a=list_a[i]*2
        print(list_a)
    return list_a
list=list(input())
p=square(list)
print(p)
def area1(area):
    square = 4 * area
    print(square)
area = input()
p = (area1(area))
print(p)


def area1(area):

def div(nb1):
    if nb1%7==0:
        print("true")
    else:
        print("false")
    return nb1
nb1=int(input())
p=div(nb1)
print(p)

class car:
    def sample_car_instance_method(self,a):
        print(a)
carobj=car()
carobj.sample_car_instance_method("hello again!")
carobj2=car()
carobj2.sample_car_instance_method(2)

class staticclass:
    @staticmethod
    def sample_static_method_addtion(x,y):
        return x+y
    @staticmethod
    def sample_static_method_multiplication(x,y):
        return x*y
staticobj=staticclass()
output_add=staticobj.sample_static_method_addtion(2,3)
output_mul=staticobj.sample_static_method_multiplication(2,3)
print(output_add,output_mul)
class animal:
    def _init_(self,species,gender):
        self.species=species
        self.gender=gender
animalobj=animal('dog','male')
print(animalobj.gender)
print(animalobj.species)
class car:
    def __init__(self,colour,max_speed,accleration,tyre_friction,start_engine,current_spped):
        self.colour=clr
        self.max_speed=speed1
        self.accleration=accleration
        self.tyre_friction=tyre_friction
        self.start_engine=start_engine
        self.current_speed=speed2
    def start_engine(self):
        engine_started="true"
    def stop_engine(self):
        engine_sttoped="false"
    def apply_brakes(self):
        if self.current_speed>=self.tyre_friction:
            self.current_speed=self.current_speed-self.tyre_friction
        else:
            self.current_speed=0
        print(self.current_speed)
    def sound_horn(self):
        if self.engine_started==true:
            print("BEEP BEEP")
        else:
            print("car is not stared yet")
    c1=car("black","1000kmph","100rpm",120,80)
    c1.start_engine()
    c1.stop_engine()
    c1.apply_brakes()
    c1.apply_brakes()
    c1.sound_horn()

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
class product(electronic):
    def __init__(self,warranty):
        self.warranty = warranty
    def get_warranty(self):
        print(self.warranty)
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








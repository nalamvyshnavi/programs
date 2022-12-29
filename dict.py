#a=2
#tuple_a=(5,"six",a,8)
#print(tuple_a)
#print(tuple_a[2])
#colour="blue"
#tuple_a=tuple(colour)
#print(tuple_a)
#list=[1,2,3]
#tuple_a=tuple(list)
#print(tuple_a)
#tuple=tuple(range(5))
#print(tuple)
#tuple=(1,2,3)
#is_part=4 in tuple
#print(is_part)
#a=('t','h','e')
#(s_1,s_2,s_3)=a
#print(s_1)
#print(s_2)
#a=1,2,3
#print(type(a))
#print(a)
#a=1
#print(type(a))
#list_a=[1,2,3,
#list_a.remove(3)
#print(list_a)


#list=[1,2,3,4,4]
#set_a=set(list)
#list_a=list(set_a)
#print(list_a)

#seta={1,2,3,4}
#setb={3,4,2,5,6}
#union=setb.union(seta)
#print(union)

#number="1,2,*,4,@,5"
#num_1=number.isdigit()
#print(num_1)

set_a={1,2,3,4,5}
set_b={1,4,3,5}
set_c={7,8}
superset=set_b.issuperset(set_a)
subset=set_c.issubset(set_b)
disjoint=set_c.isdisjoint(set_a)
print(disjoint)
print(superset)
print(subset)

set_a={1,2,3,5,4}
set_b={1,3,4,6,8}
set_c={2,4,5,1,2}
set=set_a & set_b & set_c
print(set)

list=[1,2,3,4,5]
tuple_a=tuple(list)
print(tuple_a)
tuple1=max(tuple_a)
tuple2=min(tuple_a)
print(tuple1)
print(tuple2)

list_1=[1,2,3,4,5,]
n=9
list_2=[]
for i in range (len(list_1)):
    for j in range(i+1,len(list_1)):
        if (list_1[i]+list_1[j]==n):
            list_3=[list_1[i],list_1[j]]
            list_2.append(list_3)
print(list_2)

list_a=[1,"six",[9,7],9.8]
print(list_a[2][0])
name=input()
age=input()
msg=("hi"+name+".you are"+str(age)+"years old.")
print(msg)
val_1="hi"
val_2="10"
msg="hi{}.you are{} years."
msg.format(val_1,val_2)

m=int(input())
n=int(input())
mat=[]
for i in range(m):
    row=input().split()
    for j in range(n):
        mat.append(j)
mat.sort()
k=0
for i in range(m):
    for j in range(n):
        print(mat[k],end=' ')
        k=k+1
    print()





















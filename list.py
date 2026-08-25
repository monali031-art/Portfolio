#List Data Structure 

# l=[]
# print(l)
# print(type(l))


# l=eval(input('Enter a list : '))
# print(l)




# l=list((10,20,30,40))
# print(l)


# l=[23,33,'surendra',45,63,555,True]
# print(l)


# msg='welcome to python'
# l=msg.split()
# print(l)




# dob='10-05-1997'
# l=dob.split('-')
# print(l)


# dob='10-05-1997'
# l=dob.split()
# print(l)


# msg='welcome to python django drf react'
# l=msg.split()

# for i in l:
#     print(i[0])






# msg='welcome to python django drf react'
# l=msg.split()

# for i in l:
#     if len(i)>=4:
#         print(i[4])
#     else:
#         print(i[0])






#program 
#find out all the even number from a list 

# l=[23,12,11,5,78,90,27]

# for i in l:
#     if i%2==0:
#         print(i)



# l=[23,12,11,5,78,90,27]

# for i in l:
#     if i%2!=0:
#         print(i)


# l=[23,12,11,5,78,90,27]
# for i in l:
#     if i%2==0:
#         print(f'{i} is even')
#     else:
#         print(f'{i} is odd')


# l=[10,22.3,'surendra','rahul',22,40.6,'zini']

# for i in l:
#     if type(i)==str:
#         print(i)


# l=[10,20,52,63,44,15,36,33,12,14]
# for i in l:
#     if i%2==0:
#         print(i*2)
#     else:
#         print(i*3)



# l=['surendra','priyanka','rahul','zini','jack','scoot','dev','anjali','stalina','salina']

# for i in l:
#     print(f'{i} - {len(i)}')



# l=['surendra','priyanka','rahul','zini','jack','scoot','dev','anjali','stalina','salina']

# for i in l:
#     if i[0]=='s':
#         print(i)




# l=['surendra','priyanka','rahul','zini','jack','scoot','dev','anjali','stalina','salina']
# count=0
# for i in l:
#     print(f'{i} is present at {count} index')
#     count=count+1




# l=['surendra','priyanka','rahul','zini','jack','scoot','dev','anjali','stalina','salina']
# count=0
# for i in l:
#     print(f'{i} is present at {count}  and  {-len(l)+count} index')
#     count=count+1



# l=['surendra','priyanka','rahul','zini','jack','scoot','dev','anjali','stalina','salina']

# for i in l:
#     count=0
#     for j in i:
#         if j in ('a','e','i','o','u'):
#             count=count+1
#     print(f'{i} contain {count} vowel')




# l=['surendra','priyanka','rahul','zini','jack','scoot','dev','anjali','stalina','salina']

# l.sort()
# print(l)



# l=['surendra','priyanka','rahul','zini','jack','scoot','dev','anjali','stalina','salina']

# l.sort(reverse=True)
# print(l)





# l=['surendra','priyanka','rahul','zini','jack','scoot','dev','anjali','stalina','salina']

# l.sort()

# for i in l:
#     x=sorted(i)
#     for i in x:
#         print(i,end='')
#     print()
my_list = [1, 2, 3, 4, 5, 6]
for i in my_list:
    my_list.remove(i)
print(my_list)

'''Jab loop chalega toh woh pehle first index ko remove krega mean 1 then 2nd loop mein woh 2nd index ko remove karne jayega but this 2nd index par 2 nhi 3ree hoga
so it will remove three and according to this it will remove 5 in next loop and the final value becomes [2, 4, 6]'''

'''In other way to understand! jitni baar loop chalege utni baar values ka index change hota rhega'''
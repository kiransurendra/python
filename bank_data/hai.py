''' sum of all elements in a list '''

# a=[1,2,3,4,5]
# b=a[0]+a[1]+a[2]+a[3]+a[4]
# print(b)


# a=[1,2,3]
# for item in a:
#     print(a[0]+a[1]+a[2])
#     break

#
# def list(item):
#     sum =0
#     for x in item:
#         sum += x
#     return sum
# print(list([1,2,3,10]))





''' multiples of all elements in a list '''
# def list(item):
#     multiple =1
#     for x in item:
#         multiple *= x
#     return multiple
# print(list([1,2,3,10]))



'''3. Write a Python program to get the largest number from a list'''
#
# def max_list(item):
#     max = item[0]
#     for a in item:
#         if a > max:
#             max = a
#     return a
# print(max_list([1,5,2,6,7]))


'''4. Write a Python program to get the smallest number from a list.'''

def small_list(item):
    min = item[0]
    for a in item:
        if a < min:
            min = a

    return min
print(small_list([1,2,3,4,0,-1]))


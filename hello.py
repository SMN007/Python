#print(abs(-1)) // removed any negative value




#print(round(3.75,1))

'''
numo_1 = '100'
numo_2 = '200'


numo_1 = (int(100))
numo_2 = (int(200))

print(numo_1 + numo_2) # convert to int 
'''
'''
courses = ['History','Math', 'Physics', 'Computer']

print(courses[2:]) # include 0 index but exclude last index
'''
'''
courses = ['History','Math', 'Physics', 'Computer']

courses.append('Art') #add an item to you list at the last

print(courses  

'''  
'''
courses = ['History','Math', 'Physics', 'Computer']

courses.insert( 1,'Art') #insert a item in a list any whare you want

print(courses)

'''

'''
courses = ['History','Math']

courses_2 = ['Physics', 'Computer']

courses.insert(0, courses_2) #list insite a list

print(courses) 
'''

'''
courses = ['History','Math']
courses_2 = ['Physics','Computer']


courses_3 = (courses + courses_2)

print(courses_3[0]) # print any index of a sum list or a list
'''

'''courses = ['History','Math']
courses_2 = ['Physics','Computer']

courses.extend(courses_2) #join 2 list without brackets

print(courses)'''



'''courses = ['History','Math']
courses_2 = ['Physics','Computer']

courses.append(courses_2) #join 2 list with brackets(means list inside a list)


print(courses)'''



'''courses = ['History','Math','Physics','Computer']


courses.remove('History') #to remove any item from the list

print(courses)'''



'''courses = ['History','Math','Physics','Computer']


courses.pop() #pop is a usefull when you just want to removed the last item from the list (like stack mathode)

print(courses)'''


'''courses = ['History','Math','Physics','Computer']


courses2 = courses.pop() #to to see which item is removed from the list (or if we to print out the pop item this is use full)

print(courses2)'''


'''courses = ['History','Math','Physics','Computer']

courses.reverse() #to reverse the list (the last item is the 1st item)

print(courses)'''

'''courses = ['History','Math','Physics','Computer']
num = [1,6.9,6.0,9,6]

courses.sort() #it' used to sorted the list according to the A-Z
num.sort()

print(courses)
print(num)'''


'''courses = ['History','Math','Physics','Computer']
num = [1,6.9,6.0,9,6]

courses.sort() 
num.sort(reverse=True) #sort and reversed the number Z-A

print(courses)
print(num)'''

'''num = [5,6.9,6.0,1,2,4,3,9,6]

num2=sorted(num) # this sorted function is return the sorted valued(2nd methode other is sort)

print(num2)'''

'''

# find out what is the min, max, and medium value of a list
num = [2,3,4,51,53,22,42,96,6]

num_min = min(num)
num_sum = sum(num)
num_max = max(num)

print(num_min)









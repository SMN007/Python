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
print(num_sum)
print(num_min)


'''

'''courses = ['History','Math','Physics','Computer']

print(courses.index('Computer')) #find out the index of a item in our list


#what if I want to check the value is exict or not in our list

courses = ['History','Math','Physics','Computer']

print('Art' in courses) #to check its exist or not(true or false)

'''
'''courses = ['Math','Physics','Bio']

print('Math' in courses) # check the value is avelable or not in our list

'''

'''courses = ['Math','Physics','Bio']

for index,course in enumerate(courses,): #inderx of a value 1.
  print(index,course)'''
'''courses = ['Math','Physics','Bio']

course_str = ' - '.join(courses) #join any thing between in your list (like , - _ ) // this is a string

new_list = course_str.split(' - ') # to make it a string to a list vslue ['a','b','c']

print(new_list)'''


## in puthon list is a mutable and tupple is'not

'''list_1 = ['History','Math','Physics','Computer']
list_2 = list_1

list_1 [0] ='Art' # The output are same because we l1 is asign in l2
# in this way if we change something list_1 then the output will be changed as wall as l1

print(list_1)
print(list_2) # so the values is mutable in LIST


'''



'''#immptabel Example
tuple_1 = ('History','Math','Physics')
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

tuple_1[0] = 'Art'

print(tuple_1) # it's give you a error('tuple' object does not support item assignment)
# because it's immutable (can't change the value)
print(tuple_2)'''



'''# sets(set are values that are unordered and also have not duplicates)

courses = {'History','Math','Physics','Computer','Math'}

print(courses) # its removed duplicate vaiues Math

print('Math' in courses)

'''
'''
cs_courses = {'History','Math','Physics','Computer'}
art_courses = {'History','Math','Art','design'}

print(cs_courses.intersection(art_courses)) # its use for check common values
print(cs_courses.union(art_courses)) # print value without common value


'''
'''
:Note:

#Empty list
empty_list = []
empty_list = list()

#Empty Tuples
empty_tuple = ()
empty_tuple = tuple()

#Empty Sets
empty_set = ()
empty_set = set()

'''

'''thistuple = ("apple", "banana", "cherry")
print(thistuple[1]) #print tupple
'''













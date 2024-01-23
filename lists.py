# # # Subject of this python script: lists
# # Authored by: Sania Shakeel
# # Where to contact: sania040@github.com shakeelsania040@gmail.com

# Question 1 -> Let us say your expense for every month are listed below, Create a list to store these monthly expenses and using that find out
expense = [2200, 2350, 2600, 2130, 2190]

# 1. In Feb, how many dollars you spent extra compare to January?
print ("The extra $ spent in feb compared to jan: ",str(expense[1]  - expense[0]))

# 2. Find out your total expense in first quarter (first three months) of the year.
print("The total expense in first quater of this year is:  "+ str(expense[0] + expense[1] + expense[2]))

# 3. Find out if you spent exactly 2000 dollars in any month
print(3000 in expense)

# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
expense.append(1980)
print(expense)

# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this...
expense[3] = expense[3] - 200
print(expense)

# Question 2 -> You have a list of your favourite marvel super heros. use this for finding out
heros=['spider man','thor','hulk','iron man','captain america']

# 1. Length of the list
print(len(heros))

# 2. Add 'black panther' at the end of this list
heros.append('black penther')


# 3. You realize that you need to add 'black panther' after 'hulk',
#    so remove it from the list first and then add it after 'hulk'

heros.remove('black penther')
heros.insert(4, 'black Panther')

# 4. Now you don't like thor and hulk because they get angry easily :)
#    So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#    Do that with one line of code.
heros[1:3]=['doctor strange']
print(heros)

# 5. Sort the list in alphabetical order
heros.sort()
print(heros)

#  Question 3 : Create an empty list called my_list.Add integers 1 to 5 to the list.Print the list...
my_list = [1, 2, 3, 4, 5]
print(my_list)


# Question 4: Create two lists: list1 with elements [1, 2, 3] and list2 with elements [4, 5, 6].Concatenate the two lists and store the result in a new list called combined_list.Print combined_list.
list_1 = [1, 2, 3]
list_2 = [4, 5, 6]
combined_list = list_1 + list_2
print(combined_list)

# Question 5: Create a list called numbers with elements [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].Print the first five elements using slicing.Print the last three elements using negative indexing.
numbers = [1,2,3,4,5,6,7,8,9,10]
print(numbers[0:5])
print(numbers[-3:])

# Question 6:    Create a list called squares that contains the squares of numbers from 1 to 5 using list comprehension.Create a list called even_squares that contains the squares of even numbers from 1 to 10 using list comprehension.
squares = [x**2 for x in range(1,5)]
even_squares = [ x for x in squares if x % 2 == 0]
print(even_squares)

# Question 7: Create a list called fruits with elements ['apple', 'banana', 'cherry'].Add 'orange' to the end of the list.Remove 'banana' from the list.Print the modified list.

fruits = ['apple', 'banana', 'cherry']
fruits.append('orange')
print(fruits)
fruits.remove('banana')
print(fruits)

# QUestion 8: Create a list called numbers with elements [3, 1, 4, 1, 5, 9, 2, 6, 5].Find the length of the list.Find the sum of the elements in the list.Find the maximum and minimum values in the list.
numbers = [1,2,3,4,5,6,7,8,9,10]
print(len(numbers))
print(sum(numbers))
print(max(numbers))
print(min(numbers))

# Question 9: Create a nested list called matrix with two sublists: [1, 2, 3] and [4, 5, 6].Access and print the element 5 from the matrix.
matrix =  [[1,2,3,],[4,5,6]]
print(matrix[1][1])

# Question 10: Create a list called random_numbers with elements [7, 2, 5, 1, 8, 3].Sort the list in ascending order.Sort the list in descending order.Print the sorted lists.
random_numbers = [7, 2, 3, 1, 8, 3]
random_numbers.sort()
print(random_numbers)
random_numbers.sort(reverse= True)
print(random_numbers)

# Question 11: Create a list called names with elements ['Alice', 'Bob', 'Charlie'].Use a for loop to print each name in the list.
names = ['Alice', 'Bob', 'Charlie']
for name in names:
    print(name)

# Question 12: Create a list called colors with elements ['red', 'green', 'blue'].Check if 'green' is present in the list and print the result.
colors = ['red', 'green', 'blue']
is_green = 'green' in colors
if is_green:
    print("yes")
else:
    print("no")

# Question 13: Create a list called temperatures with daily temperatures for a week. Calculate and print the average temperature.
tempratures = [5, 12, 55, 25, 27,23, 1]
average_temprature = sum(tempratures)/ 7
print(average_temprature)

# Question 14: Create a list called grades with student grades. Use list comprehension to create a new list named passing_grades that contains only grades greater than or equal to 60.
grades = [50, 70, 90, 60, 14, 20, 25, 99, 88]
passing_grades = [x for x in grades if x >= 60]
print(passing_grades)

# Question 15: Given a list of numbers, create a new list called squared_numbers containing the squares of each number using a for loop.
numbers = [1, 2, 3, 3, 7, 8]
squared_numbers = list()
for x in numbers:
    squared_numbers.append(x**2)
print(squared_numbers)

# Question 16: Create a list called unique_chars that contains only unique characters from the string "programming".
word = 'programming'
unique_chars = list(set(word))
print(unique_chars)

# Question 17: Create a list called mixed_types with elements of different types, such as integers, strings, and booleans. Use list comprehension to create a new list containing only the integers.
mixed_types = ['asa', True, 1.32, 2, 344, 'saafi', 3, '234']
integer_type = [x for x in mixed_types if type(x) == int]
print(integer_type)

# Question 18: Given a list of words, create a new list called long_words that contains words with more than three characters.
words = ['asjkfa', 'sdad', 'this', 'o','op', 'asafda','df']
long_words = [ x for x in words if len(x) > 3]
print(long_words)

# Question 19: Create a list called currencies with elements ['USD', 'EUR', 'JPY']. Use a for loop to print each currency along with its position in the list.
currencies = ['USD', 'EUR', 'JPY']
for cur in range(len(currencies)):
    print(cur,' ', currencies[cur])
    
### Question 20: Create a list called `even_numbers` containing even numbers from 1 to 20 using list comprehension.
even_numbers = [ x for  x in range(1, 20) if x % 2 ==0]
print(even_numbers)

### Question 21:Create a list called `odd_squares` containing the squares of odd numbers from 1 to 10 using list comprehension.
odd_squares = [x**2 for x in range(1,10) if x % 2 !=0]
print(odd_squares)

### Question 22:Given two lists `list1 = [1, 2, 3]` and `list2 = [4, 5, 6]`, concatenate them and then reverse the order of the elements.
list1 = [1, 2, 3]
list2 = [4, 5, 6]
concatenated_list = list1 + list2
concatenated_list.sort(reverse= True)
print(concatenated_list)
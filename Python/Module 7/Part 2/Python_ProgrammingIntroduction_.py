# %%
string = "Hello World!"
print(string)

# %%
x = 3
y = 1
x

# %%
x, y = 3, 1
print(x)
print(y)

# %%
# Always using print() when output is desired is good practice
print(x + y)

# %%
string = "Hello World!"
print(string)
print(strng)

# %%
string_a = 'This is a sentence.'
string_b = "This is a sentence."
print(string_a == string_b)

# %%
string_c = "This is John's script!"
print(string_c)

# %%
FirstName = "John"
LastName = "Snyder"
f"{FirstName} {LastName}"

# %%
FirstName + LastName

# %%
Number = 100
#%%
f"{FirstName} {LastName} is {Number}"
#%%
FirstName + LastName + Number # must use str(Number)

# %%
x = 3
# %%
y = 1
# %%
x > y
# %%
x is not y
# %%
x == y
# %%
y <= x
# %%
not y <= x

# %%
# One Trillion
1_000_000_000_000 == 1000000000000

# %%
# R code
vec <- c(10, 20, 30)
vec

# %%
# Python List
a_list = [10, 20, 30]
# %%
print(a_list)
# %%
print(a_list[2]) # indexing starts at 0!!

# %%
mixed_list = [1, "one", 1.0, [1, 1.0]]
print(mixed_list)
# %%
type(mixed_list)
# %%
type(mixed_list[0])
# %%
type(mixed_list[1])
# %%
type(mixed_list[2])
# %%
type(mixed_list[3])

# %%
a_list = [10, 20, 30, 40, 50, 60]
# %%
a_list[0]
# %%
a_list[1]

# %%
a_list[-1]
# %%
a_list[-2]

# %%
a_list[0:2]

#   0   1   2   3   4   5
# [10, 20, 30, 40, 50, 60]
#  -6  -5  -4  -3  -2  -1

# %%
a_list[1:-2]

# %%
fav_colors = ["Blue","Red","Black","Green","Orange"]
# The  character is a newline
FirstSentence = f"My favorite color is {fav_colors[0]}.\n"
SecondSentence = f"Additionally, I really do not like {fav_colors[-1]}"
print(FirstSentence + SecondSentence)

#%%
print(a_list)
#%%
a_list.append(500) # Most IDEs display a list of methods
#%%
print(a_list)
#%%
a_list.insert(4,800)  # inserts 800 before 4th element
#%%
print(a_list)

#%%
del a_list[0]
print(a_list)

#%%
Names = ["John", "Fred", "Bill", "Joe"]
# %%
print(f"Next up we have {Names.pop()}")
# %%
print(Names)
# %%
print(f"Next up we have {Names.pop()}")
# %%
print(Names)

# %%
print(a_list)
# %%
a_list[2] = 100
print(a_list)

#%%
a_tuple = (10, 20, 30) # () instead of [].
print(a_tuple)

# %%
a_tuple[2]

# %%
a_list_from_tuple = list(a_tuple)
print(a_list_from_tuple)
a_list_from_tuple[2]=100
print(a_list_from_tuple)
#%%
a_tuple[2]=100

#%%
another_list = [5, 6, 7]
print(a_list)
print(a_list + another_list)

#%%
"I" + " am" + " a" + " string"

#%%
a_dict = {'Name': "John", 'Location': "St. Louis"}
print(a_dict)

# %%
HairColor = {"Joe": "Black",
             "Josh": "Red",
             "John": "???"}

# %%
print(HairColor.keys())
# %%
print(HairColor.values())

#%%
my_name = "John"
if my_name == "John":
  print("Hello")

# %%
my_name = "Bill"
if my_name == "John":
  print("Hello")

# %%
if my_name == "John": print("Hello") # also works

# %%
my_name = "TotallyJohn"
if my_name == "John":
 print("Hello John")
else:
  print("Hey! You're not John")

# %%
my_name = "John"

if my_name == "John":
  print("Hello John")
elif my_name == "Bill":
  print("Hello Bill")
else:
  print("Goodbye")

# %%
x, y = 3, 9
# %%
if x == 3 and y > 2:
  print("True!")
# %%
if x == 3 or y < 2:
  print("True!")
# %%
if not x == 3 or y > 2:
  print("True!")
# %%
if not (x == 3 or y > 2):
  print("True!")
# %%
c = 1
while c <= 5:
  print(c)
  c += 1 # Same as c = c + 1

# %%
for <iterator object> in <some collection of elements>:
  < block of code that depends on <iterator object> >

# %%
a_list = [1, 2, 3, 4, 5]
result_list = []

# %%
for x in a_list:
  result_list.append([x, x**2]) # ** is exponentiation

# %%

print(result_list)

# %%
for x in result_list:
  print(f'Element 0 of x is {x[0]}, element 1 is {x[1]}')
  # x is itself a list of length 2
  #sub_list = [x[0], x[1]**(1/2)]
  #print(sub_list)

# %%
for c in range(3):
  print(c)

# %%
for c in range(len(result_list)):
  print(result_list[c])

# %%
my_name = "John Snyder"

for each_letter in my_name:
  #print(each_letter)
  print([each_letter, each_letter.upper()])

# %%
# [<expression> for <variable> in <list>]

FirstNumbers = range(5)
# %%
print(FirstNumbers)
# %%
PerfectSquares = [x**2 for x in FirstNumbers]
# %%
print(PerfectSquares)

# %%
FirstNumbers = range(1, 10)

# %%                                       filter
PerfectSquares = [x**2 for x in FirstNumbers if x % 2 == 0 and x > 0]
# %%    
print(PerfectSquares)

# %%
values = ["a", "b", "c", "d"]
index = 0

# %%
for value in values:
  print(index, value)
  index += 1

# %%
values = ["a", "b", "c", "d"]

for i, val in enumerate(values):
  print(i, val)

# %%
list1 = [1, 2, 3]
list2 = ["one","two","three"]
list3 = ["a","b","c"]
zipped = zip(list1, list2, list3)

# %%
list(zipped)

# %%
zipped = zip(list1, list2, list3)
print(next(zipped))
print(next(zipped))

# %%
zipped = zip(list1, list2, list3)

for li1, li2, li3 in zipped:
  print(li1, li2, li3)
# %%

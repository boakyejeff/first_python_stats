
class cat:             # Define the class and name
  """Modeling a Cat""" # Docstring for describing the class
  # NOTE:  ALL functions defined inside of a class are
  # methods that will follow instances.
  def __init__(self, name2, age2, color2):
    """Initialize cat name and attributes"""
    self.name = name2
    self.age = age2
    self.color = color2

  def scratch(self):
    """Code that simulates a cat scratching a sofa"""
    print(f"{self.name.title()} the {self.color} cat is scratching your sofa!")

  def eat(self, food):
    """Code that simulates a cat eating"""
    print(f"{self.name.title()} is eating {food}!")

my_cat = cat("Butterscotch", 4, "orange")
your_cat = cat("sam", 6, "grey")

your_cat.name
my_cat.age

your_cat.scratch()
my_cat.age
my_cat.eat(food = "tuna")

class cat:
  """Modeling a Cat"""
  def __init__(self, name, age, color):
    """Initialize cat name and attributes"""
    self.name = name
    self.age = age
    self.color = color
    self.sleephrs = 0 # default value assigned, NOT passed by user

  def sleep(self):
    print(f"{self.name.title()} slept for {self.sleephrs} hours today!")

  def update_sleephrs(self, hours):
    # reassigning self.sleephrs changes the value for all other methods!
    self.sleephrs = hours

  def happy_birthday(self):
    print(f"{self.name.title()}, it is your Birthday.  Happy Birthday")
    self.age += 1

my_cat = cat("Butterscotch", 4, "orange")
my_cat.sleephrs
my_cat.update_sleephrs(16)
my_cat.sleephrs

# Happy Birthday
my_cat.age
my_cat.happy_birthday()
my_cat.age

class OneSampleData:
  def __init__(self,dat):
    self.dat = dat

  def mean(self):
    numerator = sum(self.dat)
    denominator = len(self.dat)
    return numerator/denominator

  def var(self, unbiased = True):
    xbar = self.mean()
    numerator = sum([(x - xbar)**2 for x in self.dat])

    if unbiased:
      denominator = len(self.dat) - 1
    else:
      denominator = len(self.dat)

    return numerator/denominator


my_data = OneSampleData([1,2,3,4,5])
my_data.mean()
my_data.var()
my_data.var(unbiased = False)

class OneSampleData:
  unbiased = True               # NOTE: This is a class attribute
  def __init__(self,dat):
    self.dat = dat

  def mean(self):
    numerator = sum(self.dat)
    denominator = len(self.dat)

    return numerator/denominator

  def var(self):
    xbar = self.mean()
    numerator = sum([(x - xbar)**2 for x in self.dat])
    if OneSampleData.unbiased:    #NOTE: CHANGED
      denominator = len(self.dat) - 1
    else:
      denominator = len(self.dat)

    return numerator/denominator

my_data = OneSampleData([1,2,3,4,5])
your_data = OneSampleData([6,7,8,9,10])

my_data.unbiased
your_data.unbiased
my_data.var()

# Change class attribute
OneSampleData.unbiased = False
# Now updated in all EXISTING instances of OneSampleData
my_data.unbiased
your_data.unbiased
my_data.var()

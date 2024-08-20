# Functional Programming solution

integers = [1, 25, 12, 14, 2, 9, 30]

def sort(integers):
    result = sorted(integers)
    return result

print(sort(integers))

# Q1: This function is immutable because it uses a built in python method sorted()
#     which does not alter the original list integers, instead returnig a new list.

# Q2: Yes it is pure as it does not produce any side effects, and only returns the desired result
#     without altering the original list.

# Q3: This is not a higher order function as it does not return another function or
#     accept multiple arguments.

# Q4: No I don't believe another programing style would have been easier to solve this problem.

#Q5: Functional programming was best to solve this problem as it allowed me to create a clean dry function
#    which was designed to solve a single problem.


#-----------------------------------------------------------------------------------------------------------------


# Object Oriented Programming Solution

class Podracer:
    def __init__(self, max_speed, condition, price):
        self.max_speed = max_speed
        self.condition = condition
        self.price = price

    def repair(self):
        if self.condition == "trashed":
            self.condition = "repaired"

class AnakinsPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super().__init__(max_speed, condition, price)
     
    def boost(self):
        self.max_speed = self.max_speed * 2       

class SebulbasPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super().__init__(max_speed, condition, price)
      
    def flame_jet(self, other_podracer):
        if other_podracer.condition == "perfect":
            other_podracer.condition = "trashed"
            
# Test instances

pod1 = Podracer(500, "trashed", 15000)
print(f"Before repair: {pod1.condition}")
pod1.repair()
print(f"After repair: {pod1.condition}")


anakins_pod = AnakinsPod(700, "perfect", 25000)
print(f"Anakin's Pod speed before boost: {anakins_pod.max_speed}")
anakins_pod.boost()
print(f"Anakin's Pod speed after boost: {anakins_pod.max_speed}")


pod2 = Podracer(600, "perfect", 20000)
sebulbas_pod = SebulbasPod(650, "perfect", 30000)

print(f"Pod2 condition before flame_jet: {pod2.condition}")
sebulbas_pod.flame_jet(pod2)
print(f"Pod2 condition after flame_jet: {pod2.condition}")


# Q1A: Encapsulation
#   This solution follows encapsulation as it contains multiple attirubtes
#   wihtin classes which can only be modidied through the class methods I created.

# Q1B: Abstraction
#   This solution has abstraction as a user woud only have to call a given method 
#   on an object such as caling repair on method.

# Q1C: Inheritance
#   Inheritance is present within this solution a the AnakinsPod and SebulbasPod classes 
#   inherit attributes from the broader Podracer class to be manipulated with methods.

# Q1D: Polymorphism
#  Not present in this solution.


# Q2: No it would have been much more difficult to solve this problem with functional programming
#     as it would have required many more functions, repetiton, and manipulation of data to 
#     achieve the same results. 

# Q3: OOP was better to solve this problem as it took a "real" idea which needed to be solved using code
#     and allowed for it to be solved using classes and methods which also allows for the code to be reused
#     and added to for future changes.

# Q4: I do not believe that either of these paradigms are better than the other. Rather It's about applying 
#     a certain paradigm based on the problem you are trying to solve.

# Q5: I believe that OOP is more appealing as it provides a better mindset for someone to 
#     solve for a real world issue.

# Q6: Functional Programming
#      Pure functions, recursion, immutable data handling

#     Object Oriented Programming
#       Encapsulation/state handling, large systems, reusability


# Q7: I believe that it will take more time to understand OOP as it requires a better understanding
#     of how arguments, methods, and functions are passed to one another and determing what is in and out
#     of scope can be difficult at times especially when first learning about OOP.
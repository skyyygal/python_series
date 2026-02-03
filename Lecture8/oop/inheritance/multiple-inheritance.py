"Deriving properties from multiple base class"

class A:
    varA = "Welcome to A"

class B:
    varB = "Welcome to B"

class C(A, B):
    varC = "Welcome to C"

c1 = C()

print(c1.varC)
print(c1.varB)
print(c1.varA)
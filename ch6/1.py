A = "spam"
B = A
B = "TEST"
print(A)

a = ["spam"]
b = a
b[0] = "shrubbery"
print(a)

C = ["SPAM"]
D = C[:]
D[0] = "shrubbery"
print(C)
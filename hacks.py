#Inputing coefficients of the eqaution
a = int(input("Enter a : "))
b = int(input("Enter b : "))
c = int(input("Enter c : "))
#calculating the discriminant
d = ((b**2) - (4*a*c))
#Calculating the root
if d > 0:
 d**=0.5
 r1 = (-b+d)/(2*a)
 r2 = (-b-d)/(2*a)
 print("The roots are real and distinct")
 print("The roots are : {}, {}".format(r1,r2))


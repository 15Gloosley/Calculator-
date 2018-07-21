from math import sqrt
a = "0.0"
b = "0.0"
c = "0.0"
Sides = " "

Sides = str(input("What sides do you have? - Write as 'A and B' or 'A^2 and c^2 (^ meaning to the power to) "))

if Sides == ("A and B") or Sides == ("B and A"):
  a = float(input("What is side a? "))
  b = float(input("What is side b? "))
  c = (a * a) + (b * b)
  c = sqrt(c)
  print("Side 'C' is " + str(c))

if Sides == ("A and C") or Sides == ("C and A"):
  a = float(input("What is side a? "))
  c = float(input("What is side c? "))
  b = (c * c) - (a * a)
  b = sqrt(b)
  print("Side b is " + str(b))

if Sides == ("B and C") or Sides == ("C and B"):
  b = float(input("What is side b? "))
  c = float(input("What is side c? "))
  a = (c * c) - (b * b)
  a = sqrt(a)
  print("Side a is " + str(a))

if Sides == ("A^2 and B^2") or Sides == ("B^2 and A^2"):
  a = float(input("What is your squared side a? "))
  b = float(input("What is your squared side b? "))
  c = (a + b)
  c = sqrt(c)
  print("Side c is " + str(c))

if Sides == ("A^2 and C^2") or Sides == ("C^2 and A^2"):
  a = float(input("What is your squared side a? "))
  c = float(input("What is your squared side c? "))
  b = (c - a)
  b = sqrt(b)
  print("Side b is " + str(b))

if Sides == ("B^2 and C^2") or Sides == ("C^2 and B^2"):
  b = float(input("What is squared side b? "))
  c = float(input("What is squared side c? "))
  a = (c - b)
  a = sqrt(a)
  print("Side a is " + str(a))

if Sides == ("A^2 and B") or Sides == ("B and A^2"):
  a = float(input("What is squared side a? "))
  b = float(input("What is side b? "))
  c = a + (b * b)
  c = sqrt(c)
  print("Side c is " + str(c))

if Sides == ("A^2 and C") or Sides == ("C and A^2"):
  a = float(input("What is squared side A"))
  c = float(input("What is side c? "))
  b = a + (c * c)
  b = sqrt(b)
  print("Side b is " + str(b))

if Sides == ("B^2 and A") or Sides == ("A and B^2"):
  a = float(input("What is side a? "))
  b = float(input("What is squared side b? "))
  c = (a * a) + b
  c = sqrt(c)
  print("Side c is " + str(c))

if Sides == ("B^2 and C") or Sides == ("C and B^2"):
  b = float(input("What is squared side b? "))
  c = float(input("What is side c? "))
  a = (c*c) - b
  a = sqrt(a)
  print("Side a is " + str(a))

if Sides == ("C^2 and A") or Sides == ("A and C^2"):
  a = float(input("What is side a? "))
  c = float(input("What is squared side c? "))
  b = c - (a * a)
  b = sqrt(b)
  print("Side b is " + str(b))

if Sides == ("C^2 and B") or Sides == ("B and C^2"):
  b = float(input("What is side b? "))
  c = float(input("What is squared side c? "))
  a = c - (b * b)
  a = sqrt(a)
  print("Side a is " + str(a))

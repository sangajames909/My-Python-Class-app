try:
  x = 10
  y = 0
  z = x/y
  print(z)
except  ZeroDivisionError:
 print("sorry you cant divide a number by zero")


try:
    file = open("Temwa.docx","w")
    file.write("Hello there, here is our info")
    print("file created")
except IOError:
    print("sorry, we didnt manage creating your file")

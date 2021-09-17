greeting = "Hello class"
print(greeting.upper())
print(greeting.lower())

num = -8/3
print(num)
print(abs(num))

#USER DEFINED FUNCTIONS
def motto():
    print("Hey, this is our motto")

motto()
motto()

def avg(x,y,z):
    answer = (x + y + z)/3
    print("Your answer is ",answer)
avg(20,74,89)
avg(8334,5430,8392)


#create a funtion to allow the user to enter the username and password. On the function, check if the
# username is emobilis and the password is emobilis123. if the credentials the user has submitted match,
# print success, else print fail
def login(username, password):
    if username =="emobilis" and password =="emobilis123":
        print("success")
    else:
        print("fail")
login("emobilis","emobilis123")

#create a function that calculates the BMI of a person
#use the scale below to determine the BMI status
#0 ---------24----- underweight
#24.1--------24.9--------normal weight
#30.0----------34.9----------over weight
#35 and above-----------abuse
# N/B USE the fromula BMI = Weight/height

def bmi(weight,height):
    bmi= weight/(height*height)
    if bmi <= 24:
        print("underweight")
    elif bmi <= 25:
        print("normal weight")
    elif bmi <= 35:
        print("over weight")
    else:
        print("abuse")
bmi(82,6)

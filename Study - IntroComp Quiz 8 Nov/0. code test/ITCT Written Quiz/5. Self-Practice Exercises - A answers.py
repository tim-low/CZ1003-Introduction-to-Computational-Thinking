def pay_calc(no_of_hours):
    if no_of_hours <= 160:
        basic_pay = 10 * no_of_hours
    else:
        basic_pay = (160 * 10) + (no_of_hours - 160)* 15

    if basic_pay <= 1000:
        tax = 0.1 * basic_pay
    elif basic_pay <= 1500:
        tax = 0.1 * 1000 + 0.2 * (basic_pay - 1000)
    else:
        tax = (0.1 * 1000) + (0.2 * 500) + 0.3 * (basic_pay - 1500)
    print ("Gross pay: ", basic_pay)
    print ("Tax: ", tax)
    print ("Net Pay: ", basic_pay - tax)


def pattern_print(n):
    for i in range(n):
        print("*" * (i+1))
    for i in range(n):
        print("*" * (n-i-1))


def passwordcheck():
    strong_password = False
    while not strong_password:
        password = input("Input a password.")
        upper_count = 0
        lower_count = 0
        special_count = 0
        for char in password:
            if char.isupper():
                upper_count += 1
            if char in "!@#$%":
                special_count += 1
        if len(password) < 6 or upper_count < 1 or special_count < 1:
            print("need more than 6, at least one cap, one spec")
        else: strong_password = True
    print("Your passworld is", password)


gradebook = {"FS1":[[1,45],[2,75],[3,25],[4,65]], "FS2":[[1,85],[2,40],[3,70],[4,80]]}

def query():
    group_no = input("enter group no")
    sID = int(input("enter student id"))
    grade = gradebook[group_no][sID-1][1]
    print (grade)



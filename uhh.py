import time

print("you have 500 bucks and the IRS just took 50 bucks")

money = 500
taxes = 50


remaining = money - taxes
print("Remaining balance:", remaining)


if remaining < 500:
    print("Warning: Low on funds!")
else:
    print("Sufficient funds available.")

choice = input("any spendings? (y/n): ").lower()

if choice in ["yes", "y", "ye", "yeah", "yup"]:
    print("Proceeding with the operation...")
else:
    print("Exiting program")
    exit()

spending = float(input("how much? :"))
remaining = remaining - spending
print("Money left = ", remaining)

if remaining < 150:
    print("Low balance")
else:
    print("we got enough gng")
    time.sleep(2)
    print("you seem to running low")
    time.sleep(1)
    print("i'd wise up if i were you gng")

choice = input("any earnings man? (Y/N)")

if choice in ["yes", "y", "ye", "yeah", "yup"]:
    print("Proceeding with the operation...")
else:
    print("Exiting program")
    exit()

time.sleep(2)

print("ouu shii")

time.sleep(1)

earning = float(input("how much? :"))

remaining = remaining + earning

print("Money left = ", remaining)

if remaining > 300:
    print("ouu shii we rich twin")
else:
    print("yo dude you're cooked")
    time.sleep(1)
    print("get yo money up not your funny up gng")
    time.sleep(2)
    exit()

print ("okay you still a chance")
time.sleep(2)
choice

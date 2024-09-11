print("")
print("")

print("Welcome to the Guessing Game! Enter a number and I will try to guess it!")
print("")
num = str(input("Pick a number: "))
if(num.isnumeric()):
    print("Is your number " + num + "?")
else:
    print("Nice try! That's not a number, but did you enter: " + num + "?")

print("I must've just gotten a luck guess!")
print("Just kidding, this program is being uploaded for the purpose of learning how to use Git. I just wanted to make you think I was a good guesser")
print("Have a great rest of your day!")

print("This text line is used to show conflict when two people try to make changes to the same line.")

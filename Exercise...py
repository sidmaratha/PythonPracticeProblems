a = int(input("Enter the number\n"))
if a == 99:
    print("You got %d " % a)
elif a >= 90:
    print("You got %d so that you got A grade" % a)
elif a >= 80:
    print("You got %d so that you got B+ grade" % a)
elif a >= 70:
    print("You got %d so that you got B grade" % a)
elif a >= 60:
    print("You got %d so that you got C+ grade" % a)
elif a >= 50:
    print("You got %d so that you got C grade" % a)
elif a >= 40:
    print("You got %d so that you got D+ grade" % a)
elif a >= 35:
    print("You got %d so that you got D grade" % a)
else:
    print("YOU got no marks")

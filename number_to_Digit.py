# The Numbers Convert into Digits:
# creating dictonary
words = {0:"zero", 1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six",
         7:"seven", 8:"eight", 9:"nine", 10:"ten", 11:"eleven", 12:"tewelve",
         13:"thirteen", 14:"fourteen", 15:"fifteen", 16:"sixteen", 17:"seventeen",
         18:"eighteen", 19:"ninteen", 20:"twenty", 30:"thirty", 40:"fourty", 50:"fifty",
         60:"sixty", 70:"seventy", 80:"eighty", 90:"ninty", 100:"Hundred"}

#Take input from user
number = input("enter number [0-100] : ")
#converting string to number
strToNumbr = eval(number)
#validate
if strToNumbr >=0 and strToNumbr <=100:
    #logic
    #check user entered value is already available or not
    if strToNumbr in words:
        print(words.get(strToNumbr))
    # if user entered value not available in "words" variable
    else:
        #logic
        remainder = strToNumbr % 10
        Coefficiant = int(strToNumbr / 10) * 10
        print(words.get(Coefficiant), words.get(remainder))
else:
    print("value should be [0-100] only")

n=1234 #variable for 3rd program
x=5678 #variable for 3rd program
l=13.42 #variable for 4rd program
j=42.13 #variable for 4rd program
#1st program

def FirstProgram(): #function which prints out final number from equation
    print(9**0.5*5)a
    global R
    R = 1
    #return print("☺")
FirstProgram()

#2nd program
def SecondProgram(): #function which prints out if 9.99 is greater than 9.98 and where 1000 is not equal to 1000.1
    print(9.99 > 9.98 and 1000 != 1000.1)
    global E
    E = 1
    #return print("☺")
SecondProgram()

#3rd program
def ThridProgram(n,x): #function which takes 2 arguments and if n is equal to 1234 and x is equal to 5678 then it makes left and right number disappear and then prints out 90 if n is equal to 23 and x is equal to 67 and prints it out to the console
    if n == 1234: #condition for n if it's 1234
        n=n%1000
        n=n//10
        print("n is",n)
    if x == 5678: #condition for x if it's 5678
        x=x%1000
        x=x//10
        print("x is",x)
    if n == 23 and x == 67: #if condition n is 23 and x is 67 is met then it will print 90 cause 23+67=90.
        print(n+x)
        global W
        W = 1
        #return print("☺")
ThridProgram(n,x)

#4th program
def FourthProgram(l,j):
    li,ji = int(l), int(j)
    lf,jf = int((l-li)*100), int((j-ji)* 100) #lf=(13,42-13)*100=0.42*100=int(41.999?)?? use integer type so it would be 42, jf =(42.13 - 42) * 100 = 0.13 * 100 = 13
                                              # print(int(41.999999999999999)) #it looks like you need 15 nines so it rounds up to 42
    J=(li == jf or ji == li) #compare li if its equal to jf or if ji equal to li
    if J == True:
        print(li == jf or ji == li)
        global Q
        Q = 1
        #return print("☺")



FourthProgram(l,j)

if Q and W and E and R == 1:
    print("All tasks done successfully! ♦○♦")
else:
    print("Something is wrong ☻")
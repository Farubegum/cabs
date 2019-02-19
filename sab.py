print("welcome to cabs")

a = input("enter ur location ")

b = input("enter ur  destination ")

print ("press 1 for mini")

print ("press 2 for micro")

print ("press 3 for prime")

print ("press 4 for swedan")

c = int(input("Enter choice(1/2/3/4):"))

if c ==1:

  distance = int(input("How long is the journey to your desired destination?"))

  start = 1.20

  if distance <=10:

    print ("the total journey price will be " + str((distance*0.7)+start))

  else: 
    print ("the total of the journey will be " + str((((distance - 10)*30)+8.20)))

elif c==2:

  distance = int(input("How long is the journey to your desired destination?"))

  start = 1.90

  if distance <=10:

    print ("the total journey price will be " + str((distance*0.9)+start))

  else:
    print ("the total of the journey will be " + str((((distance - 10)*35)+9.10)))

elif c==3:

  distance = int(input("How long is the journey to your desired destination?"))

  start = 2.0

  if distance <=10:

    print ("the total journey price will be " +  str((distance*1.3)+start))

  else:
    print ("the total of the journey will be " + strt((((distance - 10)*40)+9.30)))

elif c==4:

  distance = int(input("How long is the journey to your desired destination?"))  

  start = 2.3

  if distance <=10:

    print ("the total journey price will be " + str((distance*1.4)+start))

  else:
    print ("the total of the journey will be " + str((((distance - 10)*45)+9.30)))

else :

    print ("select valid")

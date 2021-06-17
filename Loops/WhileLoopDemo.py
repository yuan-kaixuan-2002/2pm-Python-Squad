#When the argument in the parathesis of the while loop is true, the loop runs, when the argument is false, loop stops

#This loop will print Hello 5 times
counter = 0
while(counter<5):
  print("Hello")
  counter += 1
  
#This is a while True loop, it will run forever until an action breaks, or stops the loop
# in this case, entering 1 into the console stops the loop

while(True):
  ans = input("press 1 to stop the loop")
  if(ans == "1"):
    break
    
  

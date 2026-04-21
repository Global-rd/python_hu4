import time 
while True:
    answer = input("Do you want to be a professional python developer? yes/no")
    if answer in ["yes", "no"]:
        break

#while True:
#    print("infinite loop")
#    time.sleep(1)
    

count = 0

while count < 5:
    print(count)
    count += 1

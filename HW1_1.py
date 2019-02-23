midnight_second = int(input("Enter seconds from midnight: "))

hour = midnight_second // 3600
minute = (midnight_second % 3600) // 60
second = (midnight_second % 3600) % 60

print("Time in military format is: ","%02d" % hour,":","%02d" % minute,":","%02d" % second,sep='')
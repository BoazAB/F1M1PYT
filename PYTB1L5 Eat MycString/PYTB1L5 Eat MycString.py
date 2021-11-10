import time
print("Wat moet ik eten?")
s = input()

while True:
 time.sleep(1)
 ss = s[0:len(s)-1]
 s = ss
 print(ss)
 if len(ss) == 0:
     break
 else:
     continue
print("Lekker hoor")
exit()
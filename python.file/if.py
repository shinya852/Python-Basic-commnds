score = 90
if score >= 80:
    print("やったね！")
    print("次もこの調子")

score = 60
if score >= 80:
    print("やったね！")
    print("次もこの調子")
else:
    print("残念でした")

for i in range(10):
    print(5, "X",i, "=",5*i)

scorelist = [64, 100, 78, 80, 72]
for i in scorelist:
    print(i)
    
scorelist = [64, 100, 78, 80, 72]
total = 0
for i in scorelist:
    total = total + i
print(total)

for i in range(10):
    for j in range(10):
        print(j, "x", i, "=", j*i)
        

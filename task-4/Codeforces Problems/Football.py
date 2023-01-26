situation = input()
dangerous = "NO"
count = 1
for i in range(1, len(situation)):
    if situation[i] == situation[i-1]:
        count += 1
        if count == 7:
            dangerous = "YES"
            break
    else:
        count = 1
print(dangerous)
n, k = map(int, input().split())
scores = list(map(int, input().split()))
advancers = 0
for i in range(n):
    if scores[i] > 0 and scores[i] >= scores[k-1]:
        advancers += 1
print(advancers)
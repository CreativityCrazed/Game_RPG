price = int(input())
count=0

while price > 0:
    if price >= 25:
        price-=25
    elif price >= 10:
        price-=10
    elif price >= 5:
        price-=5
    else:
        price-=1
    count+=1

print(count)  
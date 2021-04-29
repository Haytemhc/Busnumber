length = int(input())
buses = list(map(int, input().rstrip().split(" ")))
    
buses.sort()

answer = [str(buses[0])]
temp = buses[0]
count = 1
for i in range(length-1):
    if(temp + count) == buses[i+1]:
        if(count >= 2):
            answer.pop()
            answer.append("-" + str(buses[i+1]))
        else:
            answer.append(" " + str(buses[i+1]))
        count += 1
    else:
        temp = buses[i + 1]
        count = 1
        answer.append(" " + str(temp))

print("".join(answer))

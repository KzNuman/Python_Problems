s,t,f = map(int,input().split())

arrival_time = (s+t+f) % 24

arrival_time = 0 if arrival_time == 24 else arrival_time


# partion if else condition as usual ▼↓ 

# if arrival_time == 24:
#     arrival_time = 0 
# else:
#     arrival_time = arrival_time

print(arrival_time)

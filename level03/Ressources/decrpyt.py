r = "Q}|u`sfg~sf{}|a3"

i = 0
# first letter to find.
while(i < 322424845):
    t = ord("Q") ^ i
    if (chr(t) == "C"):
        print(i)
        break
    i = i + 1

r = "Q}|u`sfg~sf{}|a3"

for l in r:
    print(chr(ord(l) ^ i), end="")
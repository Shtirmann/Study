n = int(input("Введите число: "))
for i in range (-n+1, n):
    for j in range (-n+1, n):
        if abs(j)+1 >=n-abs(i):
            print (chr(64+(n-abs(j))), end=" ")
    else:
        print("  ", end="")
print("")
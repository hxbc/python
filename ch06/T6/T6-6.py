s=raw_input("enter something:")
print(list(s))
for i in range(0,len(s)):
    if s[i]!=" ":
        num1=i
        print num1
        break

s1=s[::-1]
print(list(s1))
for x in range(len(s1)):
    if s1[x] != " ":
        num2=x
        print num2
        break


ss=s[num1:len(s)-x]

print ss
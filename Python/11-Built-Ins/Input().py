# Enter your code here. Read input from STDIN. Print output to STDOUT
x, k = list(map(int, input().split()))
p = input()
if eval(p) == k:
    print(True)
else:
    print(False)

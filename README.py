# A.-Array-with-Odd-Sum
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    has_odd = any(i % 2 == 1 for i in a)
    has_even = any(i % 2 == 0 for i in a)
    if has_odd == 0:
        print("NO")
    if has_even == 0 and len(a) % 2 == 0:
        print("NO")
    elif has_even == 0 and len(a) % 2 != 0:
        print("YES")
    if has_odd > 0 and has_even > 0:
        print("YES")

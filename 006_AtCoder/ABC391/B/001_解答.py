N = int(input())

# 1から9までの約数を求める
one_digit_divisors = []
for i in range(1, 10):
    if N % i == 0:
        one_digit_divisors.append(i)

# 答えを求める
ans = []
for i in range(N + 1):
    t = "-"
    for divisor in one_digit_divisors:
        if i % (N // divisor) == 0:
            t = str(divisor)
            break
    ans.append(t)
print("".join(ans))

# 논리형 boolean

a = True
b = False
print(a, type(a))
print(b, type(b))

# 비교 연산
# A > B : A가 B보다 크면 Ture, 아니면 False
# 같으면 False
# A >= B : A가 B 이상이면 Ture, 아니면 False
# A < B
# A <= B
# A == B : A, B가 같으면 Ture, 아니면 False
# A != B : A, B가 같지 않으면 Ture, 아니면 False

print("1 > 0.5:", 1 > 0.5)    # Ture
print("1 < 0.5:", 1 < 0.5)    # False
print("1 >= 0.5:", 1 >= 0.5)  # Ture
print("1 <= 0.5:", 1 <= 0.5)  # False
print("1 == 1:", 1 == 1)      # Ture
print("1 != 1:", 1 != 1)      # False

# 논리 부정 연산(not)
print(True)
print(not True)
print(not not True)
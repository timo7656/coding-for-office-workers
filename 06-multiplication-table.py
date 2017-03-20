# 1)사용자로부터 몇 단을 출력할지 받을 것
# num = int(input("몇 단을 출력 하시겠습니까? "))

# 2) 해당 단을 곱하기 1에서 곱하기 9까지 실행할 것
# a=1
# while a<10 :
#     p = int(num) * a
#     print(int(num), "*", a, "=", p)
#     a = a+1
num_b = 1
while num_b == 1:
    num = int(input("몇 단을 출력 하시겠습니까? "))
    if num <= 9 and num >= 2:
        num_b = 2
    else :
        print("2에서 9사이의 숫자를 입력해주세요")

a = 1
for a in range(1,10):
    print("{} * {} = {}".format(num, a, num*a))
    a = a + 1
#
# for a in range (1,10):
#     print("{} * {} = {}".format(num,a,num*a))
#     a = a +1

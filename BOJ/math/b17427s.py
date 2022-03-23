n = int(input())

# 하나씩 접근하게 된다면 무조건 시간초과 오류가 발생한다.
# 루트를 이용하는 방법도 시간초과를 발생시킨다.
# 따라서 우리는 배수를 이용해야한다.

'''
3의 배수 : 3, 6, 9, 12, 15, ... 3의 배수들은 모두 3을 포함하고 있다.
만약 N이 6이라면, N//3 = 2이니 N까지 3은 2번 등장한다.
만약 N이 9라면, N//3 = 3이니 N까지 3은 3번 등장한다.

3의 배수가 아닌 N을 생각해보자.
만약 N이 11이라면, N//3 = 3이니 어쨌든 N까지 3은 3번 등장한다. (3, 6, 9)
'''

resultSum = 0

for i in range(1,n+1):
    resultSum += (n//i)*i
print(resultSum)
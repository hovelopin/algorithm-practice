def solution(n, arr1, arr2):
    answer = []

    for i in range(n):
        tmp = bin(arr1[i] | arr2[i])[2:]
        print(tmp)
        tmp = tmp.zfill(n)
        tmp = tmp.replace('1', '#').replace('0', ' ')
        answer.append(tmp)

    return print(answer)

solution(6 , [46, 33, 33 ,22, 31, 50] , [27 ,56, 19, 14, 14, 10])
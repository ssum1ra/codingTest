def solution(friends, gifts):
    answer = 0
    graph = [[0] * len(friends) for _ in range(len(friends))]
    
    for gift in gifts:
        print(gift)
        a, b = gift.split()
        i = friends.index(a)
        j = friends.index(b)
        graph[i][j] += 1
                
    return answer

import sys
input = sys.stdin.readline

friends = input()
gifts = input()

print(friends)
print(solution(friends, gifts))
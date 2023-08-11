def solution(n, words):

    spoken = []

    end = False

    for i, word in enumerate(words):
        
        if word not in spoken:

            if i == 0:
                spoken.append(word)
            else:
                if spoken[-1][-1] == word[0]:
                    spoken.append(word)
                else:
                    error = i
                    end = True
                    break
            
        else:
            error = i
            end = True
            break

    if end == True:
        answer = [error % n + 1, error // n +1]
    else:
        answer = [0, 0]
        
    return answer


n = 3
words = ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]

print(solution(n, words))

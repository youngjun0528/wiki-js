def solution(answers):
    answer = []
    
    first = [1,2,3,4,5]
    second = [2,1,2,3,2,4,2,5]
    third = [3,3,1,1,2,2,4,4,5,5]
    
    if len(answers) > len(first):
        first = first*(int(len(answers)/len(first)) + 1)
    if len(answers) > len(second):
        second = second*(int(len(answers)/len(second)) + 1)
    if len(answers) > len(third):
        third = third*(int(len(answers)/len(third)) + 1)
        
    first_result = 0
    second_result = 0
    third_result = 0
    
    for i in range(len(answers)):
        if answers[i] == first[i]:
            first_result = first_result + 1
        if answers[i] == second[i]:
            second_result = second_result + 1
        if answers[i] == third[i]:
            third_result = third_result + 1
    print(first_result, second_result, third_result)
    
    result_arr = [first_result, second_result, third_result]

    result_cnt = max(result_arr)

    if first_result == result_cnt:
        answer.append(1)
    if second_result == result_cnt:
        answer.append(2)
    if third_result == result_cnt:
        answer.append(3)
        
    return answer
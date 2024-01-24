def solution(array):
    answer = 0
    array.sort()
    if array[len(array) // 2] :
      answer = array[len(array)]
    return answer
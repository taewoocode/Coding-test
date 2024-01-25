def solution(my_string):
    answer = ''
    m = ('a','e','i','o','u')
    for i in range(0,len(my_string)):
      if my_string[i] != m:
        answer += my_string[i]
    return answer
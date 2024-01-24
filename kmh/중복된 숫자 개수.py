 # 방법1)
 # def solution(array, n):
 # # answer = array.count()
  
# 방법2)
def solution(array, n):
  answer = 0
  for i in array:
    if i == n:
      answer += 1
    
  return answer
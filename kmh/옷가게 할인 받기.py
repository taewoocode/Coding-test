def solution(price):
    answer = 0
    if price >= 100000 and price:
      anwser = price-(price * 0.05)
    elif price >= 300000:
      anwser = price - (price * 0.1)
    else:
      anwser = price - (price * 0.2)
    return answer
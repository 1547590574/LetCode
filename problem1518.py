def numWaterBottles(numBottles: int, numExchange: int) -> int:
    count = 0
    while numBottles >= numExchange:
        a = numBottles % numExchange  # 剩下多少瓶
        count += numBottles - a  # 只喝能被整除的部分，不能的留着下次与新兑换的一起喝，这样方便计数
        numBottles = a + numBottles // numExchange
        print(numBottles, count)
    count += numBottles  #由于剩下几瓶不能换，直接跳出循环，这里需要将其重新加上去
    return count


print(numWaterBottles(15, 4))

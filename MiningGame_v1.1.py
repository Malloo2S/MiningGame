import random as r
import numpy as np

minerals = ["흙:0", "돌:1", "석탄:2", "부싯돌:3", "호박:4", "철:5", "석영:6", "금:8", "청금석:11", "사파이어:12", "루비:14", "토파즈:16", "에메랄드:18", "다이아몬드:20", "말라이트:30"]
myMinerals = []
mineLV = 2
sellbuy = 0

def Mining():
    probability = []
    divide = 100
    for _ in range(mineLV//2):
        divide/=2
        probability.append(divide/100)
    probability.insert(0, 1-sum(probability))
    randomMineral = np.random.choice(minerals[:(mineLV//2)+1], p=probability)
    print(randomMineral.split(":")[0] + "을/를 얻었다!")
    myMinerals.append(randomMineral.split(":")[0])


def Sell():

    if myMinerals != None:
        global sellbuy

        sum = 0
        for i in range(len(minerals)):
            sum += myMinerals.count(minerals[i].split(":")[0]) * int(minerals[i].split(":")[1])

        sellbuy += sum
        myMinerals.clear()
        print("당신은 " + str(sum) + "셀바이를 벌었습니다.")
        print("셀바이:" + str(sellbuy))

def MineUpgrade():
    global mineLV
    global sellbuy

    if mineLV == 27:
        print("광산 레벨 한도에 달했습니다.")
    elif sellbuy >= mineLV * 5:
        sellbuy -= mineLV * 5
        mineLV += 1
        print("광산 레벨이 " + str(mineLV) + "이/가 되었습니다.")
    else:
        print("셀바이가 부족합니다.")

while True:
    i = input().lower()
    if i == "m":
        Mining()
        
    if i == "s":
        Sell()
    if i == "mu":
        MineUpgrade()
    if i == "sb":
        print("셀바이:" + str(sellbuy))
    if i == "ml":
        print("광산 레벨:" + str(mineLV))
        print("현재 얻을 수 있는 광물 :")
        for i in range(mineLV//2+1):
            print(minerals[i].split(":")[0])
    if i == "nm":
        print("다음 광산 가격:" + str(mineLV * 5))
    if i == "inv":
        for i in range(len(minerals)):
            print(minerals[i].split(":")[0] + ":" + str(myMinerals.count(minerals[i].split(":")[0])))
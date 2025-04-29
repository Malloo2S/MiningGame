import random as r

minerals = ["돌", "석탄", "부싯돌", "호박", "철", "석영", "금", "청금석", "사파이어", "루비", "토파즈", "에메랄드", "다이아몬드", "말라이트"]
myMinerals = []
mineLV = 1
sellbye = 0

def Mining():
    global mineLV

    randomMineral = r.randint(0, mineLV // 2)
    print(minerals[randomMineral] + "를/을 얻었다!")
    myMinerals.append(minerals[randomMineral])
def Sell():

    if myMinerals != None:
        global sellbye

        sum = 0
        sum += myMinerals.count("돌")
        sum += myMinerals.count("부싯돌") * 2
        sum += myMinerals.count("석탄") * 3
        sum += myMinerals.count("호박") * 4
        sum += myMinerals.count("철") * 5
        sum += myMinerals.count("석영") * 6
        sum += myMinerals.count("금") * 8
        sum += myMinerals.count("청금석") * 11
        sum += myMinerals.count("사파이어") * 12
        sum += myMinerals.count("루비") * 14
        sum += myMinerals.count("토파즈") * 16
        sum += myMinerals.count("에메랄드") * 18
        sum += myMinerals.count("다이아몬드") * 20
        sum += myMinerals.count("말라이트") * 50

        sellbye += sum
        myMinerals.clear()
        print("당신은 " + str(sum) + "셀바이를 벌었습니다.")
        print("셀바이:" + str(sellbye))

def MineUpgrade():
    global mineLV
    global sellbye

    if sellbye >= mineLV * 30:
        sellbye -= mineLV * 30
        mineLV += 1
        print("광산 레벨이 " + str(mineLV) + "이/가 되었습니다.")
    else:
        print("셀바이가 부족합니다.")

while True:
    i = input()
    if i == "m":
        Mining()
    if i == "s":
        Sell()
    if i == "mu":
        MineUpgrade()
    if i == "sb":
        print("셀바이:" + str(sellbye))
    if i == "ml":
        print("광산 레벨:" + str(mineLV))
    if i == "nm":
        print("다음 광산 가격:" + str(mineLV * 30))
    else:
        for x in range(i.count("mz")):
            Mining()
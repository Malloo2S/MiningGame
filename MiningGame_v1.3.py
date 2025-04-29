import random as r
import numpy as np
import time as t
import os
import colorama as c

c.init(True)

minerals = ["흙:1", "돌:1.5", "부싯돌:5", "석탄:10", "호박:26", "철:37", "석영:48", "금:55", "청금석:60", "사파이어:72", "루비:83", "토파즈:100", "에메랄드:150", "다이아몬드:200", "말라이트:500"]
myMinerals = []
pickaxes = [["나무 곡괭이",0,3,999999], ["돌 곡괭이",50,2,60], ["철 곡괭이",150,1,80], ["합금 곡괭이",300,0,50,], ["금강석 곡괭이",500,0.2,100,], ["말라이트 곡괭이",1000,0,500]]
myPickaxe = ["나무 곡괭이",0,3,999999]
mineLV = 2
sellbuy = 0

def Mining():
    global myPickaxe
    print("곡괭이의 남은 내구도 : " + str(myPickaxe[3]))
    probability = []
    divide = 100
    for _ in range(mineLV//2):
        divide/=2
        probability.append(divide/100)
    probability.insert(0, 1-sum(probability))
    randomMineral = np.random.choice(minerals[:(mineLV//2)+1], p=probability)
    print(randomMineral.split(":")[0] + "을/를 얻었다!")
    myMinerals.append(randomMineral.split(":")[0])
    if myPickaxe[3] <= 0:
        myPickaxe = []
        print("곡괭이가 부서졌다.")
    else:
        myPickaxe[3] -= 1

def Sell():

    if myMinerals != None:
        global sellbuy

        sum = 0
        for i in range(len(minerals)):
            sum += myMinerals.count(minerals[i].split(":")[0]) * float(minerals[i].split(":")[1])

        sellbuy += sum
        myMinerals.clear()
        print("당신은 " + str(sum) + "셀바이를 벌었습니다.")
        print("셀바이:" + str(sellbuy))

def MineUpgrade():
    global mineLV
    global sellbuy

    if mineLV == 28:
        print("광산 레벨 한도에 달했습니다.")
    elif sellbuy >= mineLV * 10:
        sellbuy -= mineLV * 10
        mineLV += 1
        print("광산 레벨이 " + str(mineLV) + "이/가 되었습니다.")
    else:
        print("셀바이가 부족합니다.")

while True:
    i = input().lower()
    if i == "m":
        if myPickaxe != []:
            for i in range(5):
                print(c.Fore.GREEN + "■", end="")
                t.sleep(myPickaxe[2]/5)
            print(c.Fore.WHITE)
            Mining()
            
        else:
            print("곡괭이가 없습니다.")
    if i == "s":
        Sell()
    if i == "mu":
        MineUpgrade()
    if i == "sb":
        print("셀바이:" + str(sellbuy))
    if i == "st":
        print("무엇을 사시겠습니까?")
        for thing in pickaxes:
            print(thing[0] + " : " + str(thing[1]))
        a = input()
        for i in range(len(pickaxes)):
            if a == pickaxes[i][0]:
                if sellbuy >= pickaxes[i][1]:
                    sellbuy -= pickaxes[i][1]
                    print("구매완료!")
                    myPickaxe = pickaxes[i]
                    break
                else:
                    print("셀바이가 부족합니다.")
    if i == "ml":
        print("광산 레벨:" + str(mineLV))
        print("현재 얻을 수 있는 광물 :")
        for i in range(mineLV//2+1):
            print(minerals[i].split(":")[0])
    if i == "nm":
        print("다음 광산 가격:" + str(mineLV * 10))
    if i == "inv":
        print(myPickaxe[0] + "\n내구도 : " + str(myPickaxe[3]))
        for i in range(len(minerals)):
            print(minerals[i].split(":")[0] + ":" + str(myMinerals.count(minerals[i].split(":")[0])))
    if i == "save":
        file_name = input("추가할 또는 갱신할 파일명을 입력하세요.(.txt 붙이지 마세요.)")
        with open(file_name +".txt", "w") as file:
            file.write(str(sellbuy) + "/" + str(mineLV) + "/" + str(myPickaxe))
            print("추가/갱신 완료!")
    if i == "load":
        file_name = input("로드할 파일명을 입력하세요.(.txt 붙이지 마세요.)")
        if os.path.exists(file_name + ".txt"):
            with open(file_name + ".txt", "r", encoding="UTF8") as file:
                load = file.readline().split("/")
                sellbuy = float(load[0])
                mineLV = int(load[1])
                myPickaxe = load[2].split(":")
                myPickaxe[1] = int(myPickaxe[1])
                myPickaxe[2] = int(myPickaxe[2])
                myPickaxe[3] = int(myPickaxe[3])
                print("로드 완료!")
        else:
            print("지정한 파일이 없습니다.")
    if i == "delete":
        file_name = input("삭제할 파일명을 입력하세요.(.txt 붙이지 마세요.)")
        if os.path.exists(file_name + ".txt"):
            os.remove(file_name + ".txt")
            print("삭제 완료!")
        else:
            print("지정한 파일이 없습니다.")
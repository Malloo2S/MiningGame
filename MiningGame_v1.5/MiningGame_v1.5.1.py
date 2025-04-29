import random as r
import numpy as np
import time as t
import os
import colorama as c
from math import *

c.init(True)

auto_miner = []
minerals = ("흙:1.5", "돌:2.5", "부싯돌:5", "석탄:10", "호박:26", "철:37", "석영:48", "금:55", "청금석:60", "사파이어:72", "루비:83", "토파즈:100", "에메랄드:150", "다이아몬드:200", "말라이트:500", "레어 흙:4.5", "레어 돌:7.5", "레어 부싯돌:15", "레어 석탄:30", "레어 호박:78", "레어 철:111", "레어 석영:144", "레어 금:165", "레어 청금석:180", "레어 사파이어:216", "레어 루비:249", "레어 토파즈:300", "레어 에메랄드:450", "레어 다이아몬드:600", "레어 말라이트:1500")
RF_stone = 0
myMinerals = []
pickaxes = ("나무 곡괭이,0,3,999999,1", "돌 곡괭이,50,2,100,2", "철 곡괭이,150,1,150,3", "합금 곡괭이,300,0,50,5", "금강석 곡괭이,500,0.2,200,5", "말라이트 곡괭이,1000,0,500,10")
myPickaxe = ["나무 곡괭이",0,3,999999,1]
reforge = []
mineLV = 2
sellbuy = 0

class Auto_Miner():
    def __init__(self):
        self.level = 1
        self.start = t.time()

    def Speed(self):
        return 11 - self.level
    
    def Upgrade(self):
        global sellbuy
        if self.level == 10:
            print("최고 레벨 입니다.")
        else:
            if sellbuy >= self.level * 10:
                sellbuy -= self.level * 10
                self.level += 1
                print("업그레이드 완료!")
            else:
                print("셀바이가 부족합니다.")
    
    def Mineral(self):
        repeat = int(floor(t.time() - self.start) / (11-self.level) * self.level)
        for i in range(repeat):
           Mining(False)
        print(str(repeat) + "개의 광물을 얻었다!")
        self.start = t.time()

def Mining(isPlayer:bool):
    probability = []
    divide = 100
    for _ in range(mineLV//2):
        divide = divide / 2
        probability.append(divide/100)
    probability.insert(0, 1-sum(probability))
    randomMineral = np.random.choice(minerals[:(mineLV//2)+1], p=probability)
    if isPlayer:
        print(randomMineral.split(":")[0] + "을/를 얻었다!")
    myMinerals.append(randomMineral.split(":")[0])

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

def PickaxeStore():
    global sellbuy
    global myPickaxe
    print("무엇을 사시겠습니까?")
    for thing in pickaxes:
        print(thing.split(",")[0] + " : " + thing.split(",")[1] + "셀바이")
    a = input()
    no = 0
    for i in range(len(pickaxes)):
        if a == pickaxes[i].split(",")[0]:
            if sellbuy >= int(pickaxes[i].split(",")[1]):
                sellbuy -= int(pickaxes[i].split(",")[1])
                print("구매완료!")
                myPickaxe = pickaxes[i].split(",")
                myPickaxe[1] = int(myPickaxe[1])
                myPickaxe[2] = float(myPickaxe[2])
                myPickaxe[3] = int(myPickaxe[3])
                myPickaxe[4] = int(myPickaxe[4])
                break
            else:
                print("셀바이가 부족합니다.")
        else:
            no+=1
    if no == 6:
        print("그 물건은 없습니다.")

def ReforgeStoneStore():
    global sellbuy
    global RF_stone
    a = input("재련석을 사시겠습니까?(100셀바이,네/아니오)")
    if a == "네":
        if sellbuy >= 100:
            sellbuy -= 100
            RF_stone += 1
            print("구매 완료!")
        else:
            print("셀바이가 부족합니다.")

def Reforge():
    global reforge
    global RF_stone
    a = input("reforge = 재련\nstate = 현재 재련도\n")
    if a == "reforge":
        if RF_stone >= 1:
            a = input("무슨 광물을 재련 하시겠습니까?")
            yes = False
            for i in range(len(myMinerals)):
                if myMinerals[i] == a:
                    del myMinerals[i]
                    yes = True
                    break
            if yes:
                RF_stone -= 1
                reforge.clear()
                reforge += [a,t.time()]
                print("재련중...(5분)")
            else:
                print("지정한 광물이 없습니다.")
        else:
            print("재련석이 없습니다.")
    if a == "state":
        if reforge != []:
            print(("*"*10) + "현재 재련 상태" + ("*"*10))
            print("재련 대상:" + reforge[0])
            time = t.time() - reforge[1]
            if time >= 300:
                time = "완료!"
            else:
                time = 300 - time
                time = str(int(time//60)) + "분" + str(round(time%60,1)) + "초"
            print("남은 시간:" + time)
            if time == "완료!":
                if input("회수하시겠 습니까?(네/아니오)") == "네":
                    myMinerals.append("레어 " + reforge[0])
        else:
            print("재련 중인 광물이 없습니다.")

def AutoMiner():
    global sellbuy
    global auto_miner
    i = input("summon = 새로운 마이너 소환하기(50셀바이)\nupgrade = 마이너 업그레이드하기(레벨당 *10)\ntake = 마이너 광물 회수하기\n")
    if i == "summon":
        if sellbuy >= 50:
            sellbuy-=50
            auto_miner.append(Auto_Miner())
            print("소환 완료!")
        else:
            print("셀바이가 부족합니다.")
    if i == "upgrade":
        if auto_miner != []:
            for i in range(len(auto_miner)):
                print(str(i+1) + "번 마이너-레벨:" + str(auto_miner[i].level))
        else:
            print("현재 마이너가 없습니다.")
            return
        n = int(input("업그레이드할 마이너의 번호를 입력하세요."))
        if n > len(auto_miner):
            print("그 번호의 마이너는 없습니다.")
        else:
            auto_miner[n-1].Upgrade()
    if i == "take":
        if auto_miner != []:
            for i in range(len(auto_miner)):
                print(str(i+1) + "번 마이너-레벨:" + str(auto_miner[i].level))
        else:
            print("현재 마이너가 없습니다.")
            return
        n = int(input("회수할 마이너의 번호를 입력하세요."))
        if n > len(auto_miner):
            print("그 번호의 마이너는 없습니다.")
        else:
            auto_miner[n-1].Mineral()

def Save():
    file_name = input("추가할 또는 갱신할 파일명을 입력하세요.(.txt 붙이지 마세요.)")
    if os.path.exists(file_name + ".txt"):
         os.remove(file_name + ".txt")
    with open(file_name +".txt", "w", encoding="UTF8") as file:
        file.write(str(sellbuy) + "/" + str(mineLV) + "/")
        if myPickaxe != []:
            file.write(myPickaxe[0] + ":")
            for i in range(3):
                file.write(str(myPickaxe[i+1])+":")
            file.write(str(myPickaxe[4]) + "/")
        else: file.write("None/")
        if reforge == []:
            file.write("None" + "/" + str(len(auto_miner)))
        else:
            file.write(reforge[0] + "/" + str(reforge[1]) + "/" + str(len(auto_miner)))
        for i in range(len(auto_miner)-1):
            file.write(str(auto_miner[i].level) + " ")
        file.write(str(auto_miner[len(auto_miner)-1]))
        print("추가/갱신 완료!")

def Load():
    global sellbuy
    global mineLV
    global myPickaxe
    global reforge
    global auto_miner
    file_name = input("로드할 파일명을 입력하세요.(.txt 붙이지 마세요.)")
    if os.path.exists(file_name + ".txt"):
        with open(file_name + ".txt", "r", encoding="UTF8") as file:
            load = file.readline().split("/")
            sellbuy = float(load[0])
            mineLV = int(load[1])
            if load[2] != "None":
                myPickaxe = load[2].split(":")
                myPickaxe[1] = int(myPickaxe[1])
                myPickaxe[2] = int(myPickaxe[2])
                myPickaxe[3] = int(myPickaxe[3])
                myPickaxe[4] = int(myPickaxe[4])
            else: myPickaxe = []
            if load[3] == "None":
                reforge = []
            else:
                reforge = [load[3], int(load[4])]
            for i in range(load[5]):
                auto_miner.append(Auto_Miner(load[6].split()[i]))
            print("로드 완료!")
    else:
        print("지정한 파일이 없습니다.")
print("help 또는 ? 명령어를 입력하세요.")
while True:
    i = input().lower()
    if i == "m":
        if myPickaxe != []:
            for i in range(5):
                print(c.Fore.GREEN + "■", end="")
                t.sleep(myPickaxe[2]/5)
            print(c.Fore.WHITE)
            print("곡괭이의 남은 내구도:" + str(myPickaxe[3]-1))
            for _ in range(myPickaxe[4]):
                Mining(True)
            if myPickaxe[3] <= 1:
                myPickaxe = []
                print("곡괭이가 부서졌다.")
            else:
                myPickaxe[3] -= 1

        else:
            print("곡괭이가 없습니다.")
    if i == "s":
        Sell()
    if i == "mu":
        MineUpgrade()
    if i == "sb":
        print("셀바이:" + str(sellbuy))
    if i == "rst":
        ReforgeStoneStore()
    if i == "pst":
        PickaxeStore()
    if i == "am":
        AutoMiner()
    if i == "ml":
        print("광산 레벨:" + str(mineLV))
        print("현재 얻을 수 있는 광물 :")
        for i in range(mineLV//2+1):
            print(minerals[i].split(":")[0])
    if i == "nm":
        print("다음 광산 가격:" + str(mineLV * 10))
    if i == "rf":
        Reforge()
    if i == "help" or i == "?":
        print("m = 캐기\ns = 팔기\nmu = 광산 업그레이드\nsb = 현재 셀바이\nrst = 재련석 상점\npst = 곡괭이 상점\nam = 마이너 생성/업그레이드\nml = 현재 광산 레벨/현재 얻을 수 있는 광물\nnm = 다음 광산 가격\nrf = 재련\nhelp/? = 메뉴얼\ntip = 확률표\ninv = 인벤토리\nsave = 파일 추가/저장\nload = 파일 불러오기\ndelete = 파일 삭제")
    if i == "tip":
        divide = 100
        for i in range(14):
            divide /= 2
            print(minerals[i+1].split(":")[0] + " : " + str(divide) + "%")
    if i == "inv":
        if myPickaxe != []:
            print(myPickaxe[0] + "\n내구도 : " + str(myPickaxe[3]))
        print("재련석:" + str(RF_stone))
        for i in range(len(minerals)):
            print(minerals[i].split(":")[0] + ":" + str(myMinerals.count(minerals[i].split(":")[0])))
    if i == "save":
        Save()
    if i == "load":
        Load()
    if i == "delete":
        file_name = input("삭제할 파일명을 입력하세요.(.txt 붙이지 마세요.)")
        if os.path.exists(file_name + ".txt"):
            os.remove(file_name + ".txt")
            print("삭제 완료!")
        else:
            print("지정한 파일이 없습니다.")
    if i == "end":
        s=False
        m=False
        p=False
        clear=0
        print("1000만 셀바이 ", end="")
        if sellbuy >= 10000000:
            print(c.Fore.GREEN + "✓")
        else:print(c.Fore.RED + "✘")
        t.sleep(3)
        print("광산 레벨 28레벨 ", end="")
        if mineLV >= 28:
            print(c.Fore.GREEN + "✓")
        else:print(c.Fore.RED + "✘")
        t.sleep(3)
        print("말라이트 곡괭이 ", end="")
        if myPickaxe != []:
            if myPickaxe[0] == "말라이트 곡괭이":
                print(c.Fore.GREEN + "✓")
            else:print(c.Fore.RED + "✘")
        else:print(c.Fore.RED + "✘")
        t.sleep(3)
        if s:
            print("✯",end="")
            clear+=1
        else:print(".",end="")
        if m:
            print("✯",end="")
            clear+=1
        else:print(".",end="")
        if p:
            print("✯")
            clear+=1
        else:print(".")
        if clear == 0:
            print("좀 더 광질을 하고 오세요.")
        if clear == 1:
            print("엔딩의 기초만 다졌군요.")
        if clear == 2:
            print("한발자국만 더 나아가 봅시다!")
        if clear == 3:
            print("당신은 엔딩 조건을 모두 다 갖췄습니다. 하지만 돈을 더 벌어볼까요?")
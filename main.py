import sys
import random

print("1から100までのランダムな数字を選んだから当ててみて！")
print("7回答えるチャンスがあるよ！")
randomNumber = random.randint(1,100)

for i in range(1, 8):
    print( str(i) + " 回目の挑戦!")
    userAnswer = sys.stdin.buffer.readline().decode()

    if int(userAnswer) > randomNumber:
        print("は僕の数字よりも上だよ！")
    elif int(userAnswer) < randomNumber:
        print("は僕の数字よりも下だよ！")
    else:
        print("大正解！答えは" + str(randomNumber) + "でした！")
        sys.exit()

print("残念答えは" + str(randomNumber) + "でした！")

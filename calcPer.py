import sys

def calculate(data):
    file = open(data, "r")
    accept = 0
    count = 0
    quiz_cnt = 0
    accept_cnt = 0

    for data in file:
        if("---" in data):
            print(f"{quiz_cnt + 1} : 正解問題数={accept}問")
            print(f"{quiz_cnt + 1} : 間違い数={count - accept}問")
            print(f"{quiz_cnt + 1} : 正解率={round((accept / count) * 100)}%")
            print("---")
            quiz_cnt += count
            count = 0
            accept_cnt += accept
            accept = 0
            continue
        if("O" in data):
            accept += 1
        count += 1
    
    print(f"総回答数: {quiz_cnt}")
    print(f"全体の正解問題数: {accept_cnt}")
    print(f"全体の間違い数: {quiz_cnt - accept_cnt}")
    print(f"全体の正答率: {round((accept_cnt /  quiz_cnt) * 100)}%")


if(len(sys.argv) == 2):
    calculate(sys.argv[1])
else:
    sys.stderr.write("Usage: calcPer.py dataFile")
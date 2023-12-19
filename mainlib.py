r"I love Balls"
import requests
import json
import os
from openai import OpenAI

idk = input("smthing idk?")
headers = {"Content-type": "application/json", "Accept": "text/plain"}
os.system("cls")
cnv = json.loads(idk)

def init(arg=""):
    if arg == "":
        prejson = {
            "IPClient": "",
            "deviceId": "",
            "api_key": cnv["api_key"],
            "token": cnv["token"],
        }
        json_ = json.dumps(prejson)
        r = json.loads(
            requests.post(
                "https://api-edu.go.vn/ioe-service/v2/game/getinfo",
                headers=headers,
                data=json_,
            ).text
        )
        return r
    else:
        return arg

try:
    json.loads(idk)["api_key"] #check if it from startgame or getinfo
except KeyError:
    r = init(idk)
else:
    r = init()
try:
    questions = r["data"]["game"]["question"]
    quesnum = len(questions)
    os.system("cls")
except TypeError:
    print("Token ko hợp lệ")
    exit()


def baibth():
    i2 = -1
    while i2 < quesnum - 1:
        i2 += 1
        qid = r["data"]["game"]["question"][i2]["id"]
        answers = r["data"]["game"]["question"][i2]["ans"]
        ansnum = len(answers)
        i = -1
        while i < ansnum - 1:
            i += 1
            ans = answers[i]["content"]
            jsonans = {
                "IPClient": "",
                "deviceId": "",
                "serviceCode": "IOE",
                "api_key": cnv["api_key"],
                "token": cnv["token"],
                "examKey": cnv["examKey"],
                "ans": {"questId": qid, "point": 10, "ans": ans},
            }
            r2 = requests.post(
                "https://api-edu.go.vn/ioe-service/v2/game/answercheck",
                headers=headers,
                data=json.dumps(jsonans),
            )

            if json.loads(r2.text)["data"]["point"] == 10:
                print(str(i2 + 1) + "." + ans)
                break


def baitf():
    i2 = -1
    while i2 < quesnum - 1:
        i2 += 1
        qid = r["data"]["game"]["question"][i2]["id"]
        answers = ["True", "False"]
        i = -1
        while i < 1:
            i += 1
            ans = answers[i]
            jsonans = {
                "IPClient": "",
                "deviceId": "",
                "serviceCode": "IOE",
                "api_key": cnv["api_key"],
                "token": cnv["token"],
                "examKey": cnv["examKey"],
                "ans": {"questId": qid, "point": 10, "ans": ans},
            }
            r2 = requests.post(
                "https://api-edu.go.vn/ioe-service/v2/game/answercheck",
                headers=headers,
                data=json.dumps(jsonans),
            )
            if json.loads(r2.text)["data"]["point"] == 10:
                print(str(i2 + 1) + "." + ans)
                break


def sortcri(list):
    return list["orderTrue"]

def baisapxep():
    quesnum = 10 #mac dinh :>
    i2 = -1
    while i2 < quesnum-1:
        i2 += 1
        answers = r["data"]["game"]["question"][i2]["ans"]
        answers.sort(key=sortcri)
        ansnum = len(answers)
        i3 = -1
        fans = ""
        while i3 < ansnum-1:
            i3 +=1
            ans2 = answers[i3]["content"]
            fans = f'{fans} {ans2}' 
        print(str(i2+1)+"."+fans)
client = OpenAI(api_key='sk-kWtoW5YrEDpuR9oDuOVvT3BlbkFJ9zUbntbKt5TgBDEw4cv') #my api key ;-;
client.api_key = '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'

#getinfo = input("api_key?")
#prompt = "Nobody really ******* the changes."
def sendmsg(prompt):
#    print(prompt)
    completion = client.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt=prompt,
        max_tokens=600,
        temperature=0
)
    rtn = completion.choices[0].text
    return rtn#.replace('Điền từ: ','')
#print(sendmsg(prompt))
def checkans(ans,qid):
    jsonans = {
    "IPClient": "",
    "deviceId": "",
    "serviceCode": "IOE",
    "api_key": cnv["api_key"],
    "token": cnv["token"],
    "examKey": cnv["examKey"],
    "ans": {"questId": qid, "point": 10, "ans": ans},
}
    r2 = requests.post(
        "https://api-edu.go.vn/ioe-service/v2/game/answercheck",
        headers=headers,
        data=json.dumps(jsonans),
    )

    if json.loads(r2.text)["data"]["point"] == 10:
        return True
    else:
        return False
def baidientu():
    print("Lưu ý:Bài được làm bởi AI(ChatGPT) nên sai sót không thể tránh khỏi")
    i2 = -1
    questions = ""
    while i2 < quesnum - 1:
        i2 += 1
        qid = r["data"]["game"]["question"][i2]["id"]
        question = r["data"]["game"]["question"][i2]["content"]["content"]
        questions = f'{questions}\n{"Câu"} {i2+1}:{question}'
    
    ans = sendmsg(f'{"Điền từ dựa theo số lượng dấu hoa thị"}\n"{questions}"')
    print(ans)

def baitf4cau():
    print("Lưu ý:Bài được làm bởi AI(ChatGPT) nên sai sót không thể tránh khỏi")
    i2 = -1
    questions = ""
    wat = r["data"]["game"]["Subject"]["content"]
    sendmsg(f'{"Đọc bài văn sau"}\n{wat}')
    while i2 < quesnum - 1:
        i2 += 1
        qid = r["data"]["game"]["question"][i2]["id"]
        question = r["data"]["game"]["question"][i2]["content"]["content"]
        questions = f'{questions}\n{"Câu"} {i2+1}:{question}'
    ans = sendmsg(f'{"Từ đoạn văn trên trả lời câu hỏi True False sau:"}\n{questions}')
    print(ans)


def baiconlon():
    print("Lưu ý:Bài được làm bởi AI(ChatGPT) nên sai sót không thể tránh khỏi")
    i2 = -1
    questions = ""
    wat = r["data"]["game"]["Subject"]["content"]
    while i2 < quesnum - 1:
        i2 += 1
        qid = r["data"]["game"]["question"][i2]["id"]
        question = r["data"]["game"]["question"][i2]["content"]["content"]
        questions = question
    ans = sendmsg(f'{"Đọc bài văn sau"}\n{wat}\n{"Điền các từ sau vào đoạn văn:"}\n{questions}')
    print(ans)

def test():
    i2 = -1
    ffinal = []
    while i2 < quesnum - 1:
        i2 += 1
        qid = r["data"]["game"]["question"][i2]["id"]
        answers = r["data"]["game"]["question"][i2]["ans"]
        ansnum = len(answers)
        i = -1
        while i < ansnum - 1:
            i += 1
            ans = answers[i]["content"]
            jsonans = {
                "IPClient": "",
                "deviceId": "",
                "serviceCode": "IOE",
                "api_key": cnv["api_key"],
                "token": cnv["token"],
                "examKey": cnv["examKey"],
                "ans": {"questId": qid, "point": 10, "ans": ans},
            }
            r2 = requests.post(
                "https://api-edu.go.vn/ioe-service/v2/game/answercheck",
                headers=headers,
                data=json.dumps(jsonans),
            )
            if json.loads(r2.text)["data"]["point"] == 10:
                final = f'{{"ans":"{ans}","point":10,"questId":"{qid}"}}'
                ffinal.append(final)
                break
            finaljson = {
                "serviceCode": "IOE",
                "api_key": cnv["api_key"],
                "token": cnv["token"],
                "examKey": cnv["examKey"],
                "ans": json.dumps(list(ffinal))
            }
        print(ffinal)
    r2 = requests.post(
        "https://api-edu.go.vn/ioe-service/v2/game/finishgame",
        headers=headers,
        data=json.dumps(finaljson)
    )
    print(r2.text)
#varibles for detectings test type
quescontenttest = r["data"]["game"]["question"][0]["content"]["content"]
questypetest = r["data"]["game"]["question"][0]["type"]
subjecttypetest = r["data"]["game"]["Subject"] != None#Null js=None python bruh
quespointtest = r["data"]["game"]["question"][0]["Point"]
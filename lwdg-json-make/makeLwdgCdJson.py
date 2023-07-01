import json

f = open("lwdg-cd-list.txt", "r")
lwdgDict = {}
for x in f:
    tknLst = x.split()
    if "존재" not in tknLst:
        continue
    lwdgCd = tknLst[0]
    if lwdgCd[4:] != "000000":
        continue
    print(tknLst)
    print(f'lwdgCd = {lwdgCd}')
    lwdgNm = tknLst[1]
    if tknLst[2] != "존재":
        lwdgNm += " " + tknLst[2]
    print(f'lwdgNm = {lwdgNm}')

    lwdgDict[lwdgCd] = lwdgNm

print(lwdgDict)

with open("lwdg-cd-list.json", 'w', encoding='utf-8') as file:
    json.dump(lwdgDict, file, indent="\t", ensure_ascii=False)


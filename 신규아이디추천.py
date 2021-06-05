def solution(new_id):
    answer = ''

    #1단계
    new_id = new_id.lower()
    print("1단계 : ", new_id)

    #2단계
    allowTck = ["-","_","."]
    temp = ""
    for i in new_id:
        if i.isdigit() or i.isalpha() or i in allowTck:
            temp = temp + i
    new_id = temp
    temp = ""
    print("2단계 : ", new_id)

    #3단계
    if len(new_id) >= 2:
        for idx, i in enumerate(new_id):
            if not (i == "." and new_id[idx-1] == "."):
                temp = temp + i
        new_id = temp
        temp = ""
    print("3단계 : ", new_id)

    #4단계
    if len(new_id) > 0:
        if new_id[0] == ".":
            new_id = new_id[1:]
        if len(new_id) >= 2:
            if new_id[-1] == ".":
                new_id = new_id[:-1]
    print("4단계 : ", new_id)

    #5단계
    if len(new_id) == 0:
        new_id = "a"
    print("5단계 : ", new_id)

    #6단계
    if len(new_id) >= 16:
        new_id = new_id[:15]
    if len(new_id) >= 2 and new_id[-1] == ".":
        new_id = new_id[:-1]
    print("6단계 : ", new_id)

    #7단계
    temp = new_id[-1]
    while len(new_id) <= 2:
        new_id = new_id + temp
    print("7단계 : ", new_id)

    answer = new_id
    return answer
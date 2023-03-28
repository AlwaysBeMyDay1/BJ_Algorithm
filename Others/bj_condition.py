def oven_time():
    time, minute = [int(x) for x in input().split(' ')]
    cooking_minute = int(input())

    cooking_time, add_minute = divmod(time * 60 + cooking_minute + minute, 60)
    print(cooking_time % 24, add_minute)


def dice_face():
    face_list = [int(face) for face in input().split(' ')]

    setted_list = list(set(face_list))

    answer = 0
    if len(setted_list) == 3:
        answer = max(face_list) * 100
    elif len(setted_list) == 1:
        answer = max(face_list) * 1000 + 10000
    else:
        if face_list.count(face_list[0]) == 2:
            answer = face_list[0] * 100 + 1000
        else:
            answer = face_list[1] * 100 + 1000

    print(answer)

# https://school.programmers.co.kr/learn/courses/30/lessons/42579
# 베스트앨범


def solution(genres, plays):
  played_time = {}
  for i in zip(genres, plays):
    if i[0] in played_time:
      played_time[i[0]] += i[1]
    else:
      played_time[i[0]] = i[1]
  sorted_played_time = sorted(played_time.items(), key=lambda x: -x[1])
  print(sorted_played_time)

  genres_played_list = {}
  for index, i in enumerate(zip(genres, plays)):
    if i[0] in genres_played_list:
      genres_played_list[i[0]][index] = i[1]
    else:
      genres_played_list[i[0]] = {index: i[1]}

  answer = []
  for genre in sorted_played_time:
    sorted_list = sorted(genres_played_list[genre[0]].items(),
                         key=lambda x: (-x[1], x[0]))
    answer.append(sorted_list[0][0])
    try:
      answer.append(sorted_list[1][0])
    except:
      pass
  return answer


print(
  solution(["classic", "pop", "classic", "classic", "pop"],
           [500, 600, 150, 800, 2500]))

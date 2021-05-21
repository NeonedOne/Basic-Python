# Алексей Головлев, группа БСБО-07-19

n = int(input())
post = input().split(' опубликовал пост, количество просмотров: ')
popularity = {post[0]: [int(post[-1]), 'origin']}
for i in range(n - 1):
    post = input()
    reposter, post = post.split(' отрепостил пост у ')
    author, views = post.split(', количество просмотров: ')
    popularity[reposter] = [int(views), author]
    while author != 'origin':
        popularity[author][0] += int(views)
        author = popularity[author][1]
for val in popularity.values():
    print(val[0])

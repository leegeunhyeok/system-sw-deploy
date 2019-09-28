
# 파일 읽고 1줄씩 읽기
with open('review.txt', mode='r') as f:
    for line in f:
        print(line)

# 파일 쓰기
with open('test.txt', mode='w') as f:
    f.write('hello, ')

# 파일 이어쓰기
with open('test.txt', mode='a') as f:
    f.write('world!')

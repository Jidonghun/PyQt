# 1
x = '9'
print(x, type(x))

# 2
i_data = 8086
print(type(i_data))

# 3
print("내 꿈은 '멋진 집'을 갖는 거야")

# 4
you = '너'
me = '나'
print(you + '와', me + '는...!')

# 5
lyric = """
긴바지를 찢어 입었고 빨간 두건도 지금 쓰고 있어
노랗게 머리 염색을 하고서 모델 같은 표정을 지어 봐도
잡지 속의 이쁜 애들처럼 이뻐보이지 않는 이윤 뭘까"""
print(lyric[28])

# 6
lyric_part = lyric[29:59]
print(lyric_part)

# 7
print(lyric[-1], lyric[-2:], lyric[-3:])

# 8
lyric1 = """긴바지를 찢어 입었고 빨간 두건도 지금 쓰고 있어
노랗게 머리 염색을 하고서 모델 같은 표정을 지어 봐도
잡지 속의 이쁜 애들처럼 이뻐보이지 않는 이윤 뭘까
"""
print(lyric[0], lyric1[0])
print(lyric[-1], lyric1[-1])

# 9
fname = '김성필'
sname = '김민재\n'
print(fname, sname)
print(len(fname), len(sname))

# 10
a = 10 % 3
b = 10 // 3
print('몫: ', a, '\n나머지', b)

# 11
a = 1
b = '9'
print(a + int(b))

# 12
temperature = 25
print('온도는', str(temperature)+'도씨입니다')

# 13
y_math = 88.32
s_kor = 92.78
print('영희의 수학 점수는 {}점이고 성필이의 국어 점수는 {}점입니다!'.format(y_math, s_kor))
print('영희의 수학 점수는 {:.1f}점이고 성필이의 국어 점수는 {:.1f}점입니다!'.format(y_math, s_kor))

# 14
lyric = """긴바지를 찢어 입었고 빨간 두건도 지금 쓰고 있어
노랗게 머리 염색을 하고서 모델 같은 표정을 지어 봐도
잡지 속의 이쁜 애들처럼 이뻐보이지 않는 이윤 뭘까
친구들이 이런 말을 해 넌 너무 튀어 보이려 한다고
하지만 난 그런 말 신경안써 난 튀어 보이는게 정말 좋아
난 언제나 나를 믿고 있어 언젠가는 이뻐질 거라고
그래서 난 포기 하지 않아 나는 정말로 멋있어 보이고 싶으니까
- 주주클럽 공주병 -

돈이드니 아무말이나 해 돈이드니 사랑한다 해봐
내가 듣기에 좋은 말은 다 해도돼 넌 바보야 넌 너무 답답해
너는 정말 분위기 못맞춰 사랑한다고 말해봐 키쓰 해줄께
잼있고 즐거운 일이라면 이젠 너와 함께하고 싶어 그런 날 넌 몰라 아무리 설명해도 이해 못해
나 오늘 어때 보여 이뻐보여 널 위해 어제산 옷을 입었어
넌 매일 똑같은 옷을 입어도 내가 이쁘게 봐줄께
- 주주 클럽 돈이 드니 -"""
print('사랑' in lyric)

# 15
hobby = '드라이브, 낚시, 등산'
print(hobby.split(','))

# 16
sdate = '2023:06:28'
stime = '13-10-25'
print(sdate.replace(':', '-'))
print(stime.replace('-', ':'))

# 17
price1 = '2,000원'
price2 = '3,000원'
price_a = price1.replace(',', '').replace('원', '')
price_b = price2.replace(',', '').replace('원', '')
price_total = int(price_a) + int(price_b)
print(price_total)


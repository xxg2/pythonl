s = "spam's spam's spam's"
S = 's\np\ta\x00m'
a = """test"""
print(a)
b = b'spam'  # 字节字符串
print(b)
c = "a %s parrot" % a
print(c)
d = "a %s parrot".format(a)
print(c)
e = "asdjfljsdflksadf".find('a')
print(e)
print(s.rstrip()) # 移空行
print(s.replace('pa', 'xx'))
print(s.split("'"))
print(s.isdigit())
print(s.lower())
print(s.endswith('spam'))
print('|'.join(a))
print(S.encode('ASCII'))
for x in s:
    print(x)
print('spam' in s)
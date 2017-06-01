import re
# --------------------sub string--------------
name = "hello world"
print(name[2])
print(name[2:3])
print(name[2:4])
print(name[2:])
print(name[:3])
print(name + name[0:0])
print(name[:-1])
print(name[:3] + name[3:])
str = ''
# print str[0] # error string index out of range
print(str[12:12])  # ''
t = 'Hi'
print(t[:3] + t[3:])  # no error

# --------------------find string-------------
pythagorgs = "There is geometry in the humming of the strings, there is music in the spacing of the spheres."
print(pythagorgs.find('string'))
print(pythagorgs.find('Tom'))
print(pythagorgs.find(pythagorgs))
print('s'.find('s'))
print(pythagorgs.find(''))
print(pythagorgs.find(pythagorgs+"!!!")+1)

danton = "De l'audace, encore de l'audace, toujours de l'audace. "
print(danton.find('audace'))      # 5
print(danton.find('audace', 6))  # 25

S = 'SpaM'
print(len(S)) # 索引S[0],S[1]. 反向索引S[-1],S[-2]
print(S[len(S)-1])
print(S.lower())
print(S.upper())

# 分片操作 slice
S[1:3]

# 不可变性
# S[0] = 'Z'  会报错. TypeError: 'str' object does not support item assignment
S = 'z'+S[1:]  # 生成一个新对象

# split
line = 'aaa, bbb, ccc, dd'
sLine = line.split(',')
print(sLine)

# format
print('%s, eggs, and %s' % ('Spam', 'spami'))
print('{0}, eggs, and {1}'.format('spam', 'spam1'))
print(dir(S))
print(help(S.isalpha))

specS = 'A\nB\tC'
print(len(specS))

msg = """ aaa
bbb'''bbbbbb""bbbbbbbbbbb'bbb
ccccccccccccccc"""
print(msg)

match = re.match('Hello[ \t]*(.*)world', 'Hello Python world')
print(match.group(1))





























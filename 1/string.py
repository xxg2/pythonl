# --------------------sub string--------------
name = "hello world"
print name[2]
print name[2:3]
print name[2:4]
print name[2:]
print name[:3]
print name + name[0:0]
print name[:-1]
print name[:3] + name[3:]
str = ''
# print str[0] # error string index out of range
print str[12:12]  # ''
t = 'Hi'
print t[:3] + t[3:]  # no error

# --------------------find string-------------
pythagorgs = "There is geometry in the humming of the strings, there is music in the spacing of the spheres."
print pythagorgs.find('string')
print pythagorgs.find('Tom')
print pythagorgs.find(pythagorgs)
print 's'.find('s')
print pythagorgs.find('')
print pythagorgs.find(pythagorgs+"!!!")+1

danton = "De l'audace, encore de l'audace, toujours de l'audace. "
print danton.find('audace')      # 5
print danton.find('audace', 6)  # 25





































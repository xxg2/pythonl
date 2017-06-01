D = {'food': 'spam', 'quantity':4, 'color':'pink'}
D['food'] # spam
D['name'] = 'job'
rec = {'name':{'first':'Bob', 'last':'Smith'},
       'job':['dev','mgr'],
       'age':40.5}
rec['name']['last'] # Smith
rec['job'] # ['dev', 'mgr']
rec['job'][-1]
rec['job'].append('janitor')

Ks = list(D.keys())
Ks.sort()
for key in Ks:
    print(key, '=>', D[key])
for key in sorted(D):
    print(key, '=>', D[key])
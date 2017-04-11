import re
text = ''.join(open('ndev.sen').readlines())
sentences = re.split(r' *[\.\?\!][\'\"\)\]]* *', text)

for i in sentences:
    print(i)
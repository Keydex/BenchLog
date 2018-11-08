import time
from benchlog import BenchLog

test = BenchLog('test', 10000, ['testa','testb'])
test.setHost('http://localhost:3000')
array = []
test.enableGPU(0)
test.start()
for i in range(1,10000):
    temp = [None] * i
    array.append(temp)
    if(i % 1000 == 0):
        test.log(i)
test.end()

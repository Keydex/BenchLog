import time
from benchlog import BenchLog

logging = BenchLog('test', 10000, ['testa','testb'])
logging.setHost('http://localhost:3000')
array = []
logging.enableGPU(0)
logging.start()
for i in range(1,10000):
    temp = [None] * i
    array.append(temp)
    if(i % 1000 == 0):
        logging.log(i)
logging.end()

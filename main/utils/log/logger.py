from datetime import datetime
timeList = []
logList = []

class Logger:
    def log(step):
        print(step)
        logList.append(f' {step}\n')
        timeList.append(f'{datetime.now()}')

    def logToFile():
        summaryList = list(zip(timeList, logList))
        with open('../../../test/log.txt', 'w', encoding='utf-8') as data:
            data.write(summaryList)

    def getTimings():
        return [*timeList]
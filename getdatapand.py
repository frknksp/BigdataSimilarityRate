from concurrent.futures import ThreadPoolExecutor
import concurrent.futures
import pandas as pd
import time
import math

def fonks(threadcount,columname):
    df = pd.read_csv('cleardf.csv',low_memory=False)
    valuecountsdict = df[columname].value_counts().to_dict()
    arr = []
    threadtimer = []
    for a,b in valuecountsdict.items():
        if b > 1:
            # print(b)
            tmpobje = {
                                "firststr": a,
                                "secondstr" : a,
                                "rate" : 100
                        }
            arr.append(tmpobje)

    onlyvaluesls = list(valuecountsdict.keys())

    def comparestr(string1, string2):
        str1list = string1.split()
        str2list = string2.split()
        bigword_count = max(len(str1list), len(str2list))
        matchlist = [item for item in str1list if item in str2list]
        matchlistlen = len(matchlist)
        similarity_rate = (matchlistlen / bigword_count) * 100

        return round(similarity_rate)

    def compare(tuples):
        begin = time.perf_counter()
        for x in range(tuples[0], tuples[1]):
            for i in range(x + 1, len(onlyvaluesls)):
                simrate = comparestr(onlyvaluesls[x], onlyvaluesls[i])
                # print(onlyvaluesls[x] + "//"+  onlyvaluesls[i])
                # print(simrate)
                tempobje = {
                    "firststr": onlyvaluesls[x],
                    "secondstr": onlyvaluesls[i],
                    "rate": simrate
                }
                arr.append(tempobje)

        bitis = time.perf_counter()
        print(bitis - begin)
        threadtimer.append({"thread_index":str(tuples[2]),"time":str(bitis-begin)})

    threadnum = threadcount
    splitvaluesls = math.floor(len(onlyvaluesls) / threadnum)
    emparr = []
    for i in range(0,threadnum):
        emparr.append((splitvaluesls*i, splitvaluesls*(i+1),i+1))

    print(emparr)

    totaltimebegin = time.perf_counter()
    with concurrent.futures.ThreadPoolExecutor(threadnum) as executor:
        executor.map(compare, emparr)
        executor.shutdown(wait=True, cancel_futures=False)

    totaltimeend = time.perf_counter()
    totaltime = totaltimeend-totaltimebegin
    threadtimer.append({"thread_index":"TOTAL","time":str(totaltime)})
    print(totaltime)
    print(threadtimer)
    return (arr,threadtimer)

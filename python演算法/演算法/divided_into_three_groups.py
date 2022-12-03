"""
[1, 2, 2, 4, 6, 6]
將其分組成
[1,2],[2,4],[6,6]
[1,2],[2,6],[4,6]
[1,4],[2,2],[6,6]
[1,4],[2,6],[2,6]
[1,6],[2,4],[2,6]
[1,6],[4,6],[2,2]
不重複
"""
def permutation(vecSrc, vecDst, cur, mapAns):
    n = len(vecSrc)
    if cur == n:
        # 定義一個輔助函數，用於獲取排列中指定位置的值
        def get_dat(A):
            return vecSrc[vecDst[A]]

        szKey, szData = "", ""
        vecSort = []
        for k in range(0, n, 2):
            szKey = "{:08x}_{:08x}".format(min(get_dat(k), get_dat(k + 1)), max(get_dat(k), get_dat(k + 1)))
            vecSort.append(szKey)
        vecSort.sort()
        szKey = "{},{},{}".format(vecSort[0], vecSort[1], vecSort[2])
        szData = "[{},{}],[{},{}],[{},{}]".format(min(get_dat(0), get_dat(1)), max(get_dat(0), get_dat(1)),
                                                  min(get_dat(2), get_dat(3)), max(get_dat(2), get_dat(3)),
                                                  min(get_dat(4), get_dat(5)), max(get_dat(4), get_dat(5)))
        if szKey not in mapAns:
            mapAns[szKey] = szData

    else:
        for i in range(n):
            c1 = 0
            for j in range(cur):
                if vecDst[j] == i:
                    c1 += 1
                    break

            if c1 == 0:
                vecDst[cur] = i
                permutation(vecSrc, vecDst, cur + 1, mapAns)


vecSrc = [1, 2, 2, 4, 6, 6]
vecSrc.sort()
vecDst = [0] * len(vecSrc)
mapAns = {}
permutation(vecSrc, vecDst, 0, mapAns)

for _, v in mapAns.items():
    print(v)
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split('.')
        v2 = version2.split('.')
        if(len(v1) >= len(v2)):
            for i, val in enumerate(v1):
                compareValue = v2[i] if(i < len(v2)) else 0
                # print val
                # print compareValue
                # 去除前导0 通过转str再转回int的方式
                val = int(str(val))
                compareValue = int(str(compareValue))
                if(val > compareValue):
                    return 1
                if(val < compareValue):
                    return -1
                pass
            return 0
        else:
            for i, val in enumerate(v2):
                compareValue = v1[i] if(i < len(v1)) else 0
                # 去除前导0 通过转str再转回int的方式
                val = int(str(val))
                compareValue = int(str(compareValue))
                if(val > compareValue):
                    return -1
                if(val < compareValue):
                    return 1
                pass
            return 0
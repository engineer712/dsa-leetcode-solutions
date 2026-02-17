class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        def countbit(num):
            if num == 0:
                return 0
            return num % 2 + countbit(num // 2)

        res = []

        for i in range(12):
            for j in range(60):
                if countbit(i) + countbit(j) == turnedOn:
                    if j < 10:
                        res.append(f'{i}:0{j}')
                    else:
                        res.append(f'{i}:{j}')

        return res
      
#More smaller way using builtin methods:

# class Solution(object):
#     def readBinaryWatch(self, turnedOn):
#         res = []
#         for h in range(12):
#             for m in range(60):
#                 if bin(h).count('1') + bin(m).count('1') == turnedOn:
#                     res.append(f"{h}:{m:02d}")
#         return res

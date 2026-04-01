class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for e in operations:
            if e == "C":
                record.pop()
            elif e == "+":
                record.append(record[-1] + record[-2])
            elif e == "D":
                record.append(record[-1] * 2)
            else:
                record.append(int(e))
        return sum(record)





        
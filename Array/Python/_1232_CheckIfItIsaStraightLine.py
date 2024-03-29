from typing import List


class Solution:
    # Iteration
    # Time Complexity: BigO(N)
    # Space Complexity: BigO(1)
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        mxd = coordinates[1][0] - coordinates[0][0]
        myd = coordinates[1][1] - coordinates[0][1]

        for i in range(1, len(coordinates) - 1):
            nxd = coordinates[i + 1][0] - coordinates[i][0]
            nyd = coordinates[i + 1][1] - coordinates[i][1]

            if mxd > nxd and myd > nyd:
                try:
                    ckx = mxd / nxd
                    cky = myd / nyd
                    if ckx == cky:
                        mxd = nxd
                        myd = nyd
                        continue
                except ZeroDivisionError:
                    return False
                return False
            elif (mxd == 0 and nxd == 0) or (myd == 0 and nyd == 0):
                continue
            else:
                try:
                    ckx = mxd / nxd
                    cky = myd / nyd
                    if ckx == cky:
                        continue
                except ZeroDivisionError:
                    return False
                return False
        return True


ins = Solution

print(
    "[[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]] | Expected:",
    True,
    "| Output:",
    ins.checkStraightLine(
        ins,
        [
            [1, 2],
            [2, 3],
            [3, 4],
            [4, 5],
            [5, 6],
            [6, 7],
        ],
    ),
)
print(
    "[[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]] | Expected:",
    False,
    "| Output:",
    ins.checkStraightLine(
        ins,
        [
            [1, 1],
            [2, 2],
            [3, 4],
            [4, 5],
            [5, 6],
            [7, 7],
        ],
    ),
)
print(
    "[[0, 0],[0, 1],[0, -1]] | Expected:",
    True,
    "| Output:",
    ins.checkStraightLine(
        ins,
        [
            [0, 0],
            [0, 1],
            [0, -1],
        ],
    ),
)
print(
    "[[0,1],[1,3],[-4,-7],[5,11]] | Expected:",
    True,
    "| Output:",
    ins.checkStraightLine(
        ins,
        [
            [0, 1],
            [1, 3],
            [-4, -7],
            [5, 11],
        ],
    ),
)
print(
    "[[3, 0],[2, 1],[1, 2],[-1, 4]] | Expected:",
    True,
    "| Output:",
    ins.checkStraightLine(
        ins,
        [
            [3, 0],
            [2, 1],
            [1, 2],
            [-1, 4],
        ],
    ),
)
print(
    "[[1,1],[2,2],[2,0]] | Expected:",
    False,
    "| Output:",
    ins.checkStraightLine(
        ins,
        [[1, 1], [2, 2], [2, 0]],
    ),
)
print(
    "[[1,-8],[2,-3],[1,2]] | Expected:",
    False,
    "| Output:",
    ins.checkStraightLine(
        ins,
        [[1, -8], [2, -3], [1, 2]],
    ),
)

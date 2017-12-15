import math

class DPXDrop():
    def __init__(self, a, b):

        self.a = a.sequence
        self.b = b.sequence

        self.M = len(self.a)-1
        self.N = len(self.b)-1

        self.mat = 4
        self.mis = -2
        self.ind = -4

        self.X = 2

        self.TPrime = 0
        self.T = 0

    def main(self):
        self.s = [[None]*self.M**2 for _ in range(self.N**2)] #- gives error(compare None and float)
        #self.s = [[float("-inf")] * M * M for _ in range(N * N)]

        for x in range(2*self.M + 2):
            for y in range(2*self.N + 2):
                self.s[x][y] = float("-inf")

        self.s[0][0] = 0
        k = 0
        L = 0
        U = 0
        while L <= U+1:
            k += 1
            i = math.ceil(L)
            while i <= math.floor(U)+1:
                j = k - i
                if self.isInteger(i):
                    #max1 = 0
                    first = float("-inf")
                    second = float("-inf")
                    third = float("-inf")
                    fourth = float("-inf")

                    if L <= (i - 0.5) <= U:
                        if self.a[int(i)] == self.b[int(j)]:
                            first = self.S(i - 0.5, j - 0.5) + self.mat / 2
                        else:
                            second = self.S(i - 0.5, j - 0.5) + self.mis / 2
                    if i <= U:
                        third = self.S(i, j - 1) + self.ind
                    if L <= i-1:
                        fourth = self.S(i - 1, j) + self.ind

                    max1 = max(first, second, third, fourth)
                    self.writeS(max1, i, j)

                else:
                    if self.a[int(i + 0.5)] == self.b[int(j + 0.5)]:
                        self.writeS(self.S(i - 0.5, j - 0.5)+self.mat / 2, i, j)
                    else:
                        self.writeS(self.S(i - 0.5, j - 0.5) + self.mis / 2, i, j)

                self.TPrime = max(self.TPrime, self.S(i, j))
                if (self.S(i, j) < (self.T - self.X)):
                    self.writeS(float("-inf"), i, j);


                i += 0.5

            iTemp = 0
            while iTemp <= k:
                try:
                    if self.S(iTemp, k-iTemp) > float("-inf"):
                        L = iTemp
                        break
                except: pass
                iTemp += 0.5

            iTemp = k
            while iTemp >= 0:
                try:
                    if self.S(iTemp, k-iTemp) > float("-inf"):
                        U = iTemp
                        break
                except:pass
                iTemp -= 0.5

            L = max(L, k+1-self.N)
            U = min(U, self.M-1)
            self.T = self.TPrime
        return self.TPrime
        print("T Prime is: {}".format(self.TPrime))

    def isInteger(self, x):
        return x not in [float("inf"), float("-inf")] and x == math.floor(x)

    def S(self, i, j):
        if i<0 or j<0:
            return float("-inf")
        return self.s[int(i*2)][int(j*2)]

    def writeS(self, value, i, j):
        if i<0 or j<0:return
        self.s[int(i * 2)][int(j * 2)] = value

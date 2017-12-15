MIN_VALUE = float("-inf")


class Greedy:

    def __init__(self, a, b):
        self.a = a.sequence
        self.b = b.sequence
        self.m = len(self.a)
        self.n = len(self.b)
        self.mat = 4
        self.mis = -2
        self.ind = -4
        self.x = (max(self.m, self.n) * 0.5)
        self.t = 0
        self.t1 = 0

    def S1(self, i, j, d):
        return(((i + j) * self.mat / 2) - d * (self.mat - self.mis))

    def main(self):
        i = 0
        k0 = 0
        m_n_max = max(self.m, self.n)
        m_n_min = min(self.m, self.n)
        self.R = [[MIN_VALUE] * ((m_n_max * 2) + 1) for _ in range(m_n_max + 1)]
        T = [None] * (m_n_max + 1)

        while i < m_n_min and self.a[i] == self.b[i]:
            i += 1

        if i != m_n_max:
            k0 = 4

        self.R[0][0 + m_n_max] = i

        T1 = self.S1(i, i, 0)
        T[0] = T1

        d, L, U = 0, 0, 0

        while L <= U + 2:
            d += 1
            if d > m_n_max:
                break

            d1 = max(d - int((self.x + (self.mat / 2)) / (self.mat - self.mis)) - 1, 0)
            for k in range(L - 1, U + 2):
                i_1, i_2, i_3 = MIN_VALUE, MIN_VALUE, MIN_VALUE

                if L < k:
                    i_1 = self.R[d - 1][k - 1 + m_n_max] + 1
                if L <= k and k <= U:
                    i_2 = self.R[d - 1][k + m_n_max] + 1
                if k < U:
                    i_3 = self.R[d - 1][k + 1 + m_n_max]

                i = max(i_1, i_2, i_3)

                j = i - k
                #print(d, k)
                if i > MIN_VALUE and self.S1(i, j, d) > T[d1] - self.x:
                    while i < self.m - 1 and j < self.n - 1 and self.a[i] == self.b[j]:
                        i += 1
                        j += 1
                    self.R[d][k + m_n_max] = i
                    T1 = max(T1, self.S1(i, j, d))
                else:
                    #print(d, k)
                    self.R[d][k + m_n_max] = MIN_VALUE
            T[d] = T1
            for k in range(-m_n_max, m_n_max + 1, 1):
                if self.R[d][k + m_n_max] > MIN_VALUE:
                    L = k
                    break
            for k in range(m_n_max, -m_n_max - 1, -1):
                if self.R[d][k + m_n_max] > MIN_VALUE:
                    U = k
                    break
            for k in range(m_n_max, -m_n_max - 1, -1):
                if self.R[d][k + m_n_max] == self.n + k:
                    L = max(L, k + 2)
                    break
            for k in range(-m_n_max, m_n_max + 1, 1):
                if self.R[d][k + m_n_max] == self.m:
                    U = min(U, k - 2)
                    break
        return T1+k0

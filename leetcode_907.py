class Solution:
    def sumSubarrayMins(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        mod = 10**9+7
        n = len(A)
        left, right = [0]*n, [0]*n
        s1, s2 = [],[]
        for i in range(n):
            count = 1
            while s1 and s1[-1][0] > A[i]:
                count += s1.pop()[1]
            left[i] = count
            s1.append([A[i], count])
        for i in range(n)[::-1]:
            count = 1
            while s2 and s2[-1][0] >= A[i]:
                count += s2.pop()[1]
            right[i] = count
            s2.append((A[i], count))
        return sum(a*l*r for a,l,r in zip(A,left,right)) % mod
            


def main():
    A = [3,1,2,4]
    print(Solution().sumSubarrayMins(A))

if __name__ == '__main__':
    main()
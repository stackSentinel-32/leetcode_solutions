# class Solution:
#     def fib(self, n: int) -> int:
#         a=0
#         b=1
#         for i in range(n):
#             a,b=b,a+b
#         return a

class Solution:
    def fib(self, n: int) -> int:
        d = {0: 0, 1: 1}
        return self.fibo(n, d)

    def fibo(self, n, d):
        if n in d:
            return d[n]

        d[n] = self.fibo(n-1, d) + self.fibo(n-2, d)
        return d[n]

        # if n==0:
        #     return 0
        # elif n==1:
        #     return 1
        # return self.fib(n-1) + self.fib(n-2)

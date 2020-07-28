

class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):

            x = []
            for i in range(1,n+1):
                if n%i==0:
                    x.append(i)
            sum=0
            # return x
            for i in x:
                sum+=i
            return sum

        # pass

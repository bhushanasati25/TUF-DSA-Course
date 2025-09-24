class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator == 0:
            return "0"

        # Sign handling
        sign = '-' if (numerator < 0) ^ (denominator < 0) else ''
        n, d = abs(numerator), abs(denominator)

        # Integer part
        integer_part = n // d
        rem = n % d
        if rem == 0:
            return sign + str(integer_part)

        res = [sign + str(integer_part), '.']

        # remainder -> index in res where the corresponding digit starts
        seen = {}

        while rem != 0:
            if rem in seen:
                idx = seen[rem]
                res.insert(idx, '(')
                res.append(')')
                break

            seen[rem] = len(res)
            rem *= 10
            res.append(str(rem // d))
            rem %= d

        return ''.join(res)

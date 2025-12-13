class Solution(object):
    def validateCoupons(self, code, businessLine, isActive):
        """
        :type code: List[str]
        :type businessLine: List[str]
        :type isActive: List[bool]
        :rtype: List[str]
        """
        priority = ["electronics", "grocery", "pharmacy", "restaurant"]
        priority_index = {b: i for i, b in enumerate(priority)}

        valid = []

        for c, b, active in zip(code, businessLine, isActive):
            if not active:
                continue

            if b not in priority_index:
                continue

            if not c or not all(ch.isalnum() or ch == "_" for ch in c):
                continue

            valid.append((priority_index[b], c))

        valid.sort(key=lambda x: (x[0], x[1]))

        return [c for _, c in valid]

class Solution(object):
    def minTime(self, skill, mana):
        """
        :type skill: List[int]
        :type mana: List[int]
        :rtype: int
        """
        n, m = len(skill), len(mana)
        if n == 0 or m == 0:
            return 0

        sumSkill = sum(skill)                      
        prevWizardDone = sumSkill * mana[0]        

        for j in range(1, m):
            prevPotionDone = prevWizardDone        
            for i in range(n - 2, -1, -1):
                prevPotionDone -= skill[i + 1] * mana[j - 1]
                prevWizardDone = max(prevPotionDone, prevWizardDone - skill[i] * mana[j])
            prevWizardDone += sumSkill * mana[j]

        return prevWizardDone

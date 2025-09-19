class Spreadsheet(object):
    def __init__(self, rows):
        """
        :type rows: int
        """
        # Only store cells that were explicitly set; others default to 0
        self.values = {}

    def setCell(self, cell, value):
        """
        :type cell: str
        :type value: int
        :rtype: None
        """
        self.values[cell] = value

    def resetCell(self, cell):
        """
        :type cell: str
        :rtype: None
        """
        if cell in self.values:
            del self.values[cell]

    def getValue(self, formula):
        """
        :type formula: str
        :rtype: int
        """
        # formula format is guaranteed like "=X+Y"
        # tokens after '=' are separated by '+'
        total = 0
        for token in formula[1:].split('+'):
            if token and token[0].isdigit():     # literal number
                total += int(token)
            else:                                # cell reference like "A1"
                total += self.values.get(token, 0)
        return total


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)
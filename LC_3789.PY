
class Solution(object):
    def minimumCost(self, cost1, cost2, costBoth, need1, need2):

        # Option 1: Buy only individual items
        option1 = (need1 * cost1) + (need2 * cost2)

        # Option 2: Buy type 3 items for both requirements
        option2 = max(need1, need2) * costBoth

        # Option 3: Buy common items and remaining individual items
        common = min(need1, need2)

        option3 = (common * costBoth) + ((need1 - common) * cost1) + ((need2 - common) * cost2)

        return min(option1, option2, option3)

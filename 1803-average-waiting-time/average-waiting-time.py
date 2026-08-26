class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        time = total = 0

        for arrival, prep in customers:
            time = max(time, arrival) + prep
            total += time - arrival

        return total / len(customers)  
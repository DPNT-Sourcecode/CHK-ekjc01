from collections import Counter

class CheckoutSolution:
    def checkout(self, skus):
        
        if not all(c in "ABCD" for c in skus):
            return -1
        
        counts = Counter(skus)

        total = 0

        total += (counts["A"] // 3) * 130 + (counts["A"] % 3) * 50
        total += (counts["B"] // 2) * 45 + (counts["B"] % 2) * 30
        total += counts["C"] * 20
        total += counts["D"] * 15

        return total

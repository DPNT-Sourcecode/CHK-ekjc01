from collections import Counter

class CheckoutSolution:
    def checkout(self, skus):
        
        if not all(c in "ABCD" for c in skus):
            return -1
        
        counts = Counter(skus)

        total = 0
        
        free_b = counts["E"] // 2
        counts["B"] = max(0, counts["B"] - free_b)


        total += (counts["A" // 5]) * 200
        remainder_a = counts["A"] % 5
        total += (remainder_a // 3) * 130 + (remainder_a % 3) * 50
        
        total += (counts["B"] // 2) * 45 + (counts["B"] % 2) * 30
        total += counts["C"] * 20
        total += counts["D"] * 15
        total += counts["E"] * 40

        return total




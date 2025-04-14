from collections import Counter

class CheckoutSolution:
    def checkout(self, skus):

        if not all(c in "ABCDEF" for c in skus):
            return -1
        
        counts = Counter(skus)
        total = 0
        
       # multi-item special offers

       # E's Offer: for every 2 Es, get 1 B free
        free_b = counts.get("E", 0) // 2
        counts["B"] = max(0, counts.get("B", 0) - free_b)

       # F's Offer: for every 3 Fs, get one free
        f = counts.get("F", 0)
        payable_f = (f // 3) * 2 + (f % 3)
        total += payable_f * 10

       # A's Offer 
        a = counts.get("A", 0)
        remainder_a = a % 5
        total += (a // 5) * 200
        total += (remainder_a // 3) * 130 + (remainder_a % 3) * 50


        b = counts.get("B", 0)
        total += (b // 2) * 45 + (b % 2) * 30
        
        # Remaining items

        total += counts.get("C", 0) * 20
        total += counts.get("D", 0) * 15
        total += counts.get("E", 0) * 40

    
        return total


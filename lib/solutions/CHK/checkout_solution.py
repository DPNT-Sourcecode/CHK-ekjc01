from collections import Counter

class CheckoutSolution:
    def checkout(self, skus):

        if not all(c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" for c in skus):
            return -1
        
        counts = Counter(skus)
        total = 0
        
       # multi-item special offers

       # A's Offer: 5 for 200, 3 for 130, rmd 50 each
        a = counts.get("A", 0)
        remainder_a = a % 5
        total += (a // 5) * 200
        total += (remainder_a // 3) * 130 + (remainder_a % 3) * 50

       # E's Offer: for every 2 Es, get 1 B free
        free_b = counts.get("E", 0) // 2
        counts["B"] = max(0, counts.get("B", 0) - free_b)

       # B's Offer: 2 B for 45, Standard Price is 30  
        b = counts.get("B", 0)
        total += (b // 2) * 45 + (b % 2) * 30

       # F's Offer: for every 3 Fs, get one free
        f = counts.get("F", 0)
        payable_f = (f // 3) * 2 + (f % 3)
        total += payable_f * 10
        
        # Remaining items at regular price

        total += counts.get("C", 0) * 20
        total += counts.get("D", 0) * 15
        total += counts.get("E", 0) * 40
        total += counts.get("G", 0) * 40
        total += counts.get("I", 0) * 40
        total += counts.get("J", 0) * 40
        total += counts.get("K", 0) * 40
        total += counts.get("L", 0) * 40
        total += counts.get("M", 0) * 40
        total += counts.get("E", 0) * 40
        total += counts.get("E", 0) * 40

        total += counts.get("C", 0) * 20
        total += counts.get("D", 0) * 15
        total += counts.get("E", 0) * 40
        total += counts.get("G", 0) * 20
        total += counts.get("I", 0) * 35
        total += counts.get("J", 0) * 60
        total += counts.get("K", 0) * 70
        total += counts.get("L", 0) * 90
        total += counts.get("N", 0) * 40
        total += counts.get("R", 0) * 50
        total += counts.get("S", 0) * 0  # already counted after W logic
        total += counts.get("T", 0) * 20
        total += counts.get("W", 0) * 20
        total += counts.get("X", 0) * 17
        total += counts.get("Y", 0) * 20
        total += counts.get("Z", 0) * 21

    
        return total


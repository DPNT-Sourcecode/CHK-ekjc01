from collections import Counter

class CheckoutSolution:
    def checkout(self, skus):

        if not all(c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" for c in skus):
            return -1
        
        counts = Counter(skus)
        total = 0
        
       # "MULTI-ITEM SPECIAL" OFFERS

       # A's Offer: 5 for 200, 3 for 130, rmd 50 each
        a = counts.get("A", 0)
        remainder_a = a % 5
        total += (a // 5) * 200
        total += (remainder_a // 3) * 130 + (remainder_a % 3) * 50

       # B's Offer: 2 B for 45, Standard Price 30  
        b = counts.get("B", 0)
        total += (b // 2) * 45 + (b % 2) * 30

       # H's Offer: 10H for 80, 5H for 45, rmd at 10
        h = counts.get("H", 0)
        total += (h // 10) * 80
        h = h % 10
        total += (h // 5) * 45 + (h % 5) * 10

       # P's Offer: 5P for 200
        p = counts.get("P", 0)
        total += (p // 5) * 200 + (p % 5) * 50

       # Q's Offer: 3Q for 80
        q = counts.get("Q", 0)
        total += (q // 3) * 80 + (q % 3) * 30

       # V's Offer: 3V for 130, 2V for 90, rmd at 50
        v = counts.get("V", 0)
        total += (v // 3) * 130
        v %= 3
        total += (v // 2) * 90 + (v % 2) * 50

      # "BUY X GET Y FREE" OFFERS

       # E's Offer: 2 Es, 1B free
        free_b = counts.get("E", 0) // 2
        b = max(0, counts.get("B", 0) - free_b)
        total += (b // 2) * 45 + (b % 2) * 30

       # F's Offer: 3Fs, 1 F Free
        f = counts.get("F", 0)
        payable_f = (f // 3) * 2 + (f % 3)
        total += payable_f * 10

       # I's Offer: 3I, 1 F free ()
        free_f = counts.get("I", 0) // 3

       # N's Offer: 3N, 1 M free
        free_m = counts.get("N", 0) // 3
        m = max(0, counts.get("M", 0) - free_m)
        total += m * 15

       # R's Offer: 3R, 1 Q free
        free_q = counts.get("R", 0) // 3
        q = max(0, counts.get("Q", 0) - free_q)
        total += 0  # already counted above in Q block

       # U's Offer: 3U, 1U free
        u = counts.get("U", 0)
        payable_u = (u // 4) * 3 + (u % 4)
        total += payable_u * 40

       # W's Offer: 2X, 1S free
        free_s = (counts.get("X", 0) // 2)
        s = max(0, counts.get("S", 0) - free_s)
        total += s * 20
        
        # Remaining items at regular price

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
        total += counts.get("T", 0) * 20
        total += counts.get("W", 0) * 20
        total += counts.get("X", 0) * 17
        total += counts.get("Y", 0) * 20
        total += counts.get("Z", 0) * 21
    
        return total


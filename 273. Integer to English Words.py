''' 
Question -
Convert a non-negative integer num to its English words representation.
'''

'''
Difficulty - Hard
'''


class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        def helper(num):
            if num == 0:
                return ""
            elif num < 20:
                return dic[num] + " "
            elif num < 100:
                return dic[num // 10 * 10] + " " + helper(num % 10)
            elif num < 1000:
                return dic[num // 100] + " Hundred " + helper(num % 100)
            else:
                for i, v in enumerate(thousands):
                    if num < 1000 ** (i + 1):
                        return helper(num // 1000 ** i) + v + " " + helper(num % 1000 ** i)

        dic = {
            1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine",
            10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen", 15: "Fifteen", 16: "Sixteen",
            17: "Seventeen", 18: "Eighteen", 19: "Nineteen", 20: "Twenty", 30: "Thirty", 40: "Forty", 50: "Fifty",
            60: "Sixty", 70: "Seventy", 80: "Eighty", 90: "Ninety"
        }
        thousands = ["", "Thousand", "Million", "Billion"]
        return helper(num).strip()


'''
Time Complexity - O(log num)
'''

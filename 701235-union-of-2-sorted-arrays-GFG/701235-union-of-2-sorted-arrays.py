class Solution:
    def findUnion(self, a, b):
        # code here 
        i, j = 0, 0
        n, m = len(a), len(b)
        result = []
        while i < n and j < m:
            if a[i] <= b[j]:
                if len(result) == 0 or result[-1] != a[i]:
                    result.append(a[i])
                i += 1
                    
            else:
                if len(result) == 0 or result[-1] != b[j]:
                    result.append(b[j])
                j += 1
                    
        while i < n:
            if len(result) == 0 or result[-1] != a[i]:
                result.append(a[i])
            i += 1
                    
        while j < m:
            if len(result) == 0 or result[-1] != b[j]:
                result.append(b[j])
            j += 1
                    
        return result

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
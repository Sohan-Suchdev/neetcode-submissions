class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(i):
            return points[i][0]**2 + points[i][1]**2

        def quickselect(l, r):
            if l >= r:
                return
            pivot_val = points[r]
            pivot_dist = distance(r)
            left = l

            for i in range(l, r):
                if distance(i) < pivot_dist:
                    points[i], points[left] = points[left], points[i]
                    left += 1
            
            points[r] = points[left]
            points[left] = pivot_val

            if left == k or left == k - 1:
                return 
            elif left < k:
                quickselect(left + 1, r)
            else:
                quickselect(l, left - 1)

        quickselect(0, len(points) - 1)
        return points[0:k]
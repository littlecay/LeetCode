class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        l1 = ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**0.5
        l2 = ((p1[0]-p3[0])**2 + (p1[1]-p3[1])**2)**0.5
        l3 = ((p1[0]-p4[0])**2 + (p1[1]-p4[1])**2)**0.5
        l4 = ((p2[0]-p3[0])**2 + (p2[1]-p3[1])**2)**0.5
        l5 = ((p2[0]-p4[0])**2 + (p2[1]-p4[1])**2)**0.5
        l6 = ((p3[0]-p4[0])**2 + (p3[1]-p4[1])**2)**0.5

        if (p1 == p2) or (p1 == p3) or (p1 == p4) or (p2 == p3) or (p2 == p4) or (p3 == p4):
            return False
        if (l1 == l2) and (l3 == l4) and (l1 == l5) and (l1 == l6):
            return True
        if (l1 == l3) and (l2 == l5) and (l1 == l6) and (l1 == l4):
            return True
        if (l1 == l6) and (l2 == l3) and (l3 == l4) and (l4 == l5):
            return True
        else:
            return False

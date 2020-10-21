class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        rect1 = (C - A) * (D - B)
        if rect1 < 0:
            rect1 = -1 * rect1
        rect2 = (G - E) * (H - F)
        if rect2 < 0:
            rect2 = -1 * rect2
        overlap = (min(G, C) - max(A, E)) * (min(D, H) - max(B, F))
        if min(G, C) < max(A, E) or min(D, H) < max(B, F):
            return rect1 + rect2
        else:
            return rect1 + rect2 - overlap

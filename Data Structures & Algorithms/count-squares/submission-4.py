class CountSquares:
    def __init__(self):
        #tuple repr point : how many times it appears
        self.points = {}

    def add(self, point: List[int]) -> None:
        point = tuple(point)
        if point not in self.points :
            self.points[point] = 1
        else : 
            self.points[point] += 1

    def count(self, point: List[int]) -> int:
        res = 0
        for point2 in self.points : 
            if ((abs(point2[0] - point[0]) == abs(point2[1] - point[1])) and
                 (point2[0] - point[0] != 0)) :
                to_look1 = [point[0], point2[1]]
                to_look2 = [point2[0], point[1]]
                if (tuple(to_look1) in self.points) and (tuple(to_look2) in self.points) :
                    val1 = self.points[tuple(point2)]
                    val2 = self.points[tuple(to_look1)]
                    val3 = self.points[tuple(to_look2)]
                    if (val1 == 1) and (val2 == 1) and (val3 == 1) :
                        res += 1
                    else : 
                        curr = 1 
                        for val in [val1, val2, val3] :
                            curr *= val
                        res += curr
                    
        return res

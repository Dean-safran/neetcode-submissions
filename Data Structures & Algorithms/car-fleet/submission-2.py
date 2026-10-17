class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if len(position) == 1 :
            return 1

        cars = []
        for i in range(len(position)) :
            cars.append((position[i], speed[i]))
        cars.sort(key=lambda x : x[0])
        num_fleets = len(position)
        fleet_head = len(position) - 1
        for i in range(len(position) - 2, -1, -1) :
            # if speed of curr car is less 
            # than head of fleet behind it
            # and fleet can catch up in time
            if cars[i][1] > cars[fleet_head][1] :
                speed = cars[i][1] - cars[fleet_head][1]
                dist = cars[fleet_head][0] - cars[i][0]
                catch_up_time = dist / speed
                catch_up_pnt = (catch_up_time * cars[fleet_head][1]) + cars[fleet_head][0]
                if (catch_up_pnt) <= target :
                    num_fleets -= 1
                else : 
                    fleet_head = i
            else : 
                fleet_head = i
        return num_fleets

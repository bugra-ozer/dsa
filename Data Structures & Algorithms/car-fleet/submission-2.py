class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet_counter=0
        last_fleet_arrival=0
        sorted_zip=sorted(zip(position, speed), reverse=True)
        for idx in range(len(sorted_zip[0])):
            arrival=(target-sorted_zip[0][idx])//sorted_zip[1][idx]
            if not fleet_counter:
                last_fleet_arrival=arrival
                fleet_counter=1
            if arrival>last_fleet_arrival:
                last_fleet_arrival=arrival
                fleet_counter+=1
        return fleet_counter
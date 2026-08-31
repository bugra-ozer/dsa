class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet_counter=0
        last_fleet_arrival=0
        sorted_zip=sorted(zip(position, speed), reverse=True)
        for idx in range(len(sorted_zip)):
            arrival=(target-sorted_zip[idx][0])/sorted_zip[idx][1]
            if arrival>last_fleet_arrival:
                last_fleet_arrival=arrival
                fleet_counter+=1
        return fleet_counter
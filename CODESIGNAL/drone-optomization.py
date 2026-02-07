"""
Problem Statement:

You are designing a delivery system using drones in a linear warehouse. The warehouse is represented as a number line starting at position 0 and ending at position target (target > 0). Along this line, there are charging stations placed at various positions, represented by an array stations, where stations[i] is the position of the ith charging station. Each drone has a limited battery that allows it to travel a maximum of 10 units after being fully charged. For example, if a drone is charged at position 12, it can travel to positions 12, 13, 14, ..., up to position 22 (inclusive), but cannot reach position 23 or beyond without recharging. Your delivery protocol requires the following steps: From your current_position position, pick up the cargo and carry it on foot to the nearest charging station ahead of you. If there are no more stations ahead, carry the cargo on foot to the target position. Deploy a fully charged drone from this station and send it with the cargo as far as possible toward the target. If the target hasn't been reached, walk to the point where the drone landed to retrieve the cargo, then repeat from step 1. Your task is to calculate the total distance over which you must carry the cargo on foot, from position 0 to position target. Note: You are not expected to provide the most optimal solution, but a solution with time complexity not worse than O(stations.length × target) will fit within the execution time limit.

Assumptions:
- target > 0, integer.
- stations is a list of integers, positions > 0 and <= target, may not be sorted, may have duplicates (but code handles by sorting and unique? but assumes no issue).
- Positions are integers.
- Drone max distance is fixed at 10 units.

Example:
target = 15
stations = [3, 6, 12]
Output: 5  (walk 0 to 3: +3; drone 3 to 13; walk (no carry) to 13; then walk 13 to 15: +2; total 5)
"""

def calculate_foot_distance(target: int, stations: list[int]) -> int:
    if target <= 0:
        return 0  # Invalid, but handle
    
    # Sort stations to efficiently find next
    stations = sorted(set(stations))  # Remove duplicates, sort
    
    foot = 0
    current_position = 0
    i = 0  # Index for next station
    
    while current_position < target:
        # Advance i to the first station > current_position
        while i < len(stations) and stations[i] <= current_position:
            i += 1
        
        if i == len(stations):
            # No more stations, carry to target
            foot += target - current_position
            break
        
        next_s = stations[i]
        
        if next_s >= target:
            # Station at or beyond target, carry to target
            foot += target - current_position
            break
        
        # Carry on foot to next_s
        foot += next_s - current_position
        
        # Deploy drone to as far as possible
        land = min(next_s + 10, target)
        
        # Update current_position to land (walk to land without carry)
        current_position = land
    
    return foot

# Example usage (for testing):
if __name__ == "__main__":
    target = 15
    stations = [3, 6, 12]
    result = calculate_foot_distance(target, stations)
    print(result)  # Output: 5

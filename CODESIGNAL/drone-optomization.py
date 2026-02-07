"""
Problem Statement:

You are designing a delivery system using drones in a linear warehouse. The warehouse is represented as a number line starting at position 0 and ending at position target (target > 0). Along this line, there are charging stations placed at various positions, represented by an array stations, where stations[i] is the position of the ith charging station. Each drone has a limited battery that allows it to travel a maximum of 10 units after being fully charged. For example, if a drone is charged at position 12, it can travel to positions 12, 13, 14, ..., up to position 22 (inclusive), but cannot reach position 23 or beyond without recharging. Your delivery protocol requires the following steps: From your current position, pick up the cargo and carry it on foot to the nearest charging station ahead of you. If there are no more stations ahead, carry the cargo on foot to the target position. Deploy a fully charged drone from this station and send it with the cargo as far as possible toward the target. If the target hasn't been reached, walk to the point where the drone landed to retrieve the cargo, then repeat from step 1. Your task is to calculate the total distance over which you must carry the cargo on foot, from position 0 to position target. Note: You are not expected to provide the most optimal solution, but a solution with time complexity not worse than O(stations.length × target) will fit within the execution time limit.

Pattern Recognition:
This problem follows a greedy simulation pattern, similar to the 'jump game' or 'gas station' problems where you advance as far as possible from each 'refuel' point (here, charging stations). The key is recognizing that the protocol mandates always choosing the nearest next station, creating a sequence of 'carry-then-jump' steps until the target is reached. This is not an optimization problem but a direct simulation of specified rules, akin to traversing a graph with fixed transitions.

Subproblem Breakdown:
- How do I efficiently find the next charging station ahead of my current position?
  Answer: Sort the stations once at the beginning and use a pointer (index) that only moves forward to locate the first station strictly greater than the current position.
- When and how much cargo do I have to carry on foot in each cycle?
  Answer: Carry from the current position to the next valid charging station (or to the target if no station is available ahead), adding (next_position - current) to the total foot distance.
- How far does the drone travel each time I deploy it?
  Answer: From the charging station, the drone can fly up to 10 units forward or until the target, whichever is smaller; this distance is traveled without carrying cost.
- What do I do when there are no more charging stations ahead or the next station is beyond the target?
  Answer: Carry the cargo the remaining distance directly to the target and terminate the process.
- How do I track progress and avoid revisiting stations?
  Answer: Maintain a monotonically increasing current position and advance the station index only forward, ensuring each station is considered at most once.

State and Transitions:
- State: Defined by the current position (integer, 0 <= current <= target) and the index to the next potential station in the sorted list.
- Transitions: 
  - From current, transition to next_station > current (carry cost: next_station - current), then to landing = min(next_station + 10, target) (no cost, update current).
  - If no next_station, transition directly to target (carry cost: target - current).
- The process is deterministic, with states advancing monotonically toward the target.

Constraints Analysis:
- target: Integer, target > 0 (assumed positive as per problem).
- stations: List of integers, 0 <= stations[i] <= target (but stations at 0 or ==target may be ignored if not 'ahead'; code handles by skipping <= current).
- Drone range: Fixed at 10 units (hardcoded, but could be parameterized).
- No stations beyond target assumed (filtered by sort).
- Edge cases: No stations (full carry: target), stations at 0 (skip), stations >= target (may not use if not reached), target <=10 (may have zero carry if station at 0, but protocol starts at 0 without initial station unless present).
- Input size: len(stations) up to, say, 10^5 (but O(n log n + n) fine), target up to 10^9? But since simulation loops O(n) times worst-case (visit each station), and if target large but n small, still fine unless n*target if naive, but here not.
- Assumptions: Positions integers, no negative, stations may have duplicates/unsorted.

Time and Space Complexity:
- Time: O(n log n) for sorting stations (n = len(stations)), then O(n) for simulation (each station considered at most once, loop iterations <= n+1).
- Space: O(n) for sorted stations list.
- Meets the requirement: Better than O(n * target), as simulation doesn't loop over distances but jumps via math.

Example:
target = 15
stations = [3, 6, 12]
Output: 5  (walk 0 to 3: +3; drone 3 to 13; walk (no carry) to 13; then walk 13 to 15: +2; total 5)
"""

def calculate_foot_distance(target: int, stations: list[int]) -> int:
    """
    Calculate the total foot-carrying distance following the drone delivery protocol.

    Args:
    target (int): The end position (>0).
    stations (list[int]): List of charging station positions.

    Returns:
    int: Total foot-carrying distance.

    Time Complexity: O(n log n) due to sorting, O(n) simulation.
    Space Complexity: O(n) for sorted list.
    """
    if target <= 0:
        return 0  # Invalid, but handle
    
    # Sort and deduplicate stations for efficient next lookup
    stations = sorted(set(stations))  # O(n log n)
    
    foot = 0
    current = 0
    i = 0  # Index for next station candidate
    
    while current < target:
        # Advance i to the first station > current
        while i < len(stations) and stations[i] <= current:
            i += 1
        
        if i == len(stations):
            # No more stations, carry to target
            foot += target - current
            break
        
        next_s = stations[i]
        
        if next_s >= target:
            # If next station is at or beyond target, carry remaining distance
            foot += target - current
            break
        
        # Carry on foot to next_s
        foot += next_s - current
        
        # Deploy drone to as far as possible
        land = min(next_s + 10, target)
        
        # Update current to land (walk to land without carry)
        current = land
    
    return foot

# Example usage (for testing):
if __name__ == "__main__":
    target = 15
    stations = [3, 6, 12]
    result = calculate_foot_distance(target, stations)
    print(result)  # Output: 5

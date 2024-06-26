class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        cars = [[position, speed] for position, speed in zip(position, speed)]
        
        for position, speed in sorted(cars)[::-1]:
            stack.append((target - position) / speed)
            if len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
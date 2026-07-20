class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        cars = sorted(zip(position, speed), reverse=True)

        for i, (pos, spd) in enumerate(cars):
            time = float(target - pos) / spd

            if not stack:
                stack.append(time)
            elif time > stack[-1]:
                stack.append(time)
            
        return len(stack)
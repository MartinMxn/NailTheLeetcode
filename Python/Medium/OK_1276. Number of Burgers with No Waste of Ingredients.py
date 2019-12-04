class Solution:
    """
    2 variable equation, classic & historic
    """
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        x = (tomatoSlices - 2 * cheeseSlices) // 2
        y = cheeseSlices - x
        return [x, y] if tomatoSlices % 2 == 0 and tomatoSlices / 4 <= cheeseSlices <= tomatoSlices / 2 else []

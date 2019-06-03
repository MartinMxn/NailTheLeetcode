#class Robot(object):
#    def move(self):
#    def turnLeft(self):
#    def turnRight(self):
#    def clean(self):

class Solution(object):
    def cleanRoom(self, robot):
        """     
        intuition:
        check for every single cell and clean
        dfs for 4 directions each time
        dfs: 
            1.clean current and record to set
            2.check for next direction cell, if not visited, then move
            3.turn left or right and change the direction
            4.until for 4 directions are all all gone
        """
        visited = set()
        def dfs(x, y, dir_x, dir_y):
            robot.clean()
            visited.add((x, y))
#             for _ in range(4):
#                 if (x + dx, y + dy) not in path and robot.move():
#                     dfs(x + dx, y + dy, dx, dy)
#                 robot.turnLeft()
#                 dx, dy = -dy, dx
            for _ in range(4):
                if (x + dir_x, y + dir_y) not in visited and robot.move():
                    dfs(x + dir_x, y + dir_y, dir_x, dir_y)
                robot.turnLeft()
                # !! go to new direction, new to the dir before turn left
                # dir_x, dir_y = -dir_y, dir_x
                tmp = dir_x
                dir_x = -dir_y
                dir_y = tmp
                
            # ! back to previous postion
            robot.turnLeft()
            robot.turnLeft()
            robot.move()
            robot.turnRight()
            robot.turnRight()

        dfs(0, 0, 0, 1)

import time



class Maze(object):
    """A pathfinding problem."""

    def __init__(self, grid, location):
        """Instances differ by their current agent locations."""
        self.grid = grid
        self.location = location
    
    def display(self):
        """Print the maze, marking the current agent location."""
        for r in range(len(self.grid)):
            for c in range(len(self.grid[r])):
                if (r, c) == self.location:
                    print '*',
                else:
                    print self.grid[r][c],
            print
        print

    def moves(self):
        """Return a list of possible moves given the current agent location."""
        possible_moves = []
        (r, c) = self.location # type: (object, object)
        if self.grid[r-1][c] == ' ':
            possible_moves.append((r-1, c))
        if self.grid[r+1][c] == ' ':
            possible_moves.append((r+1, c))
        if self.grid[r][c+1] == ' ':
            possible_moves.append((r, c+1))
        if self.grid[r][c-1] == ' ':
            possible_moves.append((r, c-1))
        return possible_moves
        # YOU FILL THIS IN
    
    def neighbor(self, move):
        """Return another Maze instance with a move made."""
        if(self.moves().count(move) > 0):
            return Maze(self.grid, move)
        # YOU FILL THIS IN


class Agent(object):
    """Knows how to find the exit to a maze with BFS."""

    def bfs(self, maze, goal):
        """Return an ordered list of moves to get the maze to match the goal."""

        visited = {maze.location: None}
        queue = [maze.location]
        went = []
        path = []
        reversed_path = []

        while len(queue) > 0:
            parent = queue.pop(0)
            child_maze = Maze(maze.grid, parent)
            for r in range(len(child_maze.moves())):
                child = child_maze.moves().pop(r)
                if child not in visited:
                    visited[child] = parent
                    went.append(child)
                    queue.append(child)
                goal_key = (19, 18)
                if child == goal.location:
                    while goal_key != None:
                        path.append(goal_key)
                        goal_key = visited[goal_key]
                    for item in path[::-1]:
                        reversed_path.append(item)
                    print reversed_path
                    reversed_path.remove((1, 1)) # Don't need first element
                    return reversed_path

    def dfs(self, maze, goal):
        visited = {maze.location: None}
        queue = [maze.location]
        went = []
        path = []
        reversed_path = []

        while len(queue) > 0:
            parent = queue.pop(0)
            child_maze = Maze(maze.grid, parent)
            for r in range(len(child_maze.moves())):
                child = child_maze.moves().pop(r)
                if child not in visited:
                    visited[child] = parent
                    went.insert(0, child)
                    queue.insert(0, child) # put whatever found at beginning of queue

                # Return the correct path trace
                goal_key = (19, 18)
                if child == goal.location:
                    while goal_key != None:
                        path.append(goal_key)
                        goal_key = visited[goal_key]
                    for item in path[::-1]:
                        reversed_path.append(item)
                    print reversed_path
                    reversed_path.remove((1, 1))  # Don't need first element
                    return reversed_path


def main():
    """Create a maze, solve it with BFS, and console-animate."""
    
    grid = ["XXXXXXXXXXXXXXXXXXXX",
            "X     X    X       X",
            "X XXXXX XXXX XXX XXX",
            "X       X      X X X",
            "X X XXX XXXXXX X X X",
            "X X   X        X X X",
            "X XXX XXXXXX XXXXX X",
            "X XXX    X X X     X",
            "X    XXX       XXXXX",
            "XXXXX   XXXXXX     X",
            "X   XXX X X    X X X",
            "XXX XXX X X XXXX X X",
            "X     X X   XX X X X",
            "XXXXX     XXXX X XXX",
            "X     X XXX    X   X",
            "X XXXXX X XXXX XXX X",
            "X X     X  X X     X",
            "X X XXXXXX X XXXXX X",
            "X X                X",
            "XXXXXXXXXXXXXXXXXX X"]

    maze = Maze(grid, (1,1))
    maze.display()

    agent = Agent()
    goal = Maze(grid, (19, 18))
    path = agent.bfs(maze, goal)

    while path:
        move = path.pop(0)
        maze = maze.neighbor(move)
        time.sleep(0.5)
        maze.display()


if __name__ == '__main__':
    main()
import curses
import random
import time

def main(stdscr):
    # Set up the screen
    curses.curs_set(0)  # Hide the cursor
    sh, sw = stdscr.getmaxyx()
    w = curses.newwin(sh, sw, 0, 0)
    w.keypad(1)
    w.timeout(100)  # Refresh every 100ms

    # Initial position
    snk_x = sw // 4
    snk_y = sh // 2
    snake = [
        [snk_y, snk_x],
        [snk_y, snk_x - 1],
        [snk_y, snk_x - 2]
    ]

    # Initial food
    food = [sh // 2, sw // 2]
    w.addch(food[0], food[1], curses.ACS_PI)

    key = curses.KEY_RIGHT
    score = 0

    while True:
        next_key = w.getch()
        key = key if next_key == -1 else next_key

        # Check for game over
        if (snake[0][0] in [0, sh - 1] or 
            snake[0][1] in [0, sw - 1] or 
            snake[0] in snake[1:]):
            break

        # Calculate new head
        new_head = [snake[0][0], snake[0][1]]

        if key == curses.KEY_DOWN:
            new_head[0] += 1
        if key == curses.KEY_UP:
            new_head[0] -= 1
        if key == curses.KEY_LEFT:
            new_head[1] -= 1
        if key == curses.KEY_RIGHT:
            new_head[1] += 1

        snake.insert(0, new_head)

        # Eating food
        if snake[0] == food:
            score += 1
            food = None
            while food is None:
                nf = [
                    random.randint(1, sh - 2),
                    random.randint(1, sw - 2)
                ]
                food = nf if nf not in snake else None
            w.addch(food[0], food[1], curses.ACS_PI)
        else:
            tail = snake.pop()
            w.addch(tail[0], tail[1], ' ')

        # Draw snake
        try:
            w.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)
        except curses.error:
            pass

    # Game Over message
    stdscr.clear()
    msg = f"Game Over! Your Score: {score}"
    stdscr.addstr(sh // 2, (sw - len(msg)) // 2, msg)
    stdscr.addstr(sh // 2 + 1, (sw - 23) // 2, "Press any key to exit.")
    stdscr.refresh()
    stdscr.nodelay(0)
    stdscr.getch()

if __name__ == "__main__":
    curses.wrapper(main)

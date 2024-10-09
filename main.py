import tkinter as tk
import random

class StackingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Stacking Game")
        self.canvas = tk.Canvas(root, width=400, height=600, bg='lightblue')
        self.canvas.pack()

        # Game variables
        self.stack = []
        self.stack_height = 0
        self.game_over = False

        # Start the game
        self.root.after(1000, self.create_disc)
        self.update_game()

    def create_disc(self):
        """Creates a new falling disc"""
        width = random.randint(60, 100)
        height = random.randint(20, 50)
        x = random.randint(0, 400 - width)
        y = 0
        disc = self.canvas.create_oval(x, y, x + width, y + height, fill='red')
        self.stack.append({"disc": disc, "width": width, "height": height, "x": x, "y": y, "falling": True})

        # Schedule next disc
        self.root.after(random.randint(2000, 4000), self.create_disc)

    def update_game(self):
        """Update the game state every frame"""
        if not self.game_over:
            self.move_discs()
            self.root.after(50, self.update_game)  # 20 FPS (50 ms per frame)

    def move_discs(self):
        """Move the discs down and stack them when caught"""
        for disc_data in self.stack:
            if disc_data["falling"]:
                self.canvas.move(disc_data["disc"], 0, 5)
                disc_data["y"] += 5

                # Check if disc hits the stack or ground
                if self.stack_height > 0:
                    stack_top = self.canvas.coords(self.stack[-2]["disc"])[1]
                else:
                    stack_top = 600

                # If the disc touches the stack, stop falling
                if disc_data["y"] + disc_data["height"] >= stack_top:
                    disc_data["falling"] = False
                    self.stack_height += disc_data["height"] * 2
                    self.check_stability()

    def check_stability(self):
        """Checks if the stack is stable or collapsed"""
        # Logic to check for stack collapse can be added here
        pass

# Main game loop
if __name__ == "__main__":
    root = tk.Tk()
    game = StackingGame(root)
    root.mainloop()

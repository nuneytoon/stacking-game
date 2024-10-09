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
        self.create_disc()
        self.update_game()

    def create_disc(self):
        """Creates a new falling disc"""
        radius = random.randint(30, 60)
        x = random.randint(radius, 400 - radius)
        y = 0
        disc = self.canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill='red')
        self.stack.append({"disc": disc, "radius": radius, "x": x, "y": y, "falling": True})

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
                if disc_data["y"] + disc_data["radius"] >= stack_top:
                    disc_data["falling"] = False
                    self.stack_height += disc_data["radius"] * 2
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

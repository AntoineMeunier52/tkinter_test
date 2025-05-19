from tkinter import *

class Window():
	def __init__(self, width, height):
		self._root = Tk()
		self._root.title("Maze Solver")
		self._root.geometry(f"{width}x{height}")
		self._root.minsize(480, 360)
		self._root.config(background="white")
		self._root.protocol("WM_DELETE_WINDOW", self.close)

		self._menu = Menu(self._root, self._switch_view)
		self._maze = Maze(self._root, self._switch_view)
		self._is_running = False
		self._can_change_view = False
		self._menu.show()

	def _switch_view(self):
		print("in switch view")
		self._can_change_view=True

	def _change_view(self):
		print("menu", self._menu.is_visible)
		print("maze", self._maze.is_visible)
		if self._menu.is_visible:
			self._menu.destroy()
			self._maze.show()
		elif self._maze.is_visible:
			self._maze.destroy()
			self._menu.show()

	def redraw(self):
		self._root.update_idletasks()
		self._root.update()

	def wait_for_close(self):
		self._is_running = True
		while self._is_running:
			if self._can_change_view :
				self._change_view()
				self._can_change_view = False
			self.redraw()
		print("The window is now close")
		return

	def close(self):
		self._is_running = False
		print("Closing the window")
		return

class Menu():
	def __init__(self, root, callback):
		self._frame = Frame(root, bg="white", height=100, width=200)
		self._start_callback = callback
		self.is_visible = False
		#self.maze_size_x = IntVar(10)
		#self.maze_size_y = IntVar(10)
		#self.algo = StringVar("DFS")

		self.build_menu()

	def build_menu(self):
		Label(self._frame, text="Maze Solver", font=("roboto", 40), bg="white", fg="black").grid(row=0)
		maze_size_frame = Frame(self._frame, width=200, height=100, bg="white")
		maze_size_frame.grid(row=1)
		Label(maze_size_frame, text="Enter the size of the maze", font=("roboto", 16), bg="white", fg="black").grid(row=0, column=0)
		Label(maze_size_frame, text="X and Y must be between 10 and 40.", font=("roboto", 10), bg="white", fg="black").grid(row=1, column=0)

		x_y_frame = Frame(maze_size_frame, width=200, height=100, bg="white")
		x_y_frame.grid(row=2)
		Label(x_y_frame, text="X: ", bg="white", fg="Black", font=("roboto", 12)).grid(row=0, column=0)
		Label(x_y_frame, text="Y: ", bg="white", fg="Black", font=("roboto", 12)).grid(row=0, column=1)

		Button(self._frame, text="change view", command=self._start_maze).grid(row=2)
	def _start_maze(self):
		self._start_callback()

	def show(self):
		self.is_visible = True
		self._frame.pack(expand=YES)

	def destroy(self):
		self.is_visible = False
		self._frame.pack_forget()

class Maze():
	def __init__(self, root, callback):
		self._frame = Frame(root, bg="white", height=100, width=200)
		self._start_callback = callback
		self.is_visible = False
		#self.maze_size_x = IntVar(10)
		#self.maze_size_y = IntVar(10)
		#self.algo = StringVar("DFS")

		self.build_menu()

	def build_menu(self):
		Label(self._frame, text="Maze Maze", font=("roboto", 40), bg="white", fg="black").pack()
		Label(self._frame, text="Enter the size of the maze", font=("roboto", 16), bg="white", fg="black").pack()
		Label(self._frame, text="X and Y must be between 10 and 40.", font=("courrier", 10), bg="white", fg="black").pack()
		Button(self._frame, text="change view", command=self._start_maze).pack()
	def _start_maze(self):
		self._start_callback()

	def _start_maze(self):
		self._start_callback()

	def show(self):
		self.is_visible = True
		self._frame.pack(expand=YES)

	def destroy(self):
		self.is_visible = False
		self._frame.pack_forget()

def main():
	win = Window(1080, 720)
	win.wait_for_close()

main()

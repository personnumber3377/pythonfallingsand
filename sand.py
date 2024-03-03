
import matplotlib.pyplot as plt


# Used in rendering
import numpy as np


class SandSim:
	
	def __init__(self, sand_particles: list, width: int, height: int) -> None:
		# Constructor.
		self.sand_particles = set(sand_particles)
		self.width = width
		self.height = height
		#self.figure = plt.figure()
		#self.image = plt.imshow(np.zeros((self.width, self.height)), cmap='gray')

		self.cur_height = 0

		#plt.figure()
		plt.ion()
	
	def valid_spot(self, point):
		# Checks if the point is actually a valid position.
		# First check the x coordinate.
		x = point[0]
		y = point[1]
		if x < 0 or x > self.width-1:
			return False
		if y < 0 or y > self.height-1:
			return False
		return True

	def new_pos(self, point) -> None: # This returns the new position of a point.
		'''
		if point[1] > self.cur_height:
			# We are still in the air for certain.
			if (point[0], point[1]-1) not in self.sand_particles:

				return (point[0], max(0, point[1] - 1))
		'''

		if point[1] == 0: # Check if the sand particle is on the ground
			return point
		if (point[0], point[1]-1) not in self.sand_particles:
			return (point[0], point[1]-1)
		# Now go over the three points which are below this one.
		below_points = [(point[0]-1, point[1]-1), (point[0], point[1]-1), (point[0]+1, point[1]-1)]
		are_below_list = [p in self.sand_particles for p in below_points]
		if not are_below_list[1]:
			# Return the point which is straight below.
			if self.valid_spot(below_points[1]):
				return below_points[1]
		if not are_below_list[0]: # Left point is open, therefore return that.
			if self.valid_spot(below_points[0]):
				return below_points[0]
		if not are_below_list[2]: # Left point is open, therefore return that.
			if self.valid_spot(below_points[2]):
				return below_points[2]

		# No need to check. Assumed.
		#if all(are_below_list): # All three points below are occupied, therefore do not move point.
		assert self.valid_spot(point) # Should be vald
		self.cur_height = point[1]
		return point

	def update(self) -> None:
		'''
		new_particle_set = set()
		# Loop over the current particles and see if they can be moved.
		for p in self.sand_particles:
			new_particle_set.add(self.new_pos(p))
		self.sand_particles = new_particle_set
		return
		'''
		for p in self.sand_particles:
			self.sand_particles.remove(p)
			self.sand_particles.add(self.new_pos(p))
		return

		#return # just a stub for now.

	def to_bool_mat(self): # Converts the current points to a boolean matrix.
		mat = [[0 for _ in range(self.width)] for _ in range(self.height)]
		for p in self.sand_particles:
			mat[p[1]][p[0]] = 1
		# Reverse list, because otherwise positive y direction is down.
		mat = list(reversed(mat))
		return mat

	def render(self) -> None:
		# First convert the current point list to a grayscale matrix
		render_mat = self.to_bool_mat()
		
		#plt.show()
		#self.figure.show(render_mat, cmap="gray")


		plt.imshow(render_mat, cmap="gray")
		plt.show()
		plt.pause(0.01)
		plt.clf()


		#return # just a stub for now.


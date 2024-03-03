
import random
import time
from sand import *

def gen_rand_point(max_x, max_y):
	return (random.randrange(max_x), random.randrange(max_y))

def create_random_sand(width: int, height: int, n: int) -> list: # Returns a list of tuples, where each tuple is (x,y)
	# Tries to create n points.
	out = set()
	for _ in range(n):
		rand_point = gen_rand_point(width, height)
		if rand_point not in out:
			out.add(rand_point)
	return list(out) # Return as list

def fall_sand() -> None:
	# Create random sand particles.
	# create_random_sand(width: int, height: int, n: int)
	# def __init__(self, sand_particles: list, width: int, height: int) -> None:
	width = 100
	height = 100
	amount = 1000
	sand_particles = create_random_sand(width, height, amount)
	simulation = SandSim(sand_particles, width, height)
	# Update and render loop.
	orig_point_amount = len(sand_particles)
	while True:
		print("New loop!")
		#time.sleep(0.2) # Slow it down a bit.
		simulation.update()
		simulation.render()
		print("len(simulation.sand_particles) == "+str(len(simulation.sand_particles)))
		#assert len(simulation.sand_particles) == orig_point_amount
	return


def main() -> int:
	fall_sand()
	return 0

if __name__=="__main__":
	exit(main())

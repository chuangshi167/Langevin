# -*- coding: utf-8 -*-

"""Main module."""

import numpy as np
import matplotlib.pyplot as plt
import argparse



def drag_force(gamma, velocity):
	""" 
	This function calculates the drag force in Langevin Dynamics
	"""
	return -gamma * velocity


def check_range(location, wall_size):
	"""
	This function tests if the molecule is within the range
	wall size have to be greater than 0
	"""	
	if location <= wall_size and location >= 0:
		return True
	else:
		return False


def random_force(T, _lambda, k_B = 1, delta = 1):
	"""
	This function generates random random noise (random force), throught the function noise = 2k_B * T * lambda * delta.
	THe noise is generated normally from the mean, which is 0
	"""
	variance = 2 * k_B * T * _lambda * delta
	sigma = np.sqrt(variance)
	return np.random.normal(0, sigma)


def integrator(initial_position, initial_velocity, temperature, damping_coefficient, time_step, total_time, wall_size = 5):
	"""
	This function integrate the acceleration of the particle to get the velocity of the particle, and it also integrate the velocity of the particle to obtain the distance travelled.
	Thhe integration is based on Euler's method.
	"""
	intermediates = int(total_time/time_step + 1)
	time = np.linspace(0, total_time, intermediates)
	position = np.zeros(intermediates)
	velocity = np.zeros(intermediates)
	position[0] = initial_position
	velocity[0] = initial_velocity
	for i in range (1, intermediates):
		DragForce = drag_force(damping_coefficient, velocity[i - 1])
		RandomForce = random_force(temperature, damping_coefficient)
		dv_over_dt = DragForce + RandomForce
		velocity[i] = velocity[i - 1] + time_step * dv_over_dt
		position[i] = position[i - 1] + time_step * velocity[i - 1]
		if not check_range(position[i], wall_size):
			break
	return time[: i], velocity[: i], position[: i]


def histogram(stop_time, run):
	"""
	This function generates a histogram
	"""
	plt.figure()
	plt.hist(stop_time, bins = 20)
	plt.xlabel("Time before hitting the wall")
	plt.ylabel("Times")
	plt.title("Histogram of {} runs ".format(run))
	plt.savefig("Histogram.png")


def trajectory(time, position):
	"""
	This function generates a trajectory
	"""
	plt.figure()
	plt.plot(time, position)
	plt.xlabel("time")
	plt.ylabel("position")
	plt.title("Trajectory")
	plt.savefig("Trajectory.png")


def output(time, position, velocity):
	"""
	This function creates a txt file that contains the position and velocity of a particle at a certain time
	"""
	file = open("Langevin output.txt", "w+")
	file.write("index	time	position	velocity \n")
	for i in range(0, len(time)):
		file.write("{}	{:.2f}	{:.2f}		{:.2f} \n".format(i, time[i], position[i], velocity[i]))
	file.close()


def create_parser():
	"""
	This function creates a parser for command line
	"""
	parser = argparse.ArgumentParser(description = "Necessary input for the Langevin Dynamics")	
	parser.add_argument("--initial_position", type = float, default = 0, help = "Initial position of the particle, default = 0")
	parser.add_argument("--initial_velocity", type = float, default = 0, help = "Initial velocity of the particle, default = 0")
	parser.add_argument("--temperature", type = float, default = 300, help = "Temperature of the particle, default = 300")
	parser.add_argument("--damping_coefficient", type = float, default = 0.1, help = "Damping coefficient of the particle, default = 0.1")
	parser.add_argument("--time_step", type = float, default = 0.01, help = "Time step of the process, default = 0.01")
	parser.add_argument("--total_time", type = float, default =1000, help = "Total time of the process, default =1000")
	parser.add_argument("--wall_size", type = float, default = 5, help = "The size of the wall, default = 5")
	parser.add_argument("--run_times", type = int, default = 100, help = "The run times for histogramgeneration, default = 100")
	args = parser.parse_args()
	return args


def main():
	"""
	This is the main function
	"""
	args = create_parser()
	time_matrix = []
	position_matrix = []
	velocity_matrix = []
	stop_time = np.zeros(args.run_times)
	for i in range(args.run_times):
		time, velocity, position = integrator(args.initial_position, args.initial_velocity, args.temperature, args.damping_coefficient, args.time_step, args.total_time, args.wall_size)
		time_matrix.append(time)
		position_matrix.append(position)
		velocity_matrix.append(velocity)
		stop_time[i] = time[-1]
	
	index = np.argmax(stop_time)
	maxrun_time = time_matrix[index]
	maxrun_velocity = velocity_matrix[index]
	maxrun_position = position_matrix[index]
	
	output(maxrun_time, maxrun_position, maxrun_velocity)
	histogram(stop_time, args.run_times)
	trajectory(maxrun_time, maxrun_position)
		
		
if __name__ == '__main__':
	main()	

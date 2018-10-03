# -*- coding: utf-8 -*-

"""Main module."""

import numpy as np
import matplotlib.pyplot as plt
import argparse



def drag_force(gamma, velocity):
	""" 
	This function calculates the drag force in Langevin Dynamics
	"""
	#The equation for drag_force in Langevin Dynamics is -gamma * velocity
	return -gamma * velocity


def check_range(location, wall_size):
	"""
	This function tests if the molecule is within the range
	wall size have to be greater than or equal to 0, and be smaller than euqal to wall_size
	"""
	if location <= wall_size and location >= 0:
		return True
	else:
		return False


def random_force(T, _lambda, k_B = 1, epsilon = 1):
	"""
	This function generates random random noise (random force), throught the function variance = 2k_B * T * lambda * epsilon and the function sigma = sqrt(variance).
	THe noise is generated normally from the mean, which is 0
	"""
	variance = 2 * k_B * T * _lambda * epsilon
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
		#If the particle hits the wall, it will stop the iteration.
		if not check_range(position[i], wall_size):
			break
	#Return three list of particles velocity and position at a certain time, before hitting the wall
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
	#Write the velocity and position of the particle at a certain time, before hitting the wall, into a .txt file"
	for i in range(0, len(time)):
		file.write("{}	{:.2f}	{:.2f}		{:.2f} \n".format(i, time[i], position[i], velocity[i]))
	file.close()


def create_args():
	"""
	This function separates the parameters from command line input
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


def check_input(args):
	"""
	This function checks if the parameters in the input argument are valid or not
	"""
	if args.initial_position < 0 or args.initial_position > args.wall_size:
		return False
	if args.initial_velocity < 0:
		return False
	if args.temperature <= 0:
		return False
	if args.damping_coefficient < 0:
		return False
	if args.time_step < 0:
		return False
	if args.total_time <= args.time_step:
		return False
	if args.run_times < 0:
		return False
	else:
		return True


def main():
	"""
	This is the main function
	"""
	args = create_args()
	if not check_input(args):
		print("The input parameters are not correct, please check readme file")
	else:

		#Three lists that contain the time, position and velocity of each run, as lists
		time_matrix = []
		position_matrix = []
		velocity_matrix = []
		#A list that stores the time before the particle hit the wall, in each run
		stop_time = np.zeros(args.run_times)
		for i in range(args.run_times):
			time, velocity, position = integrator(args.initial_position, args.initial_velocity, args.temperature, args.damping_coefficient, args.time_step, args.total_time, args.wall_size)
			time_matrix.append(time)
			position_matrix.append(position)
			velocity_matrix.append(velocity)
			stop_time[i] = time[-1]
		#Choose the longest run and get its time, velocity and position data from the previous matrices
		index = np.argmax(stop_time)
		maxrun_time = time_matrix[index]
		maxrun_velocity = velocity_matrix[index]
		maxrun_position = position_matrix[index]
		#Generate a output file of the longest run
		output(maxrun_time, maxrun_position, maxrun_velocity)
		#Generate a histogram of the runs
		histogram(stop_time, args.run_times)
		#Generate a trajectory of the longest run
		trajectory(maxrun_time, maxrun_position)
		
		
if __name__ == '__main__':
	main()

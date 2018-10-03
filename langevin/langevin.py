# -*- coding: utf-8 -*-

"""Main module."""

import numpy as np
import scipy.stats as ss
import matplotlib.pyplot as plt




def drag_force(gamma, velocity):
	""" 
	This function calculates the drag force in Langevin Dynamics
	"""
	return -gamma * velocity


def check_range(location):
	"""
	This function tests if the molecule is within the range
	"""
	
	if location < 5 and location > -5:
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


def integrator(initial_position, initial_velocity, temperature, damping_coefficient, time_step, total_time):
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
		if not check_range(position[i]):
			break
	return time[: i], velocity[: i], position[: i]


def histogram(stop_time, run):
	"""
	This function generates a histogram
	"""
	plt.figure()
	plt.hist(stop_time, bins = 20)
	plt.xlabel("Time when hit the wall")
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


def parser():
	"""
	This function creates a parser for command line
	"""
	


# -*- coding: utf-8 -*-

"""Main module."""

import numpy as np
import scipy.stats as ss
import matplotlib as plt


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


def integrator(initial_position, velocity, temperature, damping_coefficient, time_step, total_time):
	return


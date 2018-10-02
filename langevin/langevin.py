# -*- coding: utf-8 -*-

"""Main module."""

import numpy as np
import scipy.stats as ss
import matplotlib as plt


def drag_force(damping_coefficient, velocity):
	""" 
	This function calculate the drag force in Langevin Dynamics
	"""
	return -damping_coefficient * velocity




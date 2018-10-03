#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `langevin` package."""

import unittest
import pytest
import langevin.langevin as langevin
import random
import numpy as np
import matplotlib
import os

class Test(unittest.TestCase):	
	def test_drag_force(self):
		"""
		unit test for testing the function drag_force
		"""
		dragForce = langevin.drag_force(2, 3)
		self.assertEqual(dragForce, -6)
	def test_check_range(self):
		"""
		unit test for testing the function check_range
		"""
		self.assertTrue(langevin.check_range(random.random() * 5))
		self.assertTrue(langevin.check_range(random.random() * (-5)))
		self.assertFalse(langevin.check_range(10))
		self.assertFalse(langevin.check_range(-10))
	def test_random_force(self):
		"""
		unit test for testing the function random_force
		"""
		_random_force = []
		T = 273.15
		_lambda = 0.07
		theoretical_value = 2 * T * _lambda
		for i in range(10000):
			_random_force.append(langevin.random_force(T, _lambda))
		mean = np.mean(_random_force)
		variance = np.var(_random_force)
		self.assertTrue(mean < 0.2 or mean > -0.2)
		self.assertTrue(variance > 0.98 * theoretical_value or variance < 1.02 * theoretical_value)
	def test_integrator(self):
		"""
		unit test for testing the function integrator
		"""
		initial_position = 0
		initial_velocity = random.random()
		temperature = 298
		damping_coefficient = random.random()
		time_step = random.random()
		total_time = 1000
		time, velocity, position = langevin.integrator(initial_position, initial_velocity, temperature, damping_coefficient, time_step, total_time)
		self.assertEqual(len(time), len(velocity))
		self.assertEqual(len(velocity), len(position))
		self.assertEqual(time[0], 0)
		self.assertEqual(velocity[0], initial_velocity)
		self.assertEqual(position[0], initial_position)
		for i in range(len(position)):
			self.assertTrue(position[i] < 5)
			self.assertTrue(position[i] > -5)

	def test_histogram(self):
		"""
		This is the unit test for histogram
		"""
		langevin.histogram(10, 100)
		self.assertTrue(os.path.isfile("Histogram.png"))

	
	def test_trajectory(self):
		"""
		This is the unit test for trajectory function
		"""
		time = np.linspace(0, 100, 101)
		position = np.linspace(-5, 5, 101)
		langevin.trajectory(time, position)
		self.assertTrue(os.path.isfile("Trajectory.png"))
	
	
	def test_output(self):
		"""
		This is the unit test for output function
		"""
		time = np.linspace(0, 100, 101)
		position = np.linspace(-5, 5, 101)
		velocity = np.linspace(-1, 1, 101)
		langevin.output(time, position, velocity)
		with open("Langevin output.txt") as file:
			line = file.readline()
			self.assertEqual(line, "index	time	position	velocity \n")

if __name__ == '__main__':
	unittest.main()

#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `langevin` package."""

import unittest
import pytest
import langevin.langevin as langevin
import random
import numpy as np


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
			
		
if __name__ == '__main__':
	unittest.main()

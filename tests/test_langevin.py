#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `langevin` package."""

import unittest
import pytest
import langevin.langevin as langevin


class Test(unittest.TestCase):	
	def test_drag_force(self):
		"""
		unit test for testing the function drag_force
		"""
		dragForce = langevin.drag_force(2, 3)
		self.assertEqual(dragForce, -6)
if __name__ == '__main__':
	unittest.main()

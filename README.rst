========
Langevin
========


.. image:: https://img.shields.io/travis/chuangshi167/langevin.svg
        :target: https://travis-ci.org/chuangshi167/langevin

.. image:: https://coveralls.io/repos/github/chuangshi167/langevin/badge.svg?branch=master
	:target: https://coveralls.io/github/chuangshi167/langevin?branch=master




Python Boilerplate contains all the boilerplate you need to create a Python package.


* Free software: MIT license
* Documentation: https://langevin.readthedocs.io.

Description
-----------
This project is for CHE 477, University of Rochester.

It is a Lagevin Dynamics Simulator for Brownian motion.

In this simulator, there are a few assumptions made:

* The potential force is ignored, and the only two forces acting on the particle of interest are drag force and random force.

- Drag force depends on the damping coefficient and velocity of the particle.

- Random force depends on the temperature and damping coefficient.

* There is a range in which the particle can move. Once the particle hits the boundary of the range, it stops.

* The position of the particle at a certain time is calculated based on Euler's method.

How to use
----------

This simulator can be invoked from the terminal, using the following command::

	 python langevin/langevin.py
 
There are a few preset parameters that can be modified in the argument.

They are:

- initial_position    Type: float default = 0

- initial_velocity    Type: float default = 0

- temperature         Type: float default = 300

- damping_coefficient Type: float default = 0.1

- time_step           Type: float default = 0.01

- total_time          Type: float default = 1000

- wall_size           Type: float default = 5

- run_times           Type: float default = 100

If you would like to change any of the preset parameters, using the following command::

	python langevin/langevin.py --initial_position 0 --initial_velocity 0 --temperature 300 --dampig_coefficient 0.1 --time_step 0.01 --total_time 1000 --wall_size 5 --run_times 100

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

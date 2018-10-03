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
This project is for CHE 477, University of Rochester. \n
It is a Lagevin Dynamics Simulator for Brownian motion.\n
In this simulator, there are a few assumptions made:\n
* The potential force is ignored, and the only two forces acting on the particle of interest are drag force and random force.\n
Drag force depends on the damping coefficient and velocity of the particle.\n
Random force depends on the temperature and damping coefficient.\n

* There is a range in which the particle can move. Once the particle hits the boundary of the range, it stops.

* The position of the particle at a certain time is calculated based on Euler's method.

How to use
----------

This simulator can be invoked from the terminal, using the following command \n
* python langevin/langevin.py \n
There are a few preset parameters that can be modified in the argument.\n
They are:\n
|Parameter|Type|Default|
|---|---|---|
|initial position|float|0|


Features
--------

* TODO

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

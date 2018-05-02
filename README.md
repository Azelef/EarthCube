# EarthCube
Find interesting cubes on Earth using Google Maps data.

This repository contains two files :
altimap.py contains fonctions to extract elevation data using the Google Maps elevation API (https://developers.google.com/maps/documentation/elevation/start)

cubeFinder.py generates random cubes with their 8 vertices on the surface of the Earth and calculates the elevation of their lowest vertex. It repeats this process in order to find cubes with all vertices close to land. This file contains fonctions to:
-Get the elevation of a point.
-Convert a point given as a vector into a latitude and a longitude.
-Draw a simple map of the world.
-Draw a map of the world that show positions of the vertices of a given cube.

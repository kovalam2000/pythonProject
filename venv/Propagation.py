import pandas as pd
from sgp4.api import Satrec
import math
import numpy as np
from astropy.time import Time

# Global Variables
k = 2 * math.pi;  # Factor from [rev/s] to [rad/s]
body_radius = 6.378e6;  # Radius of the primary body [m]
extra_radius = 20000;  # Extra radius for the primary body [m]
S = body_radius + extra_radius;  # Magnitude of the rise-set vector [m]
mu = 3.986004418e14;  # Standard gravitational parameter [m3/s2]

# ISS
s = '1 25544U 98067A   21017.72756503  .00000379  00000-0  14866-4 0  9994'
t = '2 25544  51.6466   6.9156 0000286 262.1360 269.8785 15.49296897265270'

satellite = Satrec.twoline2rv(s, t)

incl = satellite.inclo  # inclination in radians
raan = satellite.nodeo  # RAAN in radians
omega = satellite.argpo  # argument of the pergiee in radians
M = satellite.mo  # mean anomaly in radians
n = satellite.no_kozai / 60  # mean motion in radians/second
a = satellite.a * body_radius  # semi major axis
e = satellite.ecco  # eccentricty



jd, fr = 2458827, 0.362605
e, r, v = satellite.sgp4(jd, fr)

print(r)
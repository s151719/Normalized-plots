from netCDF4 import Dataset
import functools
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
from scipy import ndimage

fh1 = Dataset('output01.nc')
fh2 = Dataset('output1.nc')
fh3 = Dataset('output02.nc')

energy_time1 = fh1.variables['energy_time'][:]
mass1 = fh1.variables['mass'][:]
energy_time2 = fh2.variables['energy_time'][:]
mass2 = fh2.variables['mass'][:]
energy_time3 = fh3.variables['energy_time'][:]
mass3 = fh3.variables['mass'][:]

fig, ax = plt.subplots()
lines1 = plt.plot(energy_time1, (mass1-mass1[0])/mass1[0], energy_time2, (mass2-mass2[0])/mass2[0], energy_time3, (mass3-mass3[0])/mass3[0])
plt.legend(lines1[:3], [r'$\nu = 1 \cdot 10^{-3}$', r'$\nu = 5 \cdot 10^{-3}$', r'$\nu = 9 \cdot 10^{-3}$'])
plt.xlabel(r't [$\omega_{ci}^{-1}$]', fontsize=14)
plt.ylabel(r'$\frac{m(t)-m(0)}{m(0)}$', fontsize=14)
ax.yaxis.set_major_formatter(ScalarFormatter(useOffset=False))
plt.show()

kinetic1 = fh1.variables['kinetic'][:]
kinetic2 = fh2.variables['kinetic'][:]
kinetic3 = fh3.variables['kinetic'][:]
curvature1 = fh1.variables['curvature'][:]
curvature2 = fh2.variables['curvature'][:]
curvature3 = fh3.variables['curvature'][:]
TE1 = kinetic1 + curvature1
TE2 = kinetic2 + curvature2
TE3 = kinetic3 + curvature3

lines2 = plt.plot(energy_time1, (TE1-TE1[0]), energy_time2, (TE2-TE2[0]), energy_time3, (TE3-TE3[0]))
plt.legend(lines2[:3], [r'$\nu = 1 \cdot 10^{-3}$', r'$\nu = 5 \cdot 10^{-3}$', r'$\nu = 9 \cdot 10^{-3}$'])
plt.xlabel(r't [$\omega_{ci}^{-1}$]', fontsize=14)
plt.ylabel(r'$E_{tot}(t)-E_{tot}(0)$ [$m_ic_s^2$]', fontsize=14)
plt.show()

entropy1 = fh1.variables['entropy'][:]
entropy2 = fh2.variables['entropy'][:]
entropy3 = fh3.variables['entropy'][:]

lines3 = plt.plot(energy_time1, ((entropy1 + kinetic1)-(entropy1[0] + kinetic1[0])), energy_time2, ((entropy2 + kinetic2)-(entropy2[0] + kinetic2[0])), energy_time3, ((entropy3 + kinetic3)-(entropy3[0] + kinetic3[0])))
plt.legend(lines3[:3], [r'$\nu = 1 \cdot 10^{-3}$', r'$\nu = 5 \cdot 10^{-3}$', r'$\nu = 9 \cdot 10^{-3}$'])
plt.xlabel(r't [$\omega_{ci}^{-1}$]', fontsize=14)
plt.ylabel(r'T(t)-T(0) [$m_ic_s^2$]', fontsize=14)
plt.show()


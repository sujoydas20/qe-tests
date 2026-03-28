import numpy as np
import matplotlib.pyplot as plt

# Load 3 columns
energy, dos, idos = np.loadtxt('graphene_dos.dat', unpack=True)

# Shift Fermi level
fermi = -2.67
energy = energy - fermi

# Plot
plt.figure(figsize=(8,5))
plt.plot(energy, dos)

plt.axvline(0)

plt.xlim(-5, 5)
plt.ylim(0, 2)

plt.xlabel('Energy (eV)')
plt.ylabel('DOS')
plt.title('Graphene DOS')

plt.grid()

plt.savefig('graphene_dos.png', dpi=300)
plt.show()

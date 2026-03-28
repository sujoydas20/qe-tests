import numpy as np
import matplotlib.pyplot as plt

bands = []
kpoints = []

with open('graphene_band.dat') as f:
    lines = f.readlines()[1:]  # skip header

for i in range(0, len(lines), 2):
    e_line = lines[i+1].split()
    kpoints.append(len(kpoints))
    bands.append([float(e) for e in e_line])

bands = np.array(bands)

# Shift Fermi level
fermi = -2.67
bands = bands - fermi

plt.figure(figsize=(7,5))

# Plot all bands in black
for i in range(bands.shape[1]):
    plt.plot(kpoints, bands[:, i], color='black', linewidth=1)

# Fermi level (horizontal line)
plt.axhline(0, linestyle='--', linewidth=1)

# Vertical symmetry lines
plt.axvline(0, linestyle='--', linewidth=1)
plt.axvline(20, linestyle='--', linewidth=1)
plt.axvline(40, linestyle='--', linewidth=1)
plt.axvline(60, linestyle='--', linewidth=1)

# Labels
plt.xlabel('k-path')
plt.ylabel('Energy (eV)')

# High symmetry points
plt.xticks([0, 20, 40, 60], ['Γ', 'K', 'M', 'Γ'])

# Limits
plt.ylim(-10, 10)

# Clean look
plt.grid(False)

plt.savefig('graphene_band_clean.png', dpi=300)
plt.show()

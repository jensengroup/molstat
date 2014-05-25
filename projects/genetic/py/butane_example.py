import molecule as mol
import numpy as np

n_carbon = 4
n_dihedral = 1

# Create the molecule
mol.generate_alkane(n_carbon)

# Create the dihedral angles
sample_dihedral = np.random.uniform(0.0, 360.0, n_dihedral)
print sample_dihedral

# Set the dihedral angles
mol.set_dihedral(sample_dihedral)

# Get the energy
print mol.get_energy()

# Save the structure
mol.save_molecule('random_butane.xyz')


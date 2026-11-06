import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy as scp

# Import data
RDF_PF_dat = pd.read_excel(r"C:\Users\nkwon\OneDrive\Python\Data\RDF_PF_Data.xlsx")
RDF_PF_arr = RDF_PF_dat.to_numpy()
RDF_bulk_dat = pd.read_excel(r"C:\Users\nkwon\OneDrive\Python\Data\RDF_bulk_Data.xlsx")
RDF_bulk_arr = RDF_bulk_dat.to_numpy()

# Isolate g(r), r
RDF_PF_vect = RDF_PF_arr[:, 2]
RDF_bulk_vect = RDF_bulk_arr[:, 2]
radius_PF_vect = RDF_PF_arr[:, 1]
radius_bulk_vect = RDF_bulk_arr[:, 1]

# Initialization of radii, RDFs for bulk and PF
n_steps = 500
RDF_PF_avg = np.zeros(n_steps)
RDF_bulk_avg = np.zeros(n_steps)
rad_PF_avg = np.zeros(n_steps)
rad_bulk_avg = np.zeros(n_steps)

# Generation of averaged vectors for bulk and PF radius, RDFs
for k in range(1, n_steps+1):
    RDF_dat_bool = RDF_PF_arr[:, 0] == k

    RDF_PF_avg[k-1] = np.average(RDF_PF_vect[RDF_dat_bool])
    RDF_bulk_avg[k-1] = np.average(RDF_bulk_vect[RDF_dat_bool])
    rad_PF_avg[k-1] = np.average(radius_PF_vect[RDF_dat_bool])
    rad_bulk_avg[k-1] = np.average(radius_bulk_vect[RDF_dat_bool])

# Extract Maximum r from both
max_PF_bool = RDF_PF_avg == RDF_PF_avg.max()
rad_max_PF = rad_PF_avg[max_PF_bool][0]
max_bulk_bool = RDF_bulk_avg == RDF_bulk_avg.max()
rad_max_bulk = rad_bulk_avg[max_bulk_bool][0]
print("Max PF r = {} nm, Max bulk r = {} nm".format(rad_max_PF, rad_max_bulk))

# Plot
plt.plot(rad_PF_avg, RDF_PF_avg, color = 'blue', label = 'Precursor Film RDF')
plt.plot(rad_bulk_avg, RDF_bulk_avg, color = 'black', label = 'Bulk RDF')
plt.legend()
plt.xlabel("Radial Distance ($AA$)")
plt.ylabel("Radial Distribution Function")
plt.show()



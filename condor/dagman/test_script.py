#!/usr/bin/env python

import os
import pickle
import argparse
import matplotlib
matplotlib.use('Agg')

from matplotlib import pyplot as plt
import numpy as np
from scipy.stats import norm

parser = argparse.ArgumentParser()
parser.add_argument("-o", "--outfile", type=str, required=True,
                    help = "Name of the output file (ending in .npy")
parser.add_argument("-p", "--plotfile", type=str, default=None,
                    help = "If given, create a histogram of the values and save it here.")
parser.add_argument("-n", "--nvalues", type=int,
                    default = 10000,
                    help = "The number of random values to create")
parser.add_argument("--gaussian", default=False, action="store_true",
                    help = "If given, produce values from a Gaussian instead of"
                           " from a uniform distribution")
args = parser.parse_args()


# Going to generate some basic test data
if args.gaussian:
    my_random_values = norm.rvs(loc=0, scale=1, size=args.nvalues)
else:
    my_random_values = np.random.uniform(low=-1, high=1, size=args.nvalues)

# Save the files
np.save(args.outfile, my_random_values)

# Are we making a plot?
if args.plotfile is not None:
    fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(8, 5))

    ax.hist(my_random_values,
            bins = np.linspace(-1, 1, 101),
            histtype='step',
            linewidth=3,
            color='k',
            label = "My values!")

    # Add a legend
    ax.legend(loc='upper right', framealpha=1, fontsize=12)

    # Make it look nice
    ax.grid(alpha=0.25)
    ax.set_xlim(xmin=-1, xmax=1)
    ax.set_xlabel("Random values", fontsize=16)
    ax.set_ylabel("Number of values in each bin", fontsize=16)

    # Make the numbers on the axis larger
    ax.tick_params(labelsize=12)

    # Move things around to fix any spacing issues
    fig.tight_layout()

    # And save
    plt.savefig(args.plotfile)
    

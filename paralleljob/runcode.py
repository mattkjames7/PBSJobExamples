import numpy as np
import os

#this is the array index - note that the indices in myjob.sub
#started with "1", here it was converted to an integer starting
#at 0. This can be changed to be whatever, the environment variable
#PBS_ARRAYID will always be a string which corresponds to one of the
#array job IDs listed in the job submission file.
I = np.int32(os.getenv('PBS_ARRAYID')) - 1


#parallelized python code here

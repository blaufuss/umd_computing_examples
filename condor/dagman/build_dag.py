#!/usr/bin/env python

# test_script.py [-h] -o OUTFILE [-p PLOTFILE] [-n NVALUES] [--gaussian]
# Want to run 100 files with 10000 values each with gaussian
# + 100 files with 10000 values each with uniform

path = "/data/condor_shared/users/blaufuss/umd_computing_examples/condor/dagman/"
executable = path + "test_script.py"
sub_name = path + "submit.sub"
logdir = path + "logs/"
outfile_dir = path + "output/"

dagman = ""

for gaussian in [True, False]:
    for i in range(100):
        if gaussian: job_name = "gaussian_"
        else: job_name = "uniform_"

        job_name += str(i)
        dagman += f"JOB {job_name} {sub_name}\n"
        dagman += f"VARS {job_name} "
        dagman += f"executable=\"{executable}\" "
        dagman += f"args=\""
        dagman += f" -o {outfile_dir}{job_name}.npy "
        dagman += f" -p {outfile_dir}{job_name}.pdf "
        dagman += f" -n 10000 "
        if gaussian:
            dagman += " --gaussian"
        dagman += "\""

        dagman += f" logfile=\"{logdir}{job_name}.log\""

        dagman += "\n"


with open("my_dagman.dag", "w") as f:
    f.write(dagman)

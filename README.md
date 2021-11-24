# Notes on submitting jobs to ALICE

TL;DR: Copy one of these folders, `$cd` into it, add your python code to "runcode.py", edit myjob.sub to have the correct vram etc., then run `$ ./submitjob.sh`

## Templates

This folder contains three templates: "singlejob", "arrayjob" and "paralleljob". Each contains four files which can be tweaked as necessary and one output folder ("`out/`") which `stdout` and `stderr` are written to while the job is running.

### singlejob

This template can be used to submit a single job.

### arrayjob

This tamplate can be used to submit an array of jobs, where, for example, the same bit of code may be run in each instance, but on a different set of parameters (e.g. date).

The relevant part of the job submission code:

```bash
#PBS -t 1-1000
```

where `1-1000` indicates a range of job indices from 1 to 1000. This could also be an explicit list, e.g. `2,5,7,99`.

### paralleljob

This is an example of a parallelised job. This is also an array job, but it is also applicable to single jobs. This will run code which, in each instance, will use multiple cores (e.g. using openMP) and/or nodes (e.g. using openMPI).

The relevant part of the job submission script:

```bash
#PBS -l nodes=1:ppn=8
```

where `nodes=1` denotes the number of nodes over which this code can be distributed upon, and `ppn=8` states how many procesors to assign per node.



## Job Files

It is important that "submitjob.sh" and "startscript.sh" are marked as executable, e.g.

```bash
chmod +x submitjob.sh
```

### submitjob.sh

This script will submit the job to the cluster by running the command: `$ ./submitjob.sh` 

While it isn't necessary -  it pretty much just calls the `qsub` command, it saves some typing and it passes the current working directory to the job script so that the correct output folder is used.

### myjob.sub

This contains all of the job configuration options, e.g.

```bash
#PBS -v WD
```

This passes environment variables fromt he current session (where the job is submitted) to the running code. In this case `WD` is the working directory provided in "submitjob.sh".

```bash
#PBS -o out/output.txt
```

This is the name of the output file where `stdout` will be saved.

```bash
#PBS -e out/error.txt
```

This is the output error file where `stderr` saved.

```bash
#PBS -N ParallelArrayJob
```

This is the name of the job.

```bash
#PBS -l walltime=0:15:00
```

This is the total amount of time for the job to run in `hh:mm:ss`. For longer jobs, add days before hours, e.g `dd:hh:mm:ss`.

```bash
#PBS -l vmem=20gb
```

This is the total amount of virtual memory to assign to the job. Ideally this should not be much more than it actually requires (more jobs can run at a time in that case).

```bash
#PBS -m bea
```

This tells the cluster to send an email when each job begins `b` , ends `e` or is aborted `a`. Be warned - this will send those emails for each element of an array job!

```bash
#PBS -l nodes=1:ppn=8
```

This is for jobs which will be able to use more than one single thread. `nodes` is the number of nodes requested for each instance of the job. `ppn` is the number of processors to assign for each node.

```bash
#PBS -t 1-50
```

Array job range.

After the `#PBS` options are defined, the rest of this file can be treated as a `bash` script which will be executed when the job starts. In this case, each job will call `$WD/startscript.sh`  - this isn't necessary, the commands from within "startscript.sh" can be placed directly within this job submission file if desired.

### startscript.sh

This file contains the commands to be called when each job runs. It can be placed directly in "myjob.sub", but a separate script is used here. This file is where `python` or `idl` may be called, for example.

### runcode.py

This file contains the python code to run in the job. It assumes that the job to be submitted will be running `python` and can be replaced with scipts for other languages as needed.

For array jobs, it is important to access the ```PBS_ARRAYID``` environment variable using the ```os.getenv()``` function.
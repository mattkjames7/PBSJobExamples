#the -u flag runs python in unbuffered mode so that "print" 
#statements get written to stdout as they happen,
#rather than in batches every now and again (makes)
#tracking the job a bit easier with the output files
python3 -u $WD/runcode.py

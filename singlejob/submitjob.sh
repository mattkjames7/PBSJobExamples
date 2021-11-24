#/bin/bash
#pass the current working directory to the script
export WD=$(pwd)
echo 'Working from' $WD
qsub myjob.sub

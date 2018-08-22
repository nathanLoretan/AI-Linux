#!/bin/bash

if [ $1 == "sfs" ]
then
        python weight_plot.py /home/nathan/share/prioweight.txt  'SFS - prio weight'  1000 &
        python weight_plot.py /home/nathan/share/blockweight.txt 'SFS - block weight' 1000 &
        python weight_plot.py /home/nathan/share/lockweight.txt  'SFS - lock weight'  1000 &
        python weight_plot.py /home/nathan/share/sleepweight.txt 'SFS - sleep weight' 1000 &

elif [ $1 == "sb" ]
then
        python weight_plot.py /home/nathan/share/deltaexecweight_sb.txt  'SB - delta exec. weight'  1000 &
        python weight_plot.py /home/nathan/share/blockweight_sb.txt      'SB - block weight'        1000 &
        python weight_plot.py /home/nathan/share/completionweight_sb.txt 'SB - comp weight'         1000 &
        python weight_plot.py /home/nathan/share/schedweight_sb.txt      'SB - sched weight'         1000 &

else
        python weight_plot.py /home/nathan/share/prioweight.txt  'SFS - prio weight'  1000 &
        python weight_plot.py /home/nathan/share/blockweight.txt 'SFS - block weight' 1000 &
        python weight_plot.py /home/nathan/share/lockweight.txt  'SFS - lock weight'  1000 &
        python weight_plot.py /home/nathan/share/sleepweight.txt 'SFS - sleep weight' 1000 &

        python weight_plot.py /home/nathan/share/deltaexecweight_sb.txt  'SB - delta exec. weight'  1000 &
        python weight_plot.py /home/nathan/share/blockweight_sb.txt      'SB - block weight'  1000 &
        python weight_plot.py /home/nathan/share/completionweight_sb.txt 'SB - comp weight'  1000 &
        python weight_plot.py /home/nathan/share/schedweight_sb.txt      'SB - sched weight'  1000 &
fi

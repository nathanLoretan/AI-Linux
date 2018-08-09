#!/bin/bash

mount -t 9p -o trans=virtio host0 /mnt -oversion=9p2000.L

python /home/weight_reset.py /mnt/prioweight.txt  &
python /home/weight_reset.py /mnt/blockweight.txt &
python /home/weight_reset.py /mnt/lockweight.txt  &
python /home/weight_reset.py /mnt/sleepweight.txt &

# python /home/weight_reset.py /mnt/deltaexecweight_sb.txt  &
# python /home/weight_reset.py /mnt/blockweight_sb.txt      &
# python /home/weight_reset.py /mnt/completionweight_sb.txt &
# python /home/weight_reset.py /mnt/schedweight_sb.txt      &

nice -n -20 su -c "python /home/weight_read.py /proc/schedai_debug /mnt/prioweight.txt  prioweight  1 &"
nice -n -20 su -c "python /home/weight_read.py /proc/schedai_debug /mnt/blockweight.txt blockweight 1 &"
nice -n -20 su -c "python /home/weight_read.py /proc/schedai_debug /mnt/lockweight.txt  lockweight  1 &"
nice -n -20 su -c "python /home/weight_read.py /proc/schedai_debug /mnt/sleepweight.txt sleepweight 1 &"

# nice -n -20 su -c "python /home/weight_read.py /proc/schedsb_debug /mnt/deltaexecweight_sb.txt  deltaexecweight  1 &"
# nice -n -20 su -c "python /home/weight_read.py /proc/schedsb_debug /mnt/blockweight_sb.txt      blockweight      1 &"
# nice -n -20 su -c "python /home/weight_read.py /proc/schedsb_debug /mnt/completionweight_sb.txt completionweight 1 &"
# nice -n -20 su -c "python /home/weight_read.py /proc/schedsb_debug /mnt/schedweight_sb.txt      schedweight      1 &"

# nice -n  20 su -c "stress-ng --cpu 10 &"
# nice -n  10 su -c "stress-ng --cpu 10 &"
# nice -n   0 su -c "stress-ng --cpu 10 &"
# nice -n -10 su -c "stress-ng --cpu 10 &"

stress-ng --io 20 &
stress-ng --fallocate 20 &

# stress-ng --switch 20 &
# stress-ng --dentry 20 &

case "$1" in
  start)
    echo "Starting script measurement"
    echo "Nothing to do!"
    ;;
  stop)
    echo "Stopping script measurement"
    echo "Nothing to do!"
    ;;
  *)
    echo "Usage: /etc/init.d/measurement {start|stop}"
    exit 1
    ;;
esac

exit 0

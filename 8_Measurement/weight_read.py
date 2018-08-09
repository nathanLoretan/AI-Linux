from threading import Timer
import sys
import calendar
import time
import numpy as np

# This script takes 4 argument:
#
#     1. Proc filename from which to get the value
#         - schedai_debug
#         - schedsb_debug
#     2. The filename where the data are saved for then plotting
#         - SynchCounter.txt
#         - loadweight.txt
#         - blockweight.txt
#         - lockweight.txt
#         - sleepweight.txt
#         - SynchCounter_sb.txt
#         - dexecweight_sb.txt
#         - blockweight_sb.txt
#         - completionweight_sb.txt
#         - schedweight_sb.txt
#     3. The type of data considered
#         - SynchCounter
#         - loadweight
#         - blockweight
#         - lockweight
#         - sleepweight
#         - dexecweight
#         - completionweight
#         - schedweight
#     4. Interval when to get new values

def get_weight():

    global time_cnt

    # Read Debug file
    try:
        debug = open(DEBUG_PROC, "r")
    except IOError:
        print "File ", DEBUG_PROC, "doesn't exist!!!"
        return 0

    features = np.asarray(debug.readlines())[:15]
    debug.close()

    cnt = 0

    # Parse line to get value
    for i in range(len(features)):

        # Remove useless character
        features[i] = features[i].replace(" ", "").replace("\n", "").lower()

        type  = features[i][:features[i].find(":")]
        value = features[i][features[i].find(":")+1:]

        if type == "synchcounter":
            cnt = value

        # Attrbiute the value to the right element
        if type == DEBUG_WEIGHT:
            file = open(DEBUG_FILE, 'a')
            file.write(str(cnt) + ',' + str(value) + '\n')
            file.close()

    # time in second
    t = Timer(DEBUG_INTERVAL, get_weight).start()

if __name__ == "__main__":

    global DEBUG_FILE
    global DEBUG_INTERVAL
    global DEBUG_WEIGHT

    DEBUG_PROC      = str(sys.argv[1])
    DEBUG_FILE      = str(sys.argv[2])
    DEBUG_WEIGHT    = str(sys.argv[3])
    DEBUG_INTERVAL  = int(sys.argv[4])#s

    # time in second
    t = Timer(DEBUG_INTERVAL, get_weight).start()

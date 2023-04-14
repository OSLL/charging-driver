#!/bin/bash

source /environment.sh

# initialize launch file
dt-launchfile-init

# YOUR CODE BELOW THIS LINE
# ----------------------------------------------------------------------------


# NOTE: Use the variable DT_REPO_PATH to know the absolute path to your code
# NOTE: Use `dt-exec COMMAND` to run the main process (blocking process)

# this is necessary for the camera pipeline to work on the Jetson Nano
if [ "${ROBOT_HARDWARE}" == "jetson_nano" ]; then
    export LD_PRELOAD=${LD_PRELOAD}:/usr/lib/aarch64-linux-gnu/libGLdispatch.so
fi

# set module's health
dt-set-module-healthy

# launching app
dt-exec roslaunch connection_status connection_status.launch veh:="$VEHICLE_NAME"


# ----------------------------------------------------------------------------
# YOUR CODE ABOVE THIS LINE

# wait for app to end
dt-launchfile-join

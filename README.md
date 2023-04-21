# dt-ros-commons

Status:
[![Build Status](http://build-arm.duckietown.org/job/Docker%20Autobuild%20-%20dt-ros-commons/badge/icon.svg)](http://build-arm.duckietown.org/job/Docker%20Autobuild%20-%20dt-ros-commons/)
[![Docker Hub](https://img.shields.io/docker/pulls/duckietown/dt-ros-commons.svg)](https://hub.docker.com/r/duckietown/dt-ros-commons)

Repository containing driver to check charging connection. It used for automatic charging process.

## How to launch manually
Clone this repository and build the project with next command: `$ dts devel build -f -H <autobot name>`

To run docker container on the duckiebot, use the next command: `$ docker -H <HOSTNAME>.local run —name charging_driver -v /dev/mem —privileged —network=host -dit —restart unless-stopped -e ROBOT_TYPE=duckiebot docker.io/duckietown/charging-driver:automatic-charging-arm32v7`. Hostname is the name of the bot, for example "autobot03".

If you want to see log info, connect to duckiebot via ssh (use command `$ ssh duckie@<autobot name>.local` and use the next command: `$ docker logs —tail 50 —follow —timestamps charging_driver`

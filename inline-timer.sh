#!/usr/bin/env bash

# This is task for yac-2018:
while True; do clear && date | awk -F ' |:' '{print 28-$3 ":" 24+10-$4 ":" 60-$5 ":" 60-$6}' && sleep 0.5; done


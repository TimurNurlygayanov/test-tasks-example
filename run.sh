#!/usr/bin/env bash

for i in {1..20}; do
    python3 many_requests.py & pids[${i}]=$!
done

echo "started 10 scripts with 100 requests in each script"

# wait for all pids
for pid in ${pids[*]}; do
    wait $pid
done

echo "done"

#!/bin/sh
# #760 item 7: run the orbit-decision probe under a bound, and print the bound when it is
# reached, so that "did not return" is a line in the transcript rather than a silence.
#
#   usage (inside the sage runtime):
#     sh computations/reports/coble_760-orbit-decision-probe.sh [BOUND_SECONDS]
#
# The command this file issues is the one that produced
# coble_760-orbit-decision-probe-run.txt.
BOUND=${1:-600}
timeout "$BOUND" python /repo/computations/reports/coble_760-orbit-decision-probe.py
status=$?
echo "PROBE_EXIT=$status"
if [ "$status" -eq 124 ] || [ "$status" -eq 137 ]; then
  echo "BOUND-REACHED: K.primitive_orbit_series did not return within ${BOUND} s"
fi

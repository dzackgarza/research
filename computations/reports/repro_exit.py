"""Controlled child behaviours for the cusp launcher regression (#749): no lattice math.

The `incomplete` mode reproduces the reported jmw69fxhq behaviour exactly: the child prints a
provenance header and exits zero with no result.
"""
import os
import signal
import sys

mode = sys.argv[1] if len(sys.argv) > 1 else "incomplete"
print("child-start mode=%s" % mode)
if mode == "normal":
    print("T_En.cusps(2) -> 2 records   (0 s)")   # the anchored result format
elif mode == "incomplete":
    print("sage_indefinite_port: /repo/.scratch/port-held/src/sage_indefinite_port")
    print("sage_extensions:      /prov/src/sage_extensions")
    print("T_En: rank 12, det 1024, signature (2, 10)")
    sys.exit(0)                                   # header only, no result, clean exit
elif mode == "exit3":
    sys.exit(3)
elif mode == "segv":
    os.kill(os.getpid(), signal.SIGSEGV)
elif mode == "raise":
    raise RuntimeError("controlled failure")

"""Controlled child behaviours for the cusp launcher regression (#749): no lattice math."""
import os
import signal
import sys

mode = sys.argv[1]
print("child-start mode=%s" % mode)
if mode == "normal":
    print("T_En.cusps(2) -> 2 records   (0 s)")   # the required result marker
elif mode == "exit3":
    sys.exit(3)
elif mode == "segv":
    os.kill(os.getpid(), signal.SIGSEGV)
elif mode == "raise":
    raise RuntimeError("controlled failure")

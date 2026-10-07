# Repo-scoped stubs; see lexicon/README.md.
#
# cysignals/alarm.pyx of cysignals 1.12.6, which SageMath re-exports from
# sage.all. `inspect.signature` gives `alarm(seconds)` and `cancel_alarm()`.

def alarm(seconds: float) -> None: ...
def cancel_alarm() -> None: ...

# Origin: gitclones/integral_lattice/scripts/aut_group.py
# Copied 2026-08-20 by the integral_lattice enrichment migration
# (PLAN-corpora-audit-registry, section R3). Content below is unmodified.

"""
Automorphism group dispatcher as a library module.

Public API:
    - AutResult (dataclass)
    - compute_aut(obj, **opts)
    - aut_group(obj, **opts)  # alias

Options (kwargs to compute_aut / aut_group):
    order: bool = True                # compute order if possible
    show_gens: bool = False           # return generators when available
    algorithm: str | None = None      # passed to handlers that accept it
    timeout: int | None = None        # per-handler timeout in seconds; None disables
    force_gap: bool = False           # currently unused guard placeholder
"""
from __future__ import annotations

import signal
import time
from dataclasses import dataclass, field
from typing import Any, Callable, List, Optional, Sequence, Tuple

from sage.all import MatrixGroup, PermutationGroup, gap


@dataclass
class AutResult:
    handler: str
    group: Any
    order: Optional[int] = None
    gens: Optional[List[Any]] = None
    warnings: List[str] = field(default_factory=list)


Handler = Callable[[Any, dict], Optional[AutResult]]


def _safe_order(group: Any) -> Optional[int]:
    if group is None:
        return None
    try:
        return int(group.order())
    except Exception:
        return None


def _group_and_gens_from_matrix_gens(gens: Sequence[Any]) -> Tuple[Optional[Any], List[Any]]:
    gens_list = list(gens) if gens is not None else []
    group = None
    try:
        if gens_list:
            group = MatrixGroup(gens_list)
    except Exception:
        group = None
    return group, gens_list


def handler_automorphism_group(obj: Any, opts: dict) -> Optional[AutResult]:
    if not hasattr(obj, "automorphism_group"):
        return None
    try:
        kwargs = {}
        if opts.get("algorithm") is not None:
            kwargs["algorithm"] = opts["algorithm"]
        group = obj.automorphism_group(**kwargs)
        res = AutResult(handler="automorphism_group", group=group)
        res.order = _safe_order(group) if opts.get("order", True) else None
        try:
            res.gens = list(group.gens()) if opts.get("show_gens") else None
        except Exception:
            res.gens = None
        return res
    except Exception as e:
        return AutResult(handler="automorphism_group", group=None, warnings=[f"failed: {e}"])


def handler_aut_group_gens(obj: Any, opts: dict) -> Optional[AutResult]:
    if not hasattr(obj, "automorphism_group_gens"):
        return None
    try:
        gens = obj.automorphism_group_gens()
        group = None
        try:
            group = PermutationGroup(gens)
        except Exception:
            group = None
        res = AutResult(handler="automorphism_group_gens", group=group, gens=list(gens))
        if opts.get("order", True) and group is not None:
            res.order = _safe_order(group)
        if group is None:
            res.warnings.append("could not build group from generators")
        return res
    except Exception as e:
        return AutResult(handler="automorphism_group_gens", group=None, warnings=[f"failed: {e}"])


def handler_aut(obj: Any, opts: dict) -> Optional[AutResult]:
    if not hasattr(obj, "aut"):
        return None
    try:
        group = obj.aut()
        res = AutResult(handler="aut", group=group)
        res.order = _safe_order(group) if opts.get("order", True) else None
        try:
            res.gens = list(group.gens()) if opts.get("show_gens") else None
        except Exception:
            res.gens = None
        return res
    except Exception as e:
        return AutResult(handler="aut", group=None, warnings=[f"failed: {e}"])


def handler_free_abelian(obj: Any, opts: dict) -> Optional[AutResult]:
    # Handle free abelian groups/modules of rank n via GL_n(ZZ)
    try:
        from sage.all import ZZ, identity_matrix
    except Exception:
        return None
    rank = None
    if hasattr(obj, "rank"):
        try:
            rank = int(obj.rank())
        except Exception:
            rank = None
    if rank is None:
        return None
    if rank <= 0:
        return None
    try:
        gens = [identity_matrix(ZZ, rank)[i] for i in range(rank)]
        # build standard generators of GL_n(Z): elementary matrices
        mats = []
        for i in range(rank):
            for j in range(rank):
                if i == j:
                    continue
                m = identity_matrix(ZZ, rank)
                m[i, j] = 1
                mats.append(m)
        for i in range(rank):
            m = identity_matrix(ZZ, rank)
            m[i, i] = -1
            mats.append(m)
        group = MatrixGroup(mats)
        res = AutResult(handler="free_abelian_GLnZ", group=group)
        res.order = _safe_order(group) if opts.get("order", True) else None
        if opts.get("show_gens"):
            res.gens = mats
        return res
    except Exception as e:
        return AutResult(handler="free_abelian_GLnZ", group=None, warnings=[f"failed: {e}"])


def handler_aut_generators_matrix(obj: Any, opts: dict) -> Optional[AutResult]:
    if not hasattr(obj, "automorphism_group_generators"):
        return None
    try:
        gens = obj.automorphism_group_generators()
        group, gens_list = _group_and_gens_from_matrix_gens(gens)
        res = AutResult(handler="automorphism_group_generators", group=group, gens=gens_list)
        if opts.get("order", True):
            if hasattr(obj, "automorphism_group_order"):
                try:
                    res.order = int(obj.automorphism_group_order())
                except Exception:
                    res.order = _safe_order(group)
            else:
                res.order = _safe_order(group)
        return res
    except Exception as e:
        return AutResult(handler="automorphism_group_generators", group=None, warnings=[f"failed: {e}"])


def handler_gap(obj: Any, opts: dict) -> Optional[AutResult]:
    gap_obj = None
    if hasattr(obj, "gap"):
        try:
            gap_obj = obj.gap()
        except Exception:
            gap_obj = None
    if gap_obj is None and hasattr(obj, "_gap_"):
        try:
            gap_obj = obj._gap_()
        except Exception:
            gap_obj = None
    if gap_obj is None:
        return None
    warnings = []
    try:
        Ggap = gap.AutomorphismGroup(gap_obj)
    except Exception as e:
        return AutResult(handler="gap.AutomorphismGroup", group=None, warnings=[f"failed: {e}"])
    group = None
    try:
        group = Ggap.sage()
    except Exception:
        group = None
        warnings.append("could not convert GAP group to Sage; returning GAP object")
    res = AutResult(handler="gap.AutomorphismGroup", group=group if group is not None else Ggap, warnings=warnings)
    if opts.get("order", True):
        try:
            res.order = int(Ggap.Size())
        except Exception:
            res.order = _safe_order(group)
    try:
        if group is not None and opts.get("show_gens"):
            res.gens = list(group.gens())
    except Exception:
        res.gens = None
    return res


HANDLERS = [
    handler_automorphism_group,
    handler_free_abelian,
    handler_aut_group_gens,
    handler_aut,
    handler_aut_generators_matrix,
    handler_gap,
]


def _run_with_timeout(func: Handler, obj: Any, opts: dict) -> Optional[AutResult]:
    timeout = opts.get("timeout")
    if not timeout or not hasattr(signal, "SIGALRM"):
        return func(obj, opts)

    def _raise_timeout(signum, frame):
        raise TimeoutError()

    old = signal.signal(signal.SIGALRM, _raise_timeout)
    signal.alarm(int(timeout))
    try:
        return func(obj, opts)
    except TimeoutError:
        return AutResult(handler=getattr(func, "__name__", "handler"), group=None, warnings=["timeout"])
    finally:
        signal.alarm(0)
        signal.signal(signal.SIGALRM, old)


def compute_aut(obj: Any, **opts) -> AutResult:
    errors: List[str] = []
    for handler in HANDLERS:
        res = _run_with_timeout(handler, obj, opts)
        if res is None:
            continue
        if res.group is not None or (res.order is not None):
            return res
        errors.extend(res.warnings)
    raise RuntimeError("No automorphism handler succeeded: " + "; ".join(errors))


def aut_group(obj: Any, **opts) -> AutResult:
    return compute_aut(obj, **opts)

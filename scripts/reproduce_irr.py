#!/usr/bin/env python3
"""Reproduce Study 2 Table 2 (pre-adjudication IRR, Pass 1 and Pass 2) from the
pseudonymized tables in data/. Writes results/irr_pass1.json and results/irr_pass2.json."""
import csv, json, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from agreement import agreement
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BUCKETS = ["1", "2a", "2b", "3"]
MECHS = ["vendor_default", "explicit_check", "no_prompt_path",
         "vendor_default+explicit_check", "vendor_default+no_prompt_path",
         "explicit_check+no_prompt_path", "vendor_default+explicit_check+no_prompt_path"]
rd = lambda p: list(csv.DictReader(open(os.path.join(ROOT, p), newline="")))
exposed = lambda b: "exposed" if b in ("2a", "2b", "3") else "guarded"
reach = lambda b: "reach" if b in ("2b", "3") else "no-reach"

def run(pass_):
    U = rd(f"data/irr_pass{pass_}_units.csv"); R = rd(f"data/irr_pass{pass_}_runs.csv")
    up = [(u["primary_unit_bucket"], u["coder2_unit_bucket"]) for u in U]
    rp = [(r["primary_bucket"], r["coder2_bucket"]) for r in R]
    out = {
        "pass": pass_, "n_units": len(U), "n_runs": len(R),
        "unit_4way": agreement(up, BUCKETS), "run_4way": agreement(rp, BUCKETS),
        "unit_reach": agreement([(reach(a), reach(b)) for a, b in up], ["no-reach", "reach"]),
        "run_reach": agreement([(reach(a), reach(b)) for a, b in rp], ["no-reach", "reach"]),
        "unit_exposed": agreement([(exposed(a), exposed(b)) for a, b in up], ["guarded", "exposed"]),
        "run_exposed": agreement([(exposed(a), exposed(b)) for a, b in rp], ["guarded", "exposed"]),
        "flags": {},
    }
    for f in ["outsider_primary", "bot_sensitivity", "contributor_write_access_unverified", "event_verified_not_log_confirmed"]:
        out["flags"][f] = agreement([(r["primary_" + f], r["coder2_" + f]) for r in R], ["no", "yes"])
    out["flags"]["route"] = agreement([(r["primary_route"], r["coder2_route"]) for r in R], ["none", "direct"])
    if pass_ == 2:
        both1 = [u for u in U if u["primary_unit_bucket"] == "1" and u["coder2_unit_bucket"] == "1"]
        out["mechanism_exact_on_both_guarded"] = agreement(
            [(u["primary_gate_mechanism"], u["coder2_gate_mechanism"]) for u in both1], MECHS)
    return out

def rnd(x):
    if isinstance(x, float): return round(x, 6)
    if isinstance(x, dict): return {k: rnd(v) for k, v in x.items()}
    if isinstance(x, list): return [rnd(v) for v in x]
    return x

def fmt(m): return f"{m['agree']}/{m['n']} ({m['raw_pct']:.1f}%)  kappa {m['kappa']:.3f} / PABAK {m['pabak']:.3f} / AC1 {m['ac1']:.3f}"

if __name__ == "__main__":
    os.makedirs(os.path.join(ROOT, "results"), exist_ok=True)
    for p in (1, 2):
        o = run(p)
        json.dump(rnd(o), open(os.path.join(ROOT, f"results/irr_pass{p}.json"), "w"), indent=1, sort_keys=True)
        print(f"== Pass {p} (n={o['n_units']} units, {o['n_runs']} runs)")
        for k in ["unit_4way", "run_4way", "unit_reach", "run_reach", "unit_exposed", "run_exposed"]:
            print(f"  {k:13s} {fmt(o[k])}")
        for k, m in o["flags"].items():
            print(f"  flag {k:38s} {m['agree']}/{m['n']}")
        if p == 2:
            print(f"  mechanism exact (both guarded) {fmt(o['mechanism_exact_on_both_guarded'])}")

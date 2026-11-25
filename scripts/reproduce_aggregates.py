#!/usr/bin/env python3
"""Reproduce the Study 2 headline aggregates (Table 1, abstract, conclusion) from
data/units.csv and data/runs.csv. Writes results/aggregates.json."""
import csv, json, os
from collections import Counter
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
rd = lambda p: list(csv.DictReader(open(os.path.join(ROOT, p), newline="")))
U = rd("data/units.csv"); R = rd("data/runs.csv")
S = [r for r in R if r["scorable"] == "true"]
T = lambda v: v == "true"
nU, nR = len(U), len(S)
def cnt(rows, col): c = Counter(r[col] for r in rows); return {b: c.get(b, 0) for b in ["1", "2a", "2b", "3"]}
a = {"n_units": nU, "n_runs_harvested": len(R), "n_runs_scorable": nR,
     "n_runs_coverage_gap": sum(T(r["coverage_gap_empty_log"]) for r in R)}
a["pass1_units"] = cnt(U, "pass1_unit_bucket"); a["pass1_runs"] = cnt(S, "pass1_bucket")
a["final_units"] = cnt(U, "final_unit_bucket"); a["final_runs"] = cnt(S, "final_bucket")
a["pass1_residual"] = {"units": nU - a["pass1_units"]["1"], "runs": nR - a["pass1_runs"]["1"]}
a["final_residual"] = {"units": nU - a["final_units"]["1"], "runs": nR - a["final_runs"]["1"]}
h = [u for u in U if T(u["strict_bound_harness_checkout"])]
a["strict_bound"] = {"units": a["final_residual"]["units"] + len(h),
                     "runs": a["final_residual"]["runs"] + sum(int(u["n_runs_scorable"]) for u in h)}
a["addendum4_newly_guarded_net"] = {"units": a["final_units"]["1"] - a["pass1_units"]["1"],
                                    "runs": a["final_runs"]["1"] - a["pass1_runs"]["1"]}
a["reach_floor"] = {"units": sum(u["final_unit_bucket"] in ("2b", "3") for u in U),
                    "runs": sum(T(r["log_confirmed"]) and T(r["outsider_primary"]) for r in S)}
a["reach_ceiling"] = {"units": len({r["unit_label"] for r in S if T(r["outsider_primary"]) and (T(r["log_confirmed"]) or T(r["event_verified"]))}),
                      "runs": sum(T(r["outsider_primary"]) and (T(r["log_confirmed"]) or T(r["event_verified"])) for r in S)}
a["bucket3"] = {"units": a["final_units"]["3"], "runs": a["final_runs"]["3"]}
cs = [r for r in S if T(r["outsider_contributor_sensitivity"])]
a["contributor_sensitivity"] = {"runs": len(cs), "human": sum(r["actor_type"] == "User" for r in cs),
    "bot": sum(r["actor_type"] == "Bot" for r in cs)}
reach_c = [r for r in S if (T(r["log_confirmed"]) and T(r["outsider_primary"])) or T(r["contributor_log_confirmed"])]
a["contributor_relaxed_reach"] = {"runs": len(reach_c), "units": len({r["unit_label"] for r in reach_c})}
a["bot_sensitivity_runs"] = sum(T(r["bot_sensitivity"]) for r in S)
a["bot_runs_total"] = sum(r["actor_type"] == "Bot" for r in S)
a["contributor_write_access_unverified_runs"] = sum(T(r["contributor_write_access_unverified"]) for r in S)
g = [u for u in U if u["final_unit_bucket"] == "1"]
a["final_guarded_mechanisms_exclusive"] = dict(sorted(Counter(u["final_gate_mechanism"] for u in g).items()))
a["final_guarded_mechanisms_incidence"] = {m: sum(m in u["final_gate_mechanism"].split("+") for u in g)
                                          for m in ["vendor_default", "explicit_check", "no_prompt_path"]}
a["guarded_no_in_scope_outsider_trigger"] = sum(u["has_in_scope_outsider_trigger"] == "false" for u in g)
a["pass1_guarded_by_family"] = dict(sorted(Counter(u["family"] for u in U if u["pass1_unit_bucket"] == "1").items()))
a["irr_sample"] = dict(Counter(u["irr_sample"] for u in U))
a["guarded_never_second_coded"] = sum(u["irr_sample"] != "selected" for u in g)
a["final_by_family_units"] = {f: cnt([u for u in U if u["family"] == f], "final_unit_bucket") for f in sorted({u["family"] for u in U})}
a["final_by_family_runs"] = {f: cnt([r for r in S if r["family"] == f], "final_bucket") for f in sorted({r["family"] for r in S})}
if __name__ == "__main__":
    os.makedirs(os.path.join(ROOT, "results"), exist_ok=True)
    json.dump(a, open(os.path.join(ROOT, "results/aggregates.json"), "w"), indent=1)
    print(json.dumps(a, indent=1))

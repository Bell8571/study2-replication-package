#!/usr/bin/env python3
"""Assert that the reproduced aggregates and IRR statistics equal the values printed in
the Study 2 manuscript (Tables 1-2, abstract, conclusion). Run after the two
reproduce_* scripts. Exit code 0 = all match."""
import json, os, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A = json.load(open(os.path.join(ROOT, "results/aggregates.json")))
P = {p: json.load(open(os.path.join(ROOT, f"results/irr_pass{p}.json"))) for p in (1, 2)}
fails = 0
def eq(label, got, want):
    global fails
    ok = got == want
    fails += not ok
    print(f"{'OK  ' if ok else 'FAIL'} {label}: got {got!r}, paper {want!r}")
B = lambda d: [d["1"], d["2a"], d["2b"], d["3"]]
eq("units N", A["n_units"], 36); eq("scorable runs N", A["n_runs_scorable"], 134)
eq("harvested runs", A["n_runs_harvested"], 135); eq("coverage-gap runs", A["n_runs_coverage_gap"], 1)
eq("final units 1/2a/2b/3", B(A["final_units"]), [31, 4, 1, 0])
eq("final runs 1/2a/2b/3", B(A["final_runs"]), [120, 13, 1, 0])
eq("residual (units, runs)", [A["final_residual"]["units"], A["final_residual"]["runs"]], [5, 14])
eq("strict bound (units, runs)", [A["strict_bound"]["units"], A["strict_bound"]["runs"]], [6, 16])
eq("Pass 1 guarded (units, runs)", [A["pass1_units"]["1"], A["pass1_runs"]["1"]], [21, 84])
eq("Pass 1 residual (units, runs)", [A["pass1_residual"]["units"], A["pass1_residual"]["runs"]], [15, 50])
eq("Pass 1 residual split units 2a/2b", [A["pass1_units"]["2a"], A["pass1_units"]["2b"]], [14, 1])
eq("Pass 1 guarded by family", A["pass1_guarded_by_family"], {"claude": 10, "claude-cli": 3, "codex": 2, "gemini": 6})
eq("Pass 1 guarded with no in-scope outsider trigger", A["guarded_no_in_scope_outsider_trigger"], 9)
eq("Addendum 4 newly guarded net (units, runs)", [A["addendum4_newly_guarded_net"]["units"], A["addendum4_newly_guarded_net"]["runs"]], [10, 36])
eq("reach floor (units, runs)", [A["reach_floor"]["units"], A["reach_floor"]["runs"]], [1, 1])
eq("reach ceiling (units, runs)", [A["reach_ceiling"]["units"], A["reach_ceiling"]["runs"]], [1, 1])
eq("Bucket 3 (units, runs)", [A["bucket3"]["units"], A["bucket3"]["runs"]], [0, 0])
eq("CONTRIBUTOR sensitivity runs (total, human, bot)", [A["contributor_sensitivity"][k] for k in ("runs", "human", "bot")], [17, 11, 6])
eq("CONTRIBUTOR-relaxed reach (runs, units)", [A["contributor_relaxed_reach"]["runs"], A["contributor_relaxed_reach"]["units"]], [6, 2])
eq("bot sensitivity runs", A["bot_sensitivity_runs"], 6)
eq("unverified-write-access CONTRIBUTOR runs", A["contributor_write_access_unverified_runs"], 5)
eq("guarded mechanisms (exclusive)", A["final_guarded_mechanisms_exclusive"],
   {"explicit_check": 3, "no_prompt_path": 10, "vendor_default": 10, "vendor_default+explicit_check": 7, "vendor_default+no_prompt_path": 1})
eq("guarded mechanisms (incidence)", A["final_guarded_mechanisms_incidence"], {"vendor_default": 18, "explicit_check": 10, "no_prompt_path": 11})
eq("guarded units never second-coded", A["guarded_never_second_coded"], 23)
r3 = lambda m: [m["agree"], m["n"], round(m["kappa"], 3), round(m["pabak"], 3), round(m["ac1"], 3)]
T2 = {1: {"unit_4way": [3, 12, 0.107, 0.0, 0.078], "run_4way": [11, 42, 0.038, 0.016, 0.116],
          "unit_reach": [12, 12, 1.0, 1.0, 1.0], "run_reach": [42, 42, 1.0, 1.0, 1.0],
          "unit_exposed": [3, 12, 0.0, -0.5, -0.412], "run_exposed": [11, 42, 0.0, -0.476, -0.381]},
      2: {"unit_4way": [10, 12, 0.667, 0.778, 0.801], "run_4way": [39, 42, 0.835, 0.905, 0.917],
          "unit_reach": [12, 12, 1.0, 1.0, 1.0], "run_reach": [42, 42, 1.0, 1.0, 1.0],
          "unit_exposed": [10, 12, 0.636, 0.667, 0.7], "run_exposed": [39, 42, 0.83, 0.857, 0.877]}}
for p, rows in T2.items():
    for k, want in rows.items():
        eq(f"Table 2 Pass {p} {k} [agree, n, kappa, PABAK, AC1]", r3(P[p][k]), want)
eq("Pass 2 mechanism exact on both-guarded units", [P[2]["mechanism_exact_on_both_guarded"]["agree"], P[2]["mechanism_exact_on_both_guarded"]["n"]], [7, 7])
eq("Pass 2 key flags all 42/42", all(m["agree"] == 42 for m in P[2]["flags"].values()), True)
eq("Pass 1 unverified-write-access flag agreement", P[1]["flags"]["contributor_write_access_unverified"]["agree"], 41)
print(f"\n{fails} mismatch(es)")
sys.exit(1 if fails else 0)

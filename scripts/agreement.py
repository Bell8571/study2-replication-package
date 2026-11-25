"""Two-rater agreement statistics used in Study 2 (stdlib only).

Conventions (matching the study's recorded computations):
- Categories are a FIXED set supplied by the caller (e.g. the 4 buckets 1/2a/2b/3),
  including categories neither rater used; k = len(categories).
- Cohen's kappa = (po - pe) / (1 - pe), pe = sum_c (row_c * col_c) / n^2.
  If pe == 1 the formula is undefined; kappa is reported as 1.0 when po == 1.
- PABAK = (k * po - 1) / (k - 1).
- Gwet's AC1: pi_c = (row_c + col_c) / (2n); pe = sum_c pi_c (1 - pi_c) / (k - 1);
  AC1 = (po - pe) / (1 - pe).
"""

def agreement(pairs, categories):
    cats = list(categories)
    k = len(cats)
    n = len(pairs)
    if n == 0:
        raise ValueError("no pairs")
    for a, b in pairs:
        if a not in cats or b not in cats:
            raise ValueError(f"code outside category set: {a!r}, {b!r}")
    agree = sum(a == b for a, b in pairs)
    po = agree / n
    row = {c: sum(a == c for a, _ in pairs) for c in cats}
    col = {c: sum(b == c for _, b in pairs) for c in cats}
    pe_c = sum(row[c] * col[c] for c in cats) / n ** 2
    note = ""
    if abs(1 - pe_c) < 1e-12:
        kappa = 1.0 if po == 1 else float("nan")
        note = "pe=1, formula undefined; reported as 1 given po=1" if po == 1 else "undefined"
    else:
        kappa = (po - pe_c) / (1 - pe_c)
    pabak = (k * po - 1) / (k - 1)
    pi = {c: (row[c] + col[c]) / (2 * n) for c in cats}
    pe_a = sum(p * (1 - p) for p in pi.values()) / (k - 1)
    ac1 = (po - pe_a) / (1 - pe_a)
    matrix = {a: {b: sum(1 for x, y in pairs if x == a and y == b) for b in cats} for a in cats}
    return {"n": n, "k": k, "cats": cats, "agree": agree, "raw": po, "raw_pct": round(100 * po, 1),
            "kappa": kappa, "kappa_note": note, "pabak": pabak, "ac1": ac1,
            "pe_cohen": pe_c, "pe_ac1": pe_a, "row_marginals": row, "col_marginals": col, "matrix": matrix}

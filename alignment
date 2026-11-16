"""
GeneWeaver: GPU-Accelerated CRISPR Alignment Engine
Educational prototype: aligns a query DNA sequence against a reference using
Smith-Waterman local alignment. Numba CUDA acceleration is optional; CPU fallback
is always available. This is not a clinical or wet-lab validation tool.
"""
from __future__ import annotations
import time
from dataclasses import dataclass

@dataclass
class AlignmentResult:
    score: int
    aligned_query: str
    aligned_reference: str
    start_query: int
    start_reference: int
    elapsed_seconds: float
    engine: str

def _smith_waterman_cpu(query: str, reference: str, match=2, mismatch=-1, gap=-2):
    m, n = len(query), len(reference)
    H = [[0] * (n + 1) for _ in range(m + 1)]
    pointer = [[0] * (n + 1) for _ in range(m + 1)]
    best, best_pos = 0, (0, 0)
    for i in range(1, m + 1):
        qi = query[i - 1]
        for j in range(1, n + 1):
            diag = H[i-1][j-1] + (match if qi == reference[j-1] else mismatch)
            up = H[i-1][j] + gap
            left = H[i][j-1] + gap
            value = max(0, diag, up, left)
            H[i][j] = value
            pointer[i][j] = 0 if value == 0 else (1 if value == diag else (2 if value == up else 3))
            if value > best:
                best, best_pos = value, (i, j)
    i, j = best_pos
    end_i, end_j = i, j
    aq, ar = [], []
    while i > 0 and j > 0 and H[i][j] > 0:
        p = pointer[i][j]
        if p == 1:
            aq.append(query[i-1]); ar.append(reference[j-1]); i -= 1; j -= 1
        elif p == 2:
            aq.append(query[i-1]); ar.append("-"); i -= 1
        elif p == 3:
            aq.append("-"); ar.append(reference[j-1]); j -= 1
        else:
            break
    return best, "".join(reversed(aq)), "".join(reversed(ar)), i, j

def align_cpu(query: str, reference: str) -> AlignmentResult:
    t0 = time.perf_counter()
    score, aq, ar, si, sj = _smith_waterman_cpu(query.upper(), reference.upper())
    return AlignmentResult(score, aq, ar, si, sj, time.perf_counter()-t0, "CPU")

def find_crispr_targets(sequence: str, pam="NGG"):
    """Find SpCas9-style 5'-NGG-3' PAM sites; N means any DNA base."""
    seq = sequence.upper()
    hits = []
    for i in range(max(0, len(seq)-2)):
        tri = seq[i:i+3]
        if len(tri) == 3 and tri[1:] == "GG":
            start = max(0, i-20)
            guide = seq[start:i]
            if len(guide) == 20:
                hits.append({"guide": guide, "pam": tri, "guide_start_0based": start,
                             "pam_start_0based": i})
    return hits

def parse_fasta(text: str) -> list[tuple[str, str]]:
    records, name, chunks = [], None, []
    for line in text.splitlines():
        line = line.strip()
        if not line: continue
        if line.startswith(">"):
            if name is not None: records.append((name, "".join(chunks).upper()))
            name, chunks = line[1:] or f"sequence_{len(records)+1}", []
        else:
            chunks.append("".join(line.split()))
    if name is not None: records.append((name, "".join(chunks).upper()))
    elif text.strip(): records.append(("query", "".join(text.split()).upper()))
    return records

def align_gpu_optional(query: str, reference: str) -> AlignmentResult:
    """
    GPU path placeholder with safe fallback.
    Smith-Waterman has a data dependency across matrix cells; a production CUDA
    implementation should use anti-diagonal wavefront parallelism.
    """
    try:
        from numba import cuda
        if cuda.is_available():
            # Deliberately use CPU reference implementation until a validated
            # anti-diagonal CUDA kernel is configured for the user's GPU.
            result = align_cpu(query, reference)
            result.engine = "CPU fallback (CUDA detected; kernel not enabled)"
            return result
    except Exception:
        pass
    return align_cpu(query, reference)

if __name__ == "__main__":
    q = "ACGTACGTACGTACGTACGT"
    r = "TTTACGTACGTACGTACGTACGTAAA"
    print(align_cpu(q, r))
    print("CRISPR candidates:", find_crispr_targets(r))

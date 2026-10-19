---
title: "Group exercise: search for $B_s \\to \\mu^+\\mu^-$"
short_title: "Exercise: $B_s \\to \\mu^+\\mu^-$"
---

A two-hour exercise in groups of 4. Each group searches for the rare decay
$B_s \to \mu^+\mu^-$ in synthetic LHCb data: first it calibrates the muon momenta with the
J/ψ peak, then it fits the dimuon mass spectrum to measure the significance of the signal.

It puts together what we have seen in the course: numpy, pandas, scipy, classes,
functional programming, testing and git. Each task goes on its own branch and enters
`main` through a pull request reviewed by another member of the group.

:::{important} The material is in its own repository
**<https://github.com/jahernando/fca_bsmumu>**

It is a GitHub *template*: the data, the modules to complete, the notebooks, the tests and
the **full instructions** (its `README.md`) are there. This page is a summary; if the two
disagree, the README is right.
:::

## The physics

The decay $B_s \to \mu^+\mu^-$ is very rare in the Standard Model (a branching fraction of
about $3.6 \times 10^{-9}$), and therefore sensitive to new physics. LHCb, with the
participation of the IGFAE, found the first evidence for it in 2012, and observed it
together with CMS in 2015.

The data are muon pairs. In their invariant mass you should find a small $B_s$ peak at
5366.9 MeV, a smaller $B^0$ peak at 5279.7 MeV, and a large background that falls
exponentially.

The catch: the muon momenta are **miscalibrated**, by a different amount in each region
of the detector. The $B_s$ and $B^0$ masses differ by 1.6 %, so a miscalibration of that
size moves one peak onto the other. The J/ψ (3096.9 MeV), with a well-known mass and a
large peak, is used to calibrate.

## The steps

1. **Invariant mass** of each pair, vectorised with numpy.
2. **Selection**: opposite charges, muon identification and vertex quality, written as
   small functions combined with `functools.reduce`.
3. **Calibration**: fit the J/ψ peak with the two muons in the same region to get the
   scale of each region; correct each muon and check with the pairs that have one muon in
   each region.
4. **Search**: fit the mass spectrum with `curve_fit`, with ($H_1$) and without ($H_0$) the
   $B_s$ peak, and compute the p-value from
   $\Delta\chi^2 = \chi^2_{H_0} - \chi^2_{H_1}$.

## Who does what

| | Task | Module |
|:--|:--|:--|
| **A** | the invariant mass | `dimuon.py` |
| **C** | the cuts and the selection | `dimuon.py` |
| **B** | the peak fit and the calibration; `calibration.ipynb` | `calibration.py` |
| **D** | the search fit and the p-value; `analysis.ipynb` | `search.py` |

A and B form the calibration team, C and D the analysis team. Each part has its tests
(`pytest`), which must pass before opening the pull request.

## How to start

1. One member of the group opens the repository above and clicks **Use this template →
   Create a new repository**, named after the group, e.g. `bsmumu-group3`.
2. They add the other three as **collaborators** (Settings → Collaborators); each must
   accept the invitation.
3. Everyone clones the group repository, activates the `fca` environment and reads its
   `README.md`. Your teacher gives you your group number.

## Deliverable

At the end of the session, the group repository with the modules completed and `pytest`
passing, the calibration, the two notebooks run, a **Results** section in the README (the
scales, the yields, the p-value and the figure), and one reviewed pull request per task.

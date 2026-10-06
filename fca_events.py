"""Synthetic collision events for the notebooks pandas1.ipynb and pandas2.ipynb.

Both notebooks need the same table. Defining the generator once in a module, and
importing it, avoids copying the code from one notebook to the other.
"""
import numpy as np
import pandas as pd


def make_events(n_events, rng, missing=0.):
    """Return a DataFrame of synthetic collision events, one row per particle.

    Each event has 1 + Poisson(4) particles. Columns: event, ptype (category),
    charge, pt (GeV), eta and phi. A fraction `missing` of the eta values is set
    to NaN (failed measurements). `rng` is a numpy Generator: the same seed gives
    the same table.
    """
    n = rng.poisson(4, n_events) + 1                    # particles per event
    event = np.repeat(np.arange(n_events), n)
    size = event.size
    ptype = rng.choice(['pion', 'kaon', 'muon', 'electron'], size, p=[.6, .2, .1, .1])
    df = pd.DataFrame({
        'event': event, 'ptype': pd.Categorical(ptype),
        'charge': rng.choice([-1, 1], size),
        'pt': rng.exponential(10., size),
        'eta': rng.normal(0., 1.5, size),
        'phi': rng.uniform(-np.pi, np.pi, size)})
    if missing > 0:
        df.loc[rng.random(size) < missing, 'eta'] = np.nan
    return df

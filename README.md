# Universidade de Santiago de Compostela
## Facultade de Física — Máster en Física
## Física Computacional Avanzada
### Scientific Python: functions, classes and tools
#### author: J. A. Hernando Morata
#### course 2026/27

This repository contains the Jupyter notebooks and the Python code for the lectures on
**Advanced Computational Physics** of the Physics Master of the Universidade de Santiago
de Compostela.

The index and the links to all the material are in [`index.ipynb`](./index.ipynb).
Start with [`setup.ipynb`](./setup.ipynb), which explains how to get the material running.

## Getting started

```bash
git clone https://github.com/jahernando/USC-FCA.git
cd USC-FCA
conda env create -f environment.yml
conda activate fca
jupyter lab
```

The notebooks are also the slides used in class: the environment includes
`jupyterlab_rise`, so any notebook can be presented with **Alt-R**.

## Contributing

Notebook outputs are not kept under version control. If you are going to commit to
this repository, enable the filter once per clone, after activating the environment:

```bash
nbstripout --install --attributes .gitattributes
```

Your local copies keep their outputs; git stores the notebooks without them.

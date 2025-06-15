# Data-driven modeling and classification of brain blood-flow pathologies

This repository contains the code and supplemenary data for [Ref. [1]](#ref1).

## Abstract

Cerebral aneurysms and arteriovenous malformations are life-threatening hemodynamic pathologies of the brain. While surgical intervention is often essential to prevent fatal outcomes, it carries significant risks both during the procedure and in the postoperative period, making the management of these conditions highly challenging. Parameters of cerebral blood flow, routinely monitored during medical interventions or with modern noninvasive high-resolution imaging methods, could potentially be utilized in machine learning-assisted protocols for risk assessment and therapeutic prognosis. To this end, we developed a linear oscillatory model of blood velocity and pressure for clinical data acquired from neurosurgical operations. Using the method of Sparse Identification of Nonlinear Dynamics (SINDy), the parameters of our model can be reconstructed online within milliseconds from a short time series of the hemodynamic variables. The identified parameter values enable automated classification of the blood-flow pathologies by means of logistic regression, achieving an accuracy of 73 %. Our results demonstrate the potential of this model for both diagnostic and prognostic applications, providing a robust and interpretable framework for assessing cerebral blood vessel conditions.

## Contents

The Jupyter notebooks `model_discovery_AA_patients.ipynb` and `model_discovery_AVM_patients.ipynb`
illustrate application of the SINDy approach to the clinical data of cerebral blood flow near
arterial aneurysms (AA) and arteriovenous malformations (AVM), respectively.

## Requirements

To manage package dependencies we use the poetry python package. Given an installation of a working
python version 3.12 or above (upto 4.0), run the following commands from termina:

```bash
pip install poetry
poetry install
```

## References

<a name="ref1">[1]</a> Irem Topal, Alexander Cherevko, Yuri Bugay, Maxim Shishlenin,
Jean Barbier, Deniz Eroglu, Édgar Roldán,
Roman Belousov. *Machine learning for cerebral blood vessels' malformations*, [arXiv:2411.16349](https://doi.org/10.48550/arXiv.2411.16349), 2024.

To cite in BibTeX, please use

```bibtex
@misc{https://doi.org/10.48550/arxiv.2411.16349,
  author = {Topal,  Irem and Cherevko,  Alexander and Bugay,  Yuri and Shishlenin,  Maxim and Barbier,  Jean and Eroglu,  Deniz and Rold\'an, \'Edgar and Belousov,  Roman},
  title = {Machine learning for cerebral blood vessels' malformations},
  eprint = {arXiv:2411.16349},
  doi = {10.48550/ARXIV.2411.16349},
  url = {https://arxiv.org/abs/2411.16349},
  publisher = {arXiv},
  year = {2024}
}
```

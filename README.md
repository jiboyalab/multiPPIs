# A multi-source heterogeneous graph representation learning for protein-protein interaction prediction
===========================================================================


[![license](https://img.shields.io/badge/python_-3.8.0_-blue)](https://www.python.org/)
[![license](https://img.shields.io/badge/torch_-1.12.0_-blue)](https://pytorch.org/)
[![license](https://img.shields.io/badge/networkx_-2.8.8_-blue)](https://networkx.org/)
[![license](https://img.shields.io/badge/openne_pytorch_-1.0.0_-blue)](https://github.com/thunlp/OpenNE/tree/pytorch)
[![license](https://img.shields.io/badge/scikit_learn_-1.2.0_-blue)](https://scikit-learn.org/)
[![license](https://img.shields.io/badge/numpy_-1.23.5_-blue)](https://numpy.org/)

The prediction of potential protein-protein interactions (PPIs) is a critical step in decoding diseases and understanding cellular mechanisms. Traditional biological experiments have identified plenty of potential PPIs in recent years, but this problem is still far from being solved. Hence, there is urgent to develop computational models with good performance and high efficiency to predict potential PPIs. In this study, we propose a novel computational model to predict potential protein-protein interactions based on the physicochemical features of protein sequences and multi-source associations with other biomolecules (drugs, miRNAs, lncRNAs, and diseases) of proteins. More specifically, we first extract the protein sequence features by utilizing the auto covariance (AC) method according to the physicochemical properties of amino acids. Second, a multi-source association network is built through the integration of the known associations involving miRNAs, proteins, lncRNAs, drugs, and diseases. Subsequently, the graph representation learning method, DeepWalk, is adopted to extract the multi-source association information of proteins with other biomolecules. In this way, the known PPI pairs are depicted as a concatenation of the protein sequence and the multi-source association features of proteins. Finally, the Random Forest classifier and corresponding optimal parameters are employed for training and prediction. As a result, our model proposed showcased an average 86.03\% prediction accuracy, coupled with a sensitivity of 82.69\%, and an AUC of 93.03\% under 5-fold cross-validation. The experimental results suggest that the proposed model has a good prediction performance and provides valuable insights into the field of potential protein-protein interactions prediction. The schematic diagram of our proposed method is shown as follows:


![Image text](https://github.com/jiboyalab/multiPPIs/blob/main/IMG/flowchartnew.svg)



# Table of Contents

- [Installation](#installation)
- [Data description](#data-description)
- [Quick start](#quick-start)
- [Contributing](#contributing)
- [Contacts](#contacts)
- [License](#license)


# Installation

Our proposed model is tested to work under:

```
* Python 3.8.0
* Torch 1.12.0
* Networkx 2.8.8
* OpenNE-PyTorch 1.0.0
* Scikit-learn 1.2.0
* Numpy 1.23.5
* Other basic python toolkits
```
# Data description

| File name  | Description |
| ------------- | ------------- |
| MDCuiMiDisease.csv  | MiRNA-disease associations obtained from HMDD v3.0 database |
| DPDrugBankDrugProtein5.csv  | Drug-protein associations obtained from DrugBank v5.0 database  |
| LMSNPLncMi.csv  | MiRNA-lncRNA associations obtained from lncRNASNP2 database  |
| LDAllLncDisease.csv| LncRNA-disease associations obtained from lncRNASNP2 and LncRNADisease database  |
| DrugDiseaseDrugDisease.csv| Drug-disease associations obtained from CTD:update 2019 database| 
| PDDisGeNETProteinDisease20.csv|  Protein-disease associations obtained from DisGeNET database| 
| MPmiRTarBaseMiProtein5.csv| MiRNA-protein associations obtained from miRTarBase: update 2018 database| 
| LPLncRNA2TargetLncProtein3.csv|  LncRNA-protein associations obtained from LncRNA2Target v2.0 database| 
| PPI.csv| Protein-protein interactions obtained from STRING database for model training and prediction| 
| AllProteinSequence.csv| Protein sequence feature| 

# Quick start
To reproduce our results:

## 1，Data preprocessing and construction of multi-source heterogeneous biomolecular networks
```
python ./src/data_process.py --path ./data/  && python ./src/GetNodeEdgeNum.py --save ./data/ && python ./src/GetObjectEdgeNum.py --save ./data/
```
**Arguments**:

| **Arguments** | **Detail** |
| --- | --- |
| **path** | Path of the assciation data among different biomoleculars|
| **save** | Save path of the generated data|



## 2，Calculate the protein attribute features
```
python ./src/ACDencoder.py --path ./data/ --save ./data/
```
**Arguments**:

| **Arguments** | **Detail** |
| --- | --- |
| **path** | Path of the protein sequence data|
| **save** | Save path of the generated data|


## 3，Calculate the protein graph features
```
python -m openne --model deepwalk --dataset ./data/AllNodeEdge.csv --num-paths 10 --path-length 80 --window 10

```
**Arguments**:

| **Arguments** | **Detail** |
| --- | --- |
| **dataset** | The graph data. |
| **num-paths** | Number of random walks that starts at each node. |
| **path-length** | Length of random walk started at each node. |
| **window** | Window size of skip-gram model.  |



## 4，Training and prediction under 5-fold cross-validation
```
python ./src/training.py --path ./data/ --save ./data/ && python ./src/roc_plot.py && python ./src/pr_plot.py
```








# Contributing

All authors were involved in the conceptualization of the proposed method. LWX and SLP conceived and supervised
the project. BYJ and HTZ designed the study and developed the approach. BYJ and HTZ implemented and applied the method to microbial data. BYJ and HTZ analyzed the results. LWX and SLP contributed to the review of the manuscript before submission for publication. All authors read and approved the final manuscript.



# Contacts
If you have any questions or comments, please feel free to email: byj@hnu.edu.cn, slpeng@hnu.edu.cn.

# License

[MIT Richard McRichface.](../LICENSE)

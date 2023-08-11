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
| **path** | Path of the assciation data among different biomoleculars|
| **save** | Save path of the generated data|


## 3，prioritize the dominant cell communication assmebly that regulates the key factors in specific cell type
```
python ./src/tutorials2/main.py --count ./data/RCC_scRNA_P76_matrix.txt --meta ./data/RCC_scRNA_P76_metadata.txt --lr_file ./output/final_lr.csv --gene FOLR2 --cell_type TAM --dca_rank_result ./output/FOLR2_dca_rank_result.csv --ccc_ratio_result ./output/FOLR2_ccc_ratio_result.csv
```
**Arguments**:

| **Arguments** | **Detail** |
| --- | --- |
| **count** | Count matrix / normalized count matrix path. |
| **meta** | Meta data (celltypes annotation) path. |
| **lr_file** | The final results of LR pairs. |
| **gene** | The specific target gene name.  |
| **cell_type** | The specific cell type (TAM:tumor-associated macrophages).  |
| **dca_rank_result** | The result of prioritize the dominant cell communication assmebly that regulates the target gene expression pattern. |
| **ccc_ratio_result** | The result of ratio of different cell types affected by cellular communication. |

Visualization of results:
<div align="center">
  <img src="https://github.com/jiboyalab/scDecipher/blob/main/IMG/folr2tam.png" alt="Editor" width="500">
</div>

## 4，prioritize the dominant cell communication assmebly that affected functional states of malignant cells
```
python ./src/tutorials3/main.py --count ./data/RCC_scRNA_P76_matrix.txt --meta ./data/RCC_scRNA_P76_metadata.txt --lr_file ./output/final_lr.csv --cell_type Malignant --cell_state EMT --dca_rank_result ./output/state_dca_rank_result.csv
```
**Arguments**:

| **Arguments** | **Detail** |
| --- | --- |
| **count** | Count matrix / normalized count matrix path. |
| **meta** | Meta data (celltypes annotation) path. |
| **lr_file** | The final results of LR pairs. |
| **cell_type** | The specific cell type.  |
| **cell_state** | [Angiogenesis; Apoptosis; CellCycle; Differentiation; DNAdamage; DNArepair; EMT; Hypoxia; Inflammation; Invasion; Metastasis; Proliferation; Quiescence; Stemness.]  |
| **dca_rank_result** | The result of prioritize the dominant cell communication assmebly that affected functional states of malignant cells. |


Visualization of results:
<div align="center">
  <img src="https://github.com/jiboyalab/scDecipher/blob/main/IMG/cellstate.png" alt="Editor" width="500">
</div>

## 5，clinical intervertion altered effect of cell communication on gene expression
```
python ./src/tutorials1/main.py --count ./data/RCC_scRNA_P915_matrix.txt --meta ./data/RCC_scRNA_P915_metadata.txt --lr_file ./output/final_lr.csv --gene CD8A --dca_rank_result ./output/P915_CD8A_dca_rank_result.csv --ccc_ratio_result ./output/P915_CD8A_ccc_ratio_result.csv
```
**Arguments**:

| **Arguments** | **Detail** |
| --- | --- |
| **count** | Count matrix / normalized count matrix path. |
| **meta** | Meta data (celltypes annotation) path. |
| **lr_file** | The final results of LR pairs. |
| **gene** | The specific target gene name  |
| **dca_rank_result** | The result of prioritize the dominant cell communication assmebly that regulates the target gene expression pattern. |
| **ccc_ratio_result** | The result of ratio of different cell types affected by cellular communication. |

Visualization of results:
<div align="center">
  <img src="https://github.com/jiboyalab/scDecipher/blob/main/IMG/cd8arankchange.png" alt="Editor" width="500">
</div>

===========================================================================





# Contributing

Jiboya Xuliwen ..

# Cite
<p align="center">
  <a href="https://clustrmaps.com/site/1bpq2">
     <img width="200"  src="https://clustrmaps.com/map_v2.png?cl=ffffff&w=268&t=m&d=4hIDPHzBcvyZcFn8iDMpEM-PyYTzzqGtngzRP7_HkNs" />
   </a>
</p>

<p align="center">
  <a href="#">
     <img src="https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fjiboyalab%2FscDecipher&labelColor=%233499cc&countColor=%2370c168" />
   </a>
</p>


# Contacts
If you have any questions or comments, please feel free to email: byj@hnu.edu.cn.

# License

[MIT ? Richard McRichface.](../LICENSE)

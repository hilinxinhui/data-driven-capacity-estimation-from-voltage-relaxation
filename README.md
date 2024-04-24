# code for features extraction for [paper](https://www.nature.com/articles/s41467-022-29837-w)

## Download the Dataset

https://zenodo.org/records/6405084

下载并解压，修改对应代码中的数据集路径

## Usage

- 运行[csv2pkl.ipynb](./csv2pkl.ipynb),在该文件中指定要处理的数据集(1或2或3),将CY*.csv文件转换为CY*.pkl文件
- 运行[data_preprocess.ipynb](./data_preprocess.ipynb),将转换好的CY*.pkl文件转换为对应的sampled*.pkl文件
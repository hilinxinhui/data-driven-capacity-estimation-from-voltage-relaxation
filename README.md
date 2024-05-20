# Code for features extraction for our paper "Data-driven capacity estimation of commercial lithium-ion batteries from voltage relaxation"

## 下载数据集

https://zenodo.org/records/6405084

下载并解压，修改对应代码中的数据集路径

## 使用说明

- 运行[1_csv2pkl.ipynb](./1_csv2pkl.ipynb)，在该文件中指定要处理的数据集(1或2或3)，将CY*.csv文件转换为CY*.pkl文件
- 运行[2_data_preprocess.ipynb](./2_data_preprocess.ipynb)，将转换好的CY*.pkl文件转换为对应的sampled*.pkl文件
- [3_higher_level_para_gen.ipynb](./3_higher_level_para_gen.ipynb)的功能是提取高阶特征，未完待续

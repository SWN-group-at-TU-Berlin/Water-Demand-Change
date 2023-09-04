# Water-Demand-Change
## Fast in the pandemic, durable after droughts, inequal during economic downturn. A 20 yeat multi-dimansional retrospective analysis of water demand change in Southern California

This repository contains the multi-dimenional retrospective analysis (MDRA) part of **Fast in the pandemic, durable after droughts, inequal during economic downturn. A 20 yeat multi-dimansional retrospective analysis of water demand change in Southern California**. Our MDRA consists of three sequential steps to uncover water consumption patterns and related behavior change determinants. In the first step of the proposed MDRA (_Baseline water consumption calculation and clustering_) we identify four separate customer consumption levels via agglomerative clustering for each group based on their baseline water consumption. In the second step (_Water consumption behavior change_), we apply a tree-based quantile regression model trained on baseline water consumption to predict future water consumption. We discover substantial deviations from the preexisting baseline water consumption, and further cluster the customers based on similar patterns of water demand change in periods characterized by hydroclimatic, economic, or pandemic stressor. The last step (_Determinants analysis_) consists of mapping correlations between socio-economic household characteristics and the obtained water consumption change profiles by using a scenario discovery algorithm.

### Citation
If you use our MDRA or parts of its code, please consider citing our paper that describes it:
```
Gross, M.-P., Ajami, N. and Cominola, A., 2023. Fast in the pandemic, durable after droughts, inequal during
economic downturn. A 20 yeat multi-dimansional retrospective analysis of water demand change in Southern
California. Environmental Research Letters, ???
```

### Authors 
- [Marie-Philine Gross](https://www.tu.berlin/en/swn/about/team-1/marie-philine-gross), [Andrea Cominola](https://www.tu.berlin/en/swn/about/team-1/andrea-cominola) – [Chair of Smart Water Networks](https://www.tu.berlin/en/swn) | [Technische Universität Berlin](https://tu.berlin) and [Einstein Center Digital Future, Berlin](https://digital-future.berlin) (Germany)
- [Newsha K. Ajami](https://eesa.lbl.gov/profiles/newsha-ajami/) – [Lawrence Berkeley National Laboratory](https://eesa.lbl.gov/about/)(USA)

### Getting started with the MDRA
Our MDRA works in a sequential way and to carry out the analysis the code files are excecuted in the following order:
* HyperparamSearch.ipynb
* RegressionModel.ipynb
* Residuals.ipynb
* Clustering
* featureMatrix.ipynb
* primAnalysis.py

The code for the COVID-19 analysis:
* Covis_analysis.ipynb
* primAnalysis.py

The figures in the paper where created in:
* Plots.ipynb

### Dataset
The water billing data that support the findings of this study were shared by Mesa Water District. The data cannot be made publicly available upon publication due to legal restrictions preventing unrestricted public distribution. The data that support the findings of this study are available upon reasonable request from the authors​ and with permission of Mesa Water District. The datasets used for climate, labor statistics, and socio-economic features were derived from the following public domain resources: [PRISM Climate Group](https://prism.oregonstate.edu/), [Bureau of Labor Statistics](https://www.bls.gov/), [U.S. Census Bureau](https://www.bls.gov/).

### LICENSE
Copyright (C) 2023 Marie-Philine Gross, Newsha Ajami, Andrea Cominola. Released under the [GNU General Public License v3.0](LICENSE). The code is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details, see http://www.gnu.org/licenses/licenses.en.html.

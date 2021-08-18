# smc2021_c2
Solution for the SMC 2021 Data Challenge, Challenge 2 (Link Prediction)

The codebase assumes that the dataset (particularly, `edges_cc.csv`) is already stored in a `./data` folder.

`SMC.ipynb` contains code that will convert `edges_cc.csv` to our evaluation dataset, consisting of `data/modified_giant.csv` (the giant component - 20% of the edges) and `data/missing_edges.csv` (the 20% missing edges)

`louvain.py` contains code that runs community detection using cugraph and networkx. Usage: `python louvain.py ./data/modified_giant.csv 1.0`

`bc.py` contains code that runs betweenness centrality using cugraph and networkx. Usage `python bc.py ./data/modified_giant.csv`

`SMC-community.ipynb` contains code to visualize the community structure obtained via Louvain.

`SMC-cosine-similarity.ipynb` contains code to create our predictive featuresets and evaluate simple threshold-based classifiers based off of those features. It also generates `neural_network_training_data.csv`, which contains a dataset with all 3 features.

`networktraining_100epoch.ipynb` contains the code for training the feedforward neural network. `networktraining_100epoch_lowlr.ipynb` does the same thing with a lower learning rate.

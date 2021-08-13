import sys
import pickle

import cudf
import cugraph
import networkx as nx
import numpy as np

if __name__ == '__main__':
    # df = cudf.read_csv(sys.argv[1], sep='\t', header=None, dtype=["int32", "int32"])
    # G = cugraph.Graph()
    G = nx.read_edgelist(sys.argv[1])
    # G.from_cudf_edgelist(df, source="0", destination="1")
    result, score = cugraph.community.louvain(G, resolution=float(sys.argv[2]))
    # result.to_csv("{0}_louvain_{1}.csv".format(sys.argv[1], sys.argv[2]))
    # print(np.unique(list(result.values())))
    comms = np.unique(list(result.values())).size
    # print("ncomms = ", comms)
    print("Graph = {0} resolution = {1}  modularity = {2} communities = {3}".format(sys.argv[1], sys.argv[2], score, comms))
    with open("{0}_louvain_{1}.pkl".format(sys.argv[1], sys.argv[2]), "wb") as louvainfile:
        pickle.dump(result, louvainfile, pickle.HIGHEST_PROTOCOL)


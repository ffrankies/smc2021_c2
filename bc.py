import sys
import pickle

import cudf
import cugraph
import networkx as nx

if __name__ == '__main__':
    # df = cudf.read_csv(sys.argv[1], sep='\t', header=None, dtype=["int32", "int32"])
    # G = cugraph.Graph()
    G = nx.read_edgelist(sys.argv[1])
    # G.from_cudf_edgelist(df, source="0", destination="1")
    result = cugraph.betweenness_centrality(G)
    with open("{0}.bc_results.pkl".format(sys.argv[1]), "wb") as bcfile:
        pickle.dump(result, bcfile, pickle.HIGHEST_PROTOCOL)


#!/usr/bin/env python

import networkx as nx
from networkx.algorithms import bipartite as bip
import mydataset as md

def test(a, b):
    print a, b

if __name__ == '__main__':
    with open('tracks.csv') as f:
        g, data, track_data = md.load_tracks_graph(f)
    bottom, top = bip.sets(g)
    print type(g['image-00034.jpg']['34143']['feature'])
    print test(*g['image-00034.jpg']['34143']['feature'])


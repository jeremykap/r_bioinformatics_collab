
from random import random
from math import floor
from SVG.gene_compare import GeneCompare


def compare_genes():

    genes = ["ENSG00001", "ENSG00002", "ENSG00003"]
    samples = [str(x) for x in range(30)]

    svg = GeneCompare(genes, width=700, group_legend=True, log_graph=True, y_label="RPKM")
    for gene in genes:
        for sample in samples:
            svg.add_data_point(gene, sample, (random() * 10) + (int(sample) * 10))

    for idx, sample in enumerate(samples):
        category = "category " + str(floor(idx/10))
        svg.add_legend_point(sample, category, idx)

    svg.build()
    svg.save(filename="../svg_examples/gene_compare.svg")


if __name__ == '__main__':
    compare_genes()

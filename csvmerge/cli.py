# -*- coding: utf-8 -*-

"""Console script for csvmerge."""
import click
import numpy as np
import pandas as pd
import sys

@click.command()
@click.option('-f1', '--from-file', required=True, type=click.Path(exists=True), help='input file to merge FROM (.csv)')
@click.option('-f2', '--to-file', required=True, type=click.Path(exists=True), help='input file to merge TO (.csv)')
@click.option('-k1', '--from-key', required=True, help='key in FROM file')
@click.option('-k2', '--to-key', required=True, help='key in TO file')
@click.option('-o', '--output-file', required=True, type=click.Path(exists=False), help='output file to write results (.csv)')
def main(from_file, to_file, from_key, to_key, output_file):
    """Console script for csvmerge."""
    of = open(output_file, 'wt')
    f1_df = read_file(from_file, from_key)
    print('read %d from %s' % (len(f1_df), from_file))
    header = False
    for row in iter_big_file(to_file, to_key):
        if row.name in f1_df.index:
            match = pd.DataFrame([f1_df.ix[row.name]])
            merged = pd.concat((pd.DataFrame([row]), match), axis=1)
            merged.columns = [c if i < len(row.index) else 'MATCH_%s' % c for i,c in enumerate(merged.columns)]
            if not header:
                print('writing header')  
                of.write(merged.iloc[:0].to_csv(index=False))
                header = True
            of.write(merged.to_csv(index=False, header=False))
    of.close()


def read_file(fname, key):
    return pd.read_csv(fname, skiprows=0, lineterminator='\n', index_col=key)

def iter_big_file(fname, key, chunksize=1000):
    for chunk in (pd.read_csv(fname, chunksize=chunksize, index_col=key)):
        for i, row in chunk.iterrows():
            yield row

if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover

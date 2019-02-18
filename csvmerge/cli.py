# -*- coding: utf-8 -*-

"""csvmerge"""
import click
import numpy as np
import pandas as pd
import re
import sys

@click.command()
@click.option('-f1', '--from-file', required=True, type=click.Path(exists=True), help='input file to merge FROM (.csv). This is typically the smaller file.')
@click.option('-f2', '--to-file', required=True, type=click.Path(exists=True), help='input file to merge TO (.csv). This can be a very large file, as it is only streamed from disk, never stored completely in memory.')
@click.option('-k1', '--from-key', required=True, help='field to match in the FROM file')
@click.option('-k2', '--to-key', required=True, help='field to match in the TO file')
@click.option('-o', '--output-file', required=True, type=click.Path(exists=False), help='output file to write results (.csv)')
def main(from_file, to_file, from_key, to_key, output_file):
    """Join two csv files on specified keys and write the results."""
    of = open(output_file, 'wt')
    f1_df = read_file(from_file, from_key)
    duns2row_f1 = {r[from_key]:r for i,r in f1_df.iterrows()}
    #print(list(duns2row_f1.items())[:10])
    print('read %d from %s' % (len(f1_df), from_file))
    header = False
    header1 = ['MATCH_%s' % c for i,c in enumerate(f1_df.columns)]
    for row in iter_big_file(to_file, to_key):
        header2 = [c for i,c in enumerate(row.index)]
        #if row.name in f1_df.index:
        if row[to_key] in duns2row_f1:
            match = duns2row_f1[row[to_key]]
            match = pd.DataFrame([match])
            match.reset_index(inplace=True, drop=True)
            row = pd.DataFrame([row])
            row.reset_index(inplace=True, drop=True)
            merged = pd.concat([row, match], axis=1, ignore_index=False)
            merged.reset_index(inplace=True, drop=True)
            merged.columns = np.concatenate((header2, header1))
            if not header:
                of.write(re.sub(r'\r', ' ', merged.iloc[:0].to_csv(index=False)))
                header = True
            of.write(merged.to_csv(index=False, header=False))
    of.close()


def read_file(fname, key):
    df = pd.read_csv(fname, lineterminator='\n', index_col=False)
    df.replace('[\n\t\r]', ' ', regex=True, inplace=True)
    return df


def iter_big_file(fname, key, chunksize=1000):
    for chunk in (pd.read_csv(fname, lineterminator='\n', chunksize=chunksize, index_col=False)):
        chunk.replace('[\n\t\r]', ' ', regex=True, inplace=True)
        for i, row in chunk.iterrows():
            yield row

if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover

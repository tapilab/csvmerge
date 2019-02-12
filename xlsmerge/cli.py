# -*- coding: utf-8 -*-

"""Console script for xlsmerge."""
import sys
import click
import pandas as pd

@click.command()
@click.option('-f1', '--from-file', required=True, type=click.Path(exists=True), help='input file to merge FROM (.csv)')
@click.option('-f2', '--to-file', required=True, type=click.Path(exists=True), help='input file to merge TO (.csv)')
@click.option('-k1', '--from-key', required=True, help='key in FROM file')
@click.option('-k2', '--to-key', required=True, help='key in TO file')
def main(from_file, to_file, from_key, to_key):
    """Console script for xlsmerge."""
    f1_df = read_file(from_file, from_key)

    for row in iter_big_file(to_file, to_key):
    	if row.name in f1_df.index:
	    	print(f1_df.ix[print(row.name)])

def read_file(fname, key):
	return pd.read_csv(fname, skiprows=0, lineterminator='\n', index_col=key)

def iter_big_file(fname, key, chunksize=1000):
	for chunk in (pd.read_csv(fname, chunksize=chunksize, index_col=key)):
		for i, row in chunk.iterrows():
			yield row

if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover

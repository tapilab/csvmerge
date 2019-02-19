========
csvmerge
========


.. image:: https://img.shields.io/pypi/v/csvmerge.svg
        :target: https://pypi.python.org/pypi/csvmerge

.. image:: https://img.shields.io/travis/aronwc/csvmerge.svg
        :target: https://travis-ci.org/aronwc/csvmerge

.. image:: https://readthedocs.org/projects/csvmerge/badge/?version=latest
        :target: https://csvmerge.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status




merge csv files


* Free software: BSD license
* Documentation: https://csvmerge.readthedocs.io.


Installation
------------

.. code-block:: console

    pip install git+https://github.com/tapilab/csvmerge.git


Usage
-----

Given two files `china.csv` and `chicago.csv`:

.. code-block:: console
    csvmerge  -f1 china.csv -f2 chicago.csv -k2 'Global Duns No' -k1 'D-U-N-S@ Number' -o output.csv

.. code-block:: console
    Usage: csvmerge [OPTIONS]

      Join two csv files on specified keys and write the results.

    Options:
      -f1, --from-file PATH   input file to merge FROM (.csv). This is typically
                              the smaller file.  [required]
      -f2, --to-file PATH     input file to merge TO (.csv). This can be a very
                              large file, as it is only streamed from disk, never
                              stored completely in memory.  [required]
      -k1, --from-key TEXT    field to match in the FROM file  [required]
      -k2, --to-key TEXT      field to match in the TO file  [required]
      -o, --output-file PATH  output file to write results (.csv)  [required]
      --help                  Show this message and exit.



Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

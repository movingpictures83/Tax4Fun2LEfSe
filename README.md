# Tax4Fun2LEfSe
# Language: Python
# Input: TXT 
# Output: TXT 
# Tested with: PluMA 2.0, Python 3.6

PluMA plugin that convert Tax4Fun2 (Wemheuer et al, 2020) output to LEfSe input format (Segata et al, 2011).

The input file is a tab-delimited parameter file of keyword value pairs:
tax4fun: TSV file of functional or metabolic pathways, output from Tax4Fun2
categories: CSV file of samples and categories

The plugin will produce one single TXT file for LEfSe, with sample names, categories, then abundances.

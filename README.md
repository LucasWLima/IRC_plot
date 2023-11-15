# IRC_plot
IRC plot generator for ORCA jobs.

Usage:

$ python3 IRC_plot.py [-h] [--Eh] [--dEh] [--dkcal] [--dkJ] fname

positional arguments:
  fname       Output file

optional arguments:
  -h, --help  show this help message and exit
  --Eh        Generate IRC plot with energies in Hartrees
  --dEh       Generate IRC plot with relative energies in Hartrees
  --dkcal     Generate IRC plot with relative energies in kcal/mol
  --dkJ       Generate IRC plot with relative energies in kJ/mol

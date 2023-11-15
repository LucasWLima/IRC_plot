import os
import re
import matplotlib.pyplot as plt
import numpy as np
import argparse

def E_Eh_graph(IRC_step, IRC_E_Eh):
    """
    Generates the IRC plot in Hartrees parsed from the ORCA output file.
    :param IRC_step: Numpy array with the IRC Steps parsed from the calculation
    :param IRC_E_Eh: Numpy array with the IRC energies in Hartrees parsed from the calculation
    :return: IRC plot
    """
    plt.plot(IRC_step, IRC_E_Eh, marker="o", ls="-", color="black")
    plt.xlabel("IRC Step")
    plt.ylabel("Energy [Eh]")
    plt.tight_layout()
    plt.grid()
    plt.show()
def dE_Eh_graph(IRC_step, IRC_E_Eh):
    """
    Generates the IRC plot in Hartrees parsed from the ORCA output file.
    :param IRC_step: Numpy array with the IRC Steps parsed from the calculation
    :param IRC_E_Eh: Numpy array with the IRC energies in Hartrees parsed from the calculation
    :return: IRC plot with relative energies in Hartrees
    """
    dE_kcal = IRC_E_Eh - IRC_E_Eh[0]
    plt.plot(IRC_step, dE_kcal, marker="o", ls="-", color="black")
    plt.xlabel("IRC Step")
    plt.ylabel("Relative Energy [Eh]")
    plt.tight_layout()
    plt.grid()
    plt.show()
def dE_kcal_graph(IRC_step, IRC_E_Eh):
    """
    Generates the IRC plot in Hartrees parsed from the ORCA output file.
    :param IRC_step: Numpy array with the IRC Steps parsed from the calculation
    :param IRC_E_Eh: Numpy array with the IRC energies in Hartrees parsed from the calculation
    :return: IRC plot with relative energies in kcal/mol
    """
    dE_kcal = (IRC_E_Eh - IRC_E_Eh[0]) * 627.5
    plt.plot(IRC_step, dE_kcal, marker="o", ls="-", color="black")
    plt.xlabel("IRC Step")
    plt.ylabel("Relative Energy [kcal/mol]")
    plt.tight_layout()
    plt.grid()
    plt.show()
def dE_kJ_graph(IRC_step, IRC_E_Eh):
    """
    Generates the IRC plot in Hartrees parsed from the ORCA output file.
    :param IRC_step: Numpy array with the IRC Steps parsed from the calculation
    :param IRC_E_Eh: Numpy array with the IRC energies in Hartrees parsed from the calculation
    :return: IRC plot with relative energies in kJ/mol
    """
    dE_kJ = (IRC_E_Eh - IRC_E_Eh[0]) * 2625.5
    plt.plot(IRC_step, dE_kJ, marker="o", ls="-", color="black")
    plt.xlabel("IRC Step")
    plt.ylabel("Relative Energy [kJ/mol]")
    plt.tight_layout()
    plt.grid()
    plt.show()

# Parser creation
parser = argparse.ArgumentParser(description='IRC plot generator for ORCA jobs.')
parser.add_argument('fname', help='Output file')
parser.add_argument('--Eh', action='store_false',
                    help='Generate IRC plot with energies in Hartrees')
parser.add_argument('--dEh', action='store_false',
                    help='Generate IRC plot with relative energies in Hartrees')
parser.add_argument('--dkcal', action='store_false',
                    help='Generate IRC plot with relative energies in kcal/mol')
parser.add_argument('--dkJ', action='store_false',
                    help='Generate IRC plot with relative energies in kJ/mol')

args = parser.parse_args()

directory = os.getcwd()
file = os.path.join(directory, args.fname)
with open(file, 'r') as f:
    data = f.read()
    searchbox = re.findall(r"^Step(.*)^Timings", data, re.MULTILINE | re.DOTALL)
    parsed_values = searchbox[0].split("\n")
    parsed_values = parsed_values[1:-2]

    lines = []
    for i in range(0, len(parsed_values)):
        line = parsed_values[i].split()
        lines.append(line)

    Step = []
    E_Eh = []
    for j in range(0, len(lines)):
        Step.append(lines[j][0])
        E_Eh.append(lines[j][1])

    Step = np.array([int(step) for step in Step])
    E_Eh = np.array([float(e_eh) for e_eh in E_Eh])

    if args.Eh != True:
        E_Eh_graph(Step, E_Eh)
    elif args.dEh != True:
        dE_Eh_graph(Step, E_Eh)
    elif args.dkcal != True:
        dE_kcal_graph(Step, E_Eh)
    elif args.dkJ != True:
        dE_kJ_graph(Step, E_Eh)

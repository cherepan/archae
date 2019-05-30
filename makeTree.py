#!/usr/bin/env python


import os
import ROOT
import sys
import math
import argparse
from array import array



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--input-file",help="input file. [Default: %(default)s] ", action="store", default = 'card.dat')
    args = parser.parse_args()


    output_file = ROOT.TFile("output_"+args.input_file+".root", "RECREATE")
    output_tree = ROOT.TTree()
    output_tree.SetName("t")


    MType = array('f', [0]);
    L = array('f', [0]);
    a = array('f', [0]);
    D = array('f', [0]);
    orientation = array('f', [0]);
    content = array('f', [0]);

    output_tree.Branch("orientation",orientation,"orientation/F")
    output_tree.Branch("MType",MType,"MType/F")
    output_tree.Branch("L",L,"L/F")
    output_tree.Branch("a",a,"a/F")
    output_tree.Branch("D",D,"D/F")
    output_tree.Branch("content",content,"content/F")


    datasetsFile = args.input_file
    if not os.path.isfile(datasetsFile):
        print "File %s not found!!!" % datasetsFile
        sys.exit()
    with open(datasetsFile) as fIn:
        for line in fIn:
           line = line.strip()
           x = line.split()
           MType[0] =   float(x[0])
           L[0] =   float(x[1])
           a[0] =   float(x[2])
           D[0] =   float(x[3])
           orientation[0]  = float(x[4])
           content[0]  = float(x[5])
           output_tree.Fill()

    output_tree.Write()
    output_file.Write()
    output_file.Close()

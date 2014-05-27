#!/usr/bin/env python

"""profile_rallapck.py: 

Last modified: Sat Jan 18, 2014  05:01PM

"""
    
__author__           = "Dilawar Singh"
__copyright__        = "Copyright 2013, NCBS Bangalore"
__credits__          = ["NCBS Bangalore", "Bhalla Lab"]
__license__          = "GPL"
__version__          = "1.0.0"
__maintainer__       = "Dilawar Singh"
__email__            = "dilawars@iitb.ac.in"
__status__           = "Development"

import os
import sys
import subprocess

simclockList = {}
try:
    from lxml  import etree
except Exception as e:
    from xml import etree

def runRallpack3( startN = 10, stepSize = 50):
    import rallpacks_cable_hhchannel as rallpack3
    comps = startN
    while comps < 10000:
        rallpack3.main( {'ncomp' : comps, 'output': 'rallpack3.png'
            , 'dt' : 5e-5, 'run_time' : 0.25 }
            )
        comps += stepSize

def simResult( elemXml ):
    """ Get a single simXML and return a plottable entity 
    """
    timeStamp = elemXml.get("time_stamp")
    global simclockList 
    simclockList = {}
    elementList = {}
    for x in elemXml.iterchildren("elements"):
        for y in x:
            elementList[y.tag] = int(y.text)
        if not elementList:
            print("[INFO] Empty simulation. Ignoring ")
            return None
    for x in elemXml.iterchildren("times"):
        for y in x:
            simclockList[y.tag] = float( y.text )
    return elementList, simclockList

def plotProfile(results, output=None):
    import pylab
    xvec = []
    yvecs = [[], [], []]
    for r in results:
        if r is None:
            continue
        xvec.append( r[0]['Compartment'] )
        for i, c in enumerate(r[1]):
            yvecs[i].append( r[1][c] )

    plots = []
    for i, yvec in enumerate(yvecs):
        p, = pylab.plot(xvec, yvec, 'o')
        plots.append(p)

    pylab.legend(plots, simclockList.keys())
    pylab.xlabel('No of compartment in active cable')
    pylab.ylabel('Tiime spend by moose basecode')
    pylab.title('Rallpack 3: Step size 10 compartments')
    if output is None:
        pylab.show()
    else:
        print("[PLOT] Saving plots to {}".format(output))
        pylab.savefig(output)

def processProfile ( profileFile ):
    """ This function process the profile file given in xml format 
    """
    print("[STEP] Processing profile file {}".format( profileFile ))
    with open( profileFile, "r") as f:
        xmlTxt = f.read()
    print("[INFO] Sorrounding xml with a single root tag")
    xmlTxt = "<root>{}</root>".format( xmlTxt )
    tree = etree.fromstring( xmlTxt )
    results = [ simResult(x) for x in tree ]
    return results

def main( args ):
    if args.get('input', None) is not None:
        results = processProfile( args['input'] )
        plotProfile(results, output=args.get('output', None))
    else:
        print("[TODO] Profile rallpack3")
    
if __name__ == '__main__':
    import argparse
    # Argument parser.
    description = '''Process profile file generated by Moose basecode '''
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('-i', '--input'
            , required = False
            , help = 'Profile file in xml format e.g. __moose__.dat. If not '
            ' given then I\' run the profile code to generate one.'
            )
    parser.add_argument('-o', '--output'
            , type = str
            , help = 'I will store plot to this file.'
            )
    args = vars(parser.parse_args())
    main( args )

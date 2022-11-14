#!/usr/bin/env python
'''

Extract PLUGIN information from 'Gig Performer.settings' or .gig-files
=======================================================================

usage:
     GPpyTools.py -s               : extracts PLUGINS from 'Gig Performer.settings' and write to 'GigPerformerPlugins.xlsx' in same folder
     GPpyToos.py <gigfie.gig>      : extracts PLUGINS from 'gigfile.gig' and write to 'gigfile.gig.xlsx' in same folder
     
BBB, 27-NOV-2021 - initial script
BBB, 14-NOV-2022 - added Rackspace Names and delayedStart Info, added function AddPluginInfo(), Cleanup...

'''

import pandas as pd
import xml.etree.ElementTree as et
import openpyxl
import sys
import os.path

rows = []      # global, quick'n'dirty, see below...

# iterate through desired contecxt section and fill table 
def AddPluginInfo(s_rackspacename, context, mode) :
     global rows
     for node in context.iter('PLUGIN'):
          s_name = node.attrib.get("name")
          s_manuf = node.attrib.get("manufacturer")
          s_version = node.attrib.get ("version")
          s_format = node.attrib.get ("format")        
         
          if mode == 'SETTINGS':
               s_file = node.attrib.get ("file")
               s_isEnabled = node.attrib.get ("isEnabled")
               s_delayed = node.attrib.get("useDelayedLoading")
 
               rows.append({"name": s_name, "manufacturer": s_manuf, "version": s_version,
                         "isEnabled": s_isEnabled, "delayedStart": s_delayed, "format": s_format, "file": s_file})
               
          elif mode == 'GIG':
               rows.append({"rackspace": s_rackspacename, "name": s_name, "manufacturer": s_manuf, "version": s_version, "format": s_format})

def main():
     global rows
     inputfile=""; outputCSV=''; outputXLS=''; mode = ''
     
     args = sys.argv[1:]
     if len(args) == 1 and args[0] == '-s':
          inputfile = "Gig Performer.settings"
          if os.path.isfile(inputfile):
               outputCSV = "GigPerformerPlugins.csv"
               outputXLS = "GigPerformerPlugins.xlsx"
               mode = 'SETTINGS'
          else:
               print (inputfile + " does not exist?!")
               return        
          
     elif len(args) == 1:
          if os.path.isfile(args[0]):
               inputfile = args[0]
               outputCSV = args[0] + ".csv"
               outputXLS = args[0] + ".xlsx"
               mode = 'GIG'
          else:
               print (args[0] + " does not exist?!")
               return        
     else:
         print("GPpyTools.py -s or GPpyTools <inputfile.gig>")
         return
                      
     # prepare XML-inputfile for readout 
     xtree = et.parse(inputfile)
     xroot = xtree.getroot()
     
     '''
     Pick infos from the PLUGIN attribs (example):
             name="4U+ DynamicTiltEQ" format="AudioUnit" category="Effect"
                   manufacturer="HOFA" version="1.0.7" file="AudioUnit:Effects/aufx,hff6,HOFA"
                   uid="08154711" isInstrument="0" fileTime="0" infoUpdateTime="179dd49ca03"
                   numInputs="4" numOutputs="2" isShell="0" isEnabled="1" useDelayedLoading="0"/>
     '''
          
     if mode == 'GIG':
          print("Get Rackspaces from GIG file '" + inputfile + "'")
          df_cols = ["rackspace", "name", "manufacturer", "version", "format"]
          
          for n_rackspace in xroot.iter('GLOBALRACKSPACE'):
               s_rackspace = n_rackspace.attrib.get("name")
               #print (s_rackspace)  
               AddPluginInfo(s_rackspace, n_rackspace, mode)
                       
          for n_rackspace in xroot.iter('RACKSPACE'):
               s_rackspace = n_rackspace.attrib.get("name")
               #print (s_rackspace)  
               AddPluginInfo(s_rackspace, n_rackspace, mode)       
               
     if mode == 'SETTINGS':
          print("Get global Plugin Manager information")  
          df_cols = ["name", "manufacturer", "version", "isEnabled", "delayedStart", "format", "file"]
          AddPluginInfo('none', xroot, mode)  
                       
     
     out_df = pd.DataFrame(rows, columns=df_cols)
     
     # Writing dataframe to csv
     # out_df.to_csv(outputCSV)
     # print(outputCSV + " written")
     # Writing dataframe to xsx
     out_df.to_excel(outputXLS, sheet_name='Plugins')  
     print(outputXLS + " written")

     
# Python boilerplate.
if __name__ == '__main__':
    main()

# eof...
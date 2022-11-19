# GPpyTools
Readout of AU/VST plugin information from [Gig Performer 4](https://gigperformer.com) .gig-files or from the Plugin Manager section of the GigPerformer  settings file.

## Usage

```
      GPpyTools.py -s               extracts PLUGINS from 'Gig Performer.settings' 
                                    and write to 'GigPerformerPlugins.xlsx' in same folder
      GPpyTools.py <gigfie.gig>     extracts PLUGINS from 'gigfile.gig' 
                                    and write to 'gigfile.gig.xlsx' in same folder
```

The created excel files can by filtered, e.g. to figure out which rackspace uses a specific Plugin in which format (AU, VST, VST3).

Initial script back in 2021. Tested with Gig Performer 4.5.8 files under macOS 12.6 Monterey and Python v3.10.2 (v3.7.4 before...)

Have fun!

## Environment

I use MS Visual Studio Code with the python extension, also from MS. I created a virtual environment with the additional module 'pandas' and 'openpyxl'. Please refer to a suitable documentation how to do this on web. 

## Binaries

After updating my Python environment to 3.10.2 on my Mac I was finally able to build a standalone macOS console app. So I just added binaries here for Mac and Windows (based on Python 3.10.8...).

They have been created using pyinstaller with the onefile/standalone option (after installing it with pip install pyinstaller...)

```
pyinstaller GPpyTools.py --onefile
```
I just moved a binary for the mac app and a GPpyTools.exe for Windows to the binaries folder. 

The binaries work the same as the Python scripts...
```
      GPpyTools(.exe) -s              extracts PLUGINS from 'Gig Performer.settings' 
                                      and write to 'GigPerformerPlugins.xlsx' in same folder
      GPpyTools(.exe) <gigfie.gig>    extracts PLUGINS from 'gigfile.gig' 
                                      and write to 'gigfile.gig.xlsx' in same folder
```


## Disclaimer

Whenever possible use this tool from your personal Python environment! I cannot guarantee that the binaries are free from any side effects on your computers - I'm not a professional prgrammer, and this is my first try providing executables beside the pure python scripts...
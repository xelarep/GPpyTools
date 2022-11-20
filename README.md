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

I use MS Visual Studio Code with the python extension, also from MS. I created a virtual environment with the additional module 'pandas' and 'openpyxl'. Please refer to a suitable documentation oin how to do this on the web... 

## Binaries

After updating my Python environment to 3.10.2 on my Mac I was finally able to build a standalone macOS console app. So I just added binaries here for Mac and Windows (based on Python 3.10.8...).

They have been created using the pyinstaller with the onefile/standalone option (after installing it with `pip install pyinstaller`...)

```
pyinstaller GPpyTools.py --onefile
```
I just moved a `GPpyTools` binary for the macOS app and a `GPpyTools.exe` for Windows to the binaries folder. 

The binaries work the same way as the Python script...
```
      GPpyTools(.exe) -s              extracts PLUGINS from 'Gig Performer.settings' 
                                      and write to 'GigPerformerPlugins.xlsx' in same folder
      GPpyTools(.exe) <gigfie.gig>    extracts PLUGINS from 'gigfile.gig' 
                                      and write to 'gigfile.gig.xlsx' in same folder
```

### Mac users
After downloading the GPpyTools binary macOS may block it as it is not signed and suspected to be malware. Also the Download folder in macOS is something 'special' and may need some extra permission in the terminal...
So, just move the GPpyTools app to a suitable folder (e.g. ~/temp) and Shift-right click to open GPpyTools for the first time. Allow macOS to open and wait for the now opening terminal to finish the first time.
Now you can 'cd' in any terminal to your folder from above and start `./GPpyTools "you gig file.gig"` and everything should work.


## Disclaimer

Whenever possible use this tool from your personal Python environment! I cannot guarantee that the binaries are free from any side effects on your computers - I'm not a professional programmer, and this is my first try providing executables beside the pure Python scripts...

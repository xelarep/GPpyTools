# GPpyTools
Readout of AU/VST plugin information from [Gig Performer 4](https://gigperformer.com) .gig-files or from the Plugin Manager section of the GigPerformer  settings file.

## Usage

```
      GPpyTools.py -s               extracts PLUGINS from 'Gig Performer.settings' 
                                    and write to 'GigPerformerPlugins.xlsx' in same folder
      GPpyToos.py <gigfie.gig>      extracts PLUGINS from 'gigfile.gig' 
                                    and write to 'gigfile.gig.xlsx' in same folder
```

The created excel files can by filtered, e.g. to figure out which rackspace uses a specific Plugin in which format (AU, VST, VST3).

Initial script back in 2021. Tested with Gig Performer 4.5.8 files under macOS 12.6 Monterey and Python 3.7.4

Have fun!

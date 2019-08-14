Post Processing Script for SabNZBD
===========================
This script will automatically rename and move files after they are downloaded.

Features
--------
- Supports Windows and Linux systems
- Renames file according to scene title
- Adds Scene ID to filename if necessary
- Designed to make plex matching with this metadata agent work smoothly/automatically
- Deletes leftover files and empty folders
- Batch rename old collections (on windows)


- Customisation:
  - Specify how to handle duplicates
  - Specify where to move renamed files
  - Include Media Info in the file or folder name. e.g Resolution/Framerate
  
Dependancies
--------
- lxml
  - `pip install lxml`
- If using Media Info Options:
  - `pip install pymediainfo`
  - https://mediaarea.net/en/MediaInfo for the MediaInfo.DLL file

Instructions
--------
1. Place the files in you sabnzbd script folder
2. Point SabNZBD to pa_renamer_post.py
3. Customise your settings in siteConfig.py
4. Set sabnzbd to run this post processing script after appropriate downloads complete

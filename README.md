# rbxmx-bulk-export

rbxmx bulk exporter for rbxlx rojo projects in python using Element Tree for xml and Tkinter for GUI.
Separated one large rbxmx export into multiple smaller rbxmx files.

## Usage

1. Place all models, audio and image assets inside a parent folder.

```bash
-- Workspace:Service
  |- Export:Folder
    |- Apple:Model
    |- Blueberry:Model
    |- Grape:Model
    |- Lime:Model
    |- Orange:Model
```

2. Right click the folder with the assets to be exported, save to file as a rbxmx file.

3. Run main.py
4. Select the rbxmx file to separate into other rbxmx files.
5. Select a folder to create the new rbxmx files in.

Refer to [example1](tests/example1) in [tests](tests).

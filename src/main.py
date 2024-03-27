# https://stackoverflow.com/a/3579625
from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import askdirectory

import xml.etree.ElementTree as ET

# Header xml that all .rbxlx files must have to be valid
header = '''
<roblox xmlns:xmime="http://www.w3.org/2005/05/xmlmime" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.roblox.com/roblox.xsd" version="4">
    <Meta name="ExplicitAutoJoints">true</Meta>
	<External>null</External>
	<External>nil</External>
'''

# Footer xml that all .rbxlx files must have to be valid
# TODO - temp fix, some exports need the <SharedStrings> tag while other don't
footer =  '''
    <SharedStrings>
        <SharedString md5="yuZpQdnvvUBOTYh1jqZ2cA=="></SharedString>
	</SharedStrings>
</roblox>'''

# selected rbxlx file follows an xml structure, there are multiple xml trees that need to be separated inside this file
# these separated trees inserted into new xml files and placed in a user selected directory.

# number of parent tags after header
afterHeaderIndex = 3

Tk().withdraw()
selectfile = askopenfilename() # get the rbxlx file to be separated
directory = askdirectory() # get directory to create new rbxlx files

# open and read the rbxlx file
originalFileOpened = open(selectfile, 'r')
originalFileRead = originalFileOpened.read()

root = ET.fromstring(originalFileRead) # create element tree object from read rbxlx string

# look past the original header for the rbxlx file and iterate through each sub tree
for item in root[afterHeaderIndex]:

  if item.tag == 'Properties': # do not iterate through root tree properties
    continue
  
  # get the name of the subtree to separate form the main tree
  itemProperties = item[0]
  name = itemProperties.find("string").text

  # add the rbxlx header and footer to the extracted sub tree and format the code
  separatedText = header + ET.tostring(item, "unicode") + footer
  formatText = ET.fromstring(separatedText)
  ET.indent(formatText, '    ', 0)

  # create a new rbxlx file at the selected directory and write the spearated xml data
  f = open(directory + "/" + name + ".rbxmx", 'w')
  f.write(ET.tostring(formatText, "unicode"))
  f.close()

from xml.etree import ElementTree as ET

filePath = 'D:/Python/HttpTests/test.xml'
def agentID():
    try:
        tree = ET.parse(filePath)
        root = tree.getroot()
       #print(root)
        for p in root.findall('.//AgentID'):
            return p.text
    except IOError:
        print('Error occured during parsing')
def agentIP():
    try:
        tree = ET.parse(filePath)
        root = tree.getroot()
       #print(root)
        for p in root.findall('.//AgentIP'):
            return p.text
    except IOError:
        print('Error occured during parsing')
def agentPORT():
    try:
        tree = ET.parse(filePath)
        root = tree.getroot()
       #print(root)
        for p in root.findall('.//AgentPORT'):
            return p.text
    except IOError:
        print('Error occured during parsing')
def serverIP():
    try:
        tree = ET.parse(filePath)
        root = tree.getroot()
       #print(root)
        for p in root.findall('.//ServerIP'):
            return p.text
    except IOError:
        print('Error occured during parsing')
def serverPORT():
    try:
        tree = ET.parse(filePath)
        root = tree.getroot()
       #print(root)
        for p in root.findall('.//ServerPORT'):
            return p.text
    except IOError:
        print('Error occured during parsing')
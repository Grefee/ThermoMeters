import datetime as d
import requests
import xml.etree.ElementTree as ET
import io



class Teplomer:
    def __init__(self, ip_add, id, name):
        self.ip_add = ip_add
        self.id = id
        self.name = name
        value = None
        self.value = value

    def teplomerData(self):
        self.ip_add
        self.name
        return (self.ip_add,self.name)

    def teplomerName(self):
        self

    def getData(self):
        page = requests.get("http://" + self.ip_add + "/xml/?mode=sensor&type=list&id=01")
        xmlPage = page.content.decode("utf-8")
        f = io.StringIO(xmlPage)
        tree = ET.parse(f)
        root = tree.getroot()

        for child in root:
            if (child.tag == "name"):
                term_name = child.text
            if (child.tag == "current"):
                term_value = child.text

        timeStamp = str(d.datetime.now())
        print("-----")

        print("nazev :" + term_name)
        print("teplota :" + term_value)

        print("cas :" + timeStamp)

        return (self.ip_add, term_value, timeStamp)




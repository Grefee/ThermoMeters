import xml.etree.ElementTree as ET
import io
import teplomer



def readTermMeter():
    with io.open("xmlConfig.xml", "r",encoding="utf-8") as xmlPage:
        f = ET.parse(xmlPage)
        root = f.getroot()
    for child in root:
        if (child.tag == "temp"):
            for var in child:
                if(var.tag == "id"):
                    id = var.text
                if(var.tag == "name"):
                    name = var.text
                if(var.tag == "ip"):
                    ip_add = var.text
            print (id, name, ip_add)
            teplomer.Teplomer(id, name, ip_add)

readTermMeter()
locals()




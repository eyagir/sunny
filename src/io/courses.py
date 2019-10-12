import requests
from bs4 import BeautifulSoup

class course_scraper:
    url = 'https://csrpt.cc.unc.edu/psc/csreportsns/EMPLOYEE/UNC_CSNS/c/COMMUNITY_ACCESS.CLASS_SEARCH.GBL'
    
    form_data = {"ICAJAX": "1",
                 "ICNAVTYPEDROPDOWN": "0",
                 "ICType": "Panel",
                 "ICElementNum": "0",
                 "ICStateNum": "11",
                 "ICAction": "CLASS_SRCH_WRK2_SSR_PB_CLASS_SRCH",
                 "ICModelCancel": "0",
                 "ICXPos": "0",
                 "ICYPos": "0",
                 "ResponsetoDiffFrame": "-1",
                 "TargetFrameName": "None",
                 "FacetPath": "None",
                 "ICFocus": "",
                 "ICSaveWarningFilter": "0",
                 "ICChanged": "-1",
                 "ICSkipPending": "0",
                 "ICAutoSave": "0",
                 "ICResubmit": "0",
                 "ICSID": "VZrKMRstMwDAJ0FNd9BDGeWrL6ofu%2BzgqeRRGsk2Dis%3D",
                 "ICActionPrompt": "false",
                 "ICTypeAheadID": "",
                 "ICBcDomData": "UnknownValue",
                 "ICPanelName": "",
                 "ICFind": "",
                 "ICAddCount": "",
                 "ICAppClsData": "",
                 "SSR_CLSRCH_WRK_CATALOG_NBR$1": "411"}
    
    response = requests.post(url = url, data = form_data)

    print(response.text)

        

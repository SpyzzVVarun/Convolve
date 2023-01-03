import warnings
warnings.filterwarnings('ignore')
from driver import driver
from selenium.webdriver.common.by import By
import re
# import json

def parsePage(links):
    feature_configs = dict()

    for link in links:
        driver.get(link)
        elements = driver.find_elements(By.XPATH, "//*[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'summary steps')]")
        if (len(elements)):
            for element in elements:
                headings = []
                for i in range(1,7):
                    try:
                        headings.append(element.find_element(By.XPATH, f"./preceding::h{i}[1]").location["y"])
                    except:
                        pass
                idx = headings.index(max(headings))+1
                heading = element.find_element(By.XPATH, f"./preceding::h{idx}[1]")
                while ('procedure' in heading.text.lower() or 'before' in heading.text.lower()):
                    headings[idx-1] = heading.find_element(By.XPATH, f"./preceding::h{idx}[1]").location["y"]
                    idx = headings.index(max(headings))+1
                    heading = heading.find_element(By.XPATH, f"./preceding::h{idx}[1]")
                ol = element.find_element(By.XPATH, "./following-sibling::ol[1]") #assumption
                if (ol.text.split('\n')[-1] == ol.text.split('\n')[-2]):
                    feature_configs[heading.text] = ol.text.split('\n')[:-1]
                else:
                    feature_configs[heading.text] = ol.text.split('\n')
        else:
            elements = driver.find_elements(By.CSS_SELECTOR, "table")
            if (len(elements)):
                for element in elements:
                    headings = []
                    for i in range(1,7):
                        try:
                            headings.append(element.find_element(By.XPATH, f"./preceding::h{i}[1]").location["y"])
                        except:
                            pass
                    idx = headings.index(max(headings))+1
                    heading = element.find_element(By.XPATH, f"./preceding::h{idx}[1]")
                    while ('procedure' in heading.text.lower() or 'before' in heading.text.lower()):
                        headings[idx-1] = heading.find_element(By.XPATH, f"./preceding::h{idx}[1]").location["y"]
                        idx = headings.index(max(headings))+1
                        heading = heading.find_element(By.XPATH, f"./preceding::h{idx}[1]")
                        
                    if element.get_attribute("outerHTML").lower().count('step') >= 3:
                        lst = []
                        for row in element.find_elements(By.CSS_SELECTOR, "tr")[1:]:
                            if row.text.lower().split(' ')[0] == 'note':
                                continue
                            string = row.find_elements(By.CSS_SELECTOR, "td")[1].text.lower()
                            word = "example"
                            result = string.split(word)[0]
                            lst.append(re.sub("\n", "", result))
                        feature_configs[heading.text] = lst

    return feature_configs
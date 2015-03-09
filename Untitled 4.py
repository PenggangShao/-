#! /usr/bin/env python

#coding=utf-8
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import time
driver = webdriver.Firefox()
url = "http://localhost:4502"
driver.get(url)
driver.implicitly_wait(5)
driver.find_element_by_id("learnmore").click()
driver.implicitly_wait(10)
driver.back()
driver.implicitly_wait(5)
driver.find_element_by_link_text('help')
webdriver.back()
driver.find_element_by_link_text("Terms of Use").click()
webdriver.implicitly_wait(10)
driver.find_element_by_link_text("Privacy Policy and Cookies").click()
driver.back()
driver.find_element_by_id("username").send_keys("admin")
driver.find_element_by_id('password').send_keys('admin')
#driver.find_element_by_tag_name("button").click()
driver.find_element_by_tag_name("button").send_keys(Keys.ENTER)
driver.find_element_by_link_text("Assets").click()
driver.find_element_by_id("aem-assets-create").click()
ActionChains(driver).move_to_element(driver.find_element_by_link_text('Create Folder')).perform()
ActionChains(driver).click().perform()
driver.find_element_by_id("foldertitle").send_keys('selenium')
driver.find_element_by_id("privatefoldercb").click()
driver.find_element_by_id('createfolder-submit').click()
driver.find_element_by_xpath('//a[@data-foundation-content-history-title="selenium"]').click()
driver.find_element_by_xpath('//input[@type="file"]').send_keys(u'/Users/test/Downloads/pic.png')
driver.find_element_by_xpath('//button[@class="coral-Button coral-Button--primary uploadBtn"]').click()  #Upload Button
# driver.find_element_by_xpath('//button[@class="coral-Button"]').click() Cancel button
# Open enter selection 
driver.find_element_by_xpath('//i[@class="coral-Icon coral-Icon--checkCircle"]').click()
#select assets
driver.find_element_by_xpath('//a[@data-foundation-content-history-title="logdata.dat"]').click()
driver.find_element_by_xpath('//@a[data-foundation-content-history-title="build.txt"]').click()
ActionChains(driver).move_to_element(driver.find_element_by_xpath('//a[@data-foundation-content-history-title="build.txt"]')).perform()
ActionChains(driver).click().perform()
ActionChains(driver).move_to_element(driver.find_element_by_xpath('//button[@class="endor-ActionBar-item cq-damadmin-admin-actions-download-activator foundation-collection-action coral-Button coral-Button--secondary coral-Button--quiet"]')).perform()
ActionChains(driver).click().perform()
# Cancel button
ll = driver.find_elements_by_xpath('//button[@class="coral-Button"]')
for x in ll:
    if x.text == "Cancel":
        x.click()
ActionChains(driver).move_to_element(driver.find_element_by_xpath('//button[@class="endor-ActionBar-item cq-damadmin-admin-actions-download-activator foundation-collection-action coral-Button coral-Button--secondary coral-Button--quiet"]')).perform()
ActionChains(driver).click().perform()
#Download button
ll1 = driver.find_element_by_xpath('//[@class="coral-Button coral-Button--primary"]')
for y in ll1:
    if y.text == "Download":
        y.click()
#Download title/assetname
ActionChains(driver).move_to_element(driver.find_element_by_xpath('//button[@class="endor-ActionBar-item cq-damadmin-admin-actions-download-activator foundation-collection-action coral-Button coral-Button--secondary coral-Button--quiet"]')).perform()
ActionChains(driver).click().perform()
s1 = driver.find_element_by_id("dam-asset-download-label").text
if s1 == "Download":
    print "Access download panel"
ActionChains(driver).move_to_element(driver.find_element_by_xpath('//button[@class="endor-ActionBar-item cq-damadmin-admin-actions-download-activator foundation-collection-action coral-Button coral-Button--secondary coral-Button--quiet"]')).perform()
ActionChains(driver).click().perform()
s1 = driver.find_element_by_id("dam-asset-download-title").get_attribute("value")
if s1[0:-4] == "logdata.dat":
    print s1
# Cancel the download panel
driver.refresh()
driver.find_element_by_xpath('//i[@class="coral-Icon coral-Icon--checkCircle"]').click()
#Copy need enter selection mode and select asset
driver.find_element_by_xpath('//i[@class="coral-Icon coral-Icon--copy"]').click()
driver.find_element_by_xpath('//i[@class="coral-Icon coral-Icon--paste"]').click()
for x in driver.find_elements_by_tag_name('h4'):
    if x.text == "logdata1.dat":
        print 'True'
driver.find_element_by_xpath('//i[@class="coral-Icon coral-Icon--checkCircle"]').click()
#publish
driver.find_element_by_xpath('//i[@class="endor-ActionButton-icon coral-Icon coral-Icon coral-Icon--globe"]').click()
ActionChains(driver).move_to_element(driver.find_element_by_xpath('//a[@class="cq-damadmin-admin-actions-publish-activator foundation-collection-action s7off endor-List-item endor-List-item--interactive coral-Link"]')).perform()
ActionChains(driver).click().perform()
for x in driver.find_elements_by_xpath('//h2[@class="coral-Modal-title coral-Heading coral-Heading--2"]'):
    if x.text == "Success":
        print "Publish Success"
    else:
        pass
ss = driver.find_elements_by_xpath('//div[@class="coral-Modal-body"]')
for s in ss:
    if s.text != "":
        print s.text
    else:
        pass
closebtns = driver.find_elements_by_xpath('//button[@class="coral-Button coral-Button coral-Button--primary"]')
for s in closebtns:
    if s.text != "":
        print s.text
        s.click()
closeicons = driver.find_elements_by_xpath("//button[@class='coral-MinimalButton coral-Modal-closeButton']")
closeicons[28].click()
#Back icon
driver.find_element_by_css_selector(".coral-Icon.coral-Icon--chevronLeft").click()
#Publish later
ActionChains(driver).move_to_element(driver.find_element_by_xpath('//a[@class="endor-List-item cq-damadmin-admin-actions-publish-activator foundation-collection-action endor-List-item--interactive coral-Link"]')).perform()
ActionChains(driver).click().perform()
#Tooltip
print driver.find_element_by_css_selector(".coral-Form-fieldinfo.coral-Icon.coral-Icon--infoCircle.coral-Icon--sizeS").get_attribute("data-quicktip-content")
#Calendar icon
driver.find_element_by_css_selector(".coral-Button.coral-Button--secondary.coral-Button--square").click()
driver.find_element_by_css_selector(".coral-MinimalButton.coral-DatePicker-nextMonth").click()
trs = driver.find_elements_by_tag_name("tr")
tds = driver.find_elements_by_tag_name("td")
#Calendar 
'''
current_time = time.strftime("%Y-%m-%d")
monthes = ["January","February","March","April","May","June","July","August","September","October","November","December"]
cuttent_month = driver.find_elements_by_css_selector(".coral-Heading.coral-Heading--2")[2].text
month={"January":'1',"February":'2',"March":'3',"April":'4',"May":'5',"June":'6',"July":'7',"August":'8',"September":'9',"October":'10',"November":'11',"December":'12'}
x = 1
f = True
jj = 1
while x < 7:
	y = 1
	while y < 8:
		ss = "//tr["+str(x)+"]/td["+str(y)+"]"
		day = int(driver.find_element_by_xpath(ss).text)
		month1 = cuttent_month[:-5]
		print f
		if day > 1:
			if f:
				cal_time = cuttent_month[-4:]+"-"+ month[monthes[int(month[cuttent_month[:-5]])-2]] +"-"+ driver.find_element_by_xpath(ss).text
				print cal_time,
			else:
				cal_time = cuttent_month[-4:]+"-"+ month[cuttent_month[:-5]] + "-" + driver.find_element_by_xpath(ss).text
				
				print cal_time,
		if day == 1:
			cal_time = cuttent_month[-4:]+"-"+ month[cuttent_month[:-5]] + "-" + driver.find_element_by_xpath(ss).text
			print cal_time,
			f = False
			
		y += 1
	x += 1
	print
'''
x = 1
while x < 7:
    y = 1
    while y < 8:
        ss = "//tr["+str(x)+"]/td["+str(y)+"]"
        print driver.find_element_by_xpath(ss).text
        driver.find_element_by_xpath(ss).click()
        y += 1
    x += 1
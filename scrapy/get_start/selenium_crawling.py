from selenium import webdriver

browser = webdriver.PhantomJS()
browser.get('http://app1.sfda.gov.cn/datasearch/face3/base.jsp?tableId=120&tableName=TABLE120&title=%CA%B3%C6%B7%C9%FA%B2%FA%D0%ED%BF%C9%BB%F1%D6%A4%C6%F3%D2%B5(SC)&bcId=145275419693611287728573704379')
browser.implicitly_wait(10)
html = browser.page_source
subTable = browser.find_elements_by_xpath('//table[@width="763"]')
# subSelector = subTable[1].xpath('tr[position() mod 2 = 1]//text()')
# sub = browser.find_elements_by_xpath('//img[@src="images/dataanniu_07.gif"]')
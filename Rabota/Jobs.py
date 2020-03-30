import re
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import sqlite3 as sql
from torrequest import TorRequest

class Proxy:
	def __init__(self):
		self.tr=TorRequest(password='M8r0s1N2')
		self.tr.reset_identity()
	def get(self,site):
		header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:25.0) Gecko/20100101 Firefox/29.0'}
		response= self.tr.get(site,headers=header)
		return(response)
	

class Get_jobs:
	def __init__(self,site):
		self.site = site
		self.Page()

	def Page(self):

		self.pageno=1
		self.links = {}

		while True:
			site=self.site.rsplit('/',1)[0]
			self.site=(f'{site}/pg{self.pageno}')
			page=self.Parse(self.site)
			if page != False:
				pass
			elif page == False:
				break;
			self.pageno+=1

	def Parse(self,page):
		proxy = Proxy()
		resp = proxy.get(page)
		resp = BeautifulSoup(resp.text, 'html5lib')
		links = [(x.text.rstrip(),''.join(['https://rabota.ua',x['href']])) for x in resp.find_all(href=re.compile('(^/company)(\d)*(/vacancy)'))]
		if all (x[0] in self.links for x in links):
			return(False)
		if len(links) > 0:
			for item in links:
				self.links[item[0]]=item[1]
		else:
			return(False)

class Get_application(Get_jobs):
	def __init__(self,site):
		super().__init__(site)
		self.jobs = {}
	def applications(self,db,exceptions):
		db_links = [x[0] for x in db.execute('select link from jobs')]
		proxy = Proxy() 
		for job,link in self.links.items():
			app=proxy.get(link)
			app = BeautifulSoup(app.text, 'html5lib')
			try:
				ignore = False
				words = job.split(' ')
				for word in words:
					if word.lower() in exceptions:
						ignore = True
				if ignore == False:
					link = ''.join([link,'?mode=apply#apply'])
				if link not in db_links and ignore == False:
					self.jobs[job]=link
				elif link in db_links:
					pass
				elif ignore == True:
					pass
			except:
				print('Error',job,link,sep='|')
		return(self.jobs)

class Apply:
	def __init__(self,url):
		self.driver = webdriver.Firefox()
		self.driver.implicitly_wait(30)
		self.driver.maximize_window()
		self.login(url,'mjbosher@yahoo.co.uk','249smuss')
	def Parse_urls():
		pass
	def getPage(self,url,cover):
		
		self.apply(cover)
	def login(self,url,user,passw):
		self.url = url
		self.driver.get(self.url)
		login = self.driver.find_element_by_class_name('f-header-menu-list-link-with-border')
		login.click()
		email = self.driver.find_element_by_id('ctl00_Sidebar_login_txbLogin')
		email.send_keys(user)
		password = self.driver.find_element_by_id('ctl00_Sidebar_login_txbPassword')
		password.send_keys(passw)
		submit = self.driver.find_element_by_id('ctl00_Sidebar_login_lnkLogin')
		submit.click()
	def apply(self,url,cover):
		
		self.url = url
		self.driver.get(self.url)
		load = False
		while load == False:
			if load == True:
				break;
			try:	
				open_cover_letter = self.driver.find_element_by_css_selector('span.f-text-dark-bluegray')
				open_cover_letter.location_once_scrolled_into_view
				open_cover_letter.click()				
				load =True
			except:
				continue
		
		cover_letter = self.driver.find_element_by_name("ctl00$content$ngElementWrapper$vacancyApplyForm$txAreaGreeting")

		cover_letter.send_keys(cover)
		try:
			lang =self.driver.find_element_by_name("ctl00$content$ngElementWrapper$vacancyApplyForm$applyControlQuestion$rptLanguages$ctl00$ddlSkills")
			lang.click()
			lang = Select(lang)
			lang.select_by_index(8)
		except:
			pass
		submit = self.driver.find_element_by_id("ctl00_content_ngElementWrapper_vacancyApplyForm_hpLnkSendResumeToEmployer")
		submit.click()
		self.driver.implicitly_wait(30)
	def Quit(self):
		pass
		self.driver.quit()

class New:
	def job(search,cover,exceptions,check=False):
		db = 'jobs.db'
		db = sql.connect(db)
		try:
			maxid = max([int(x[0]) for x in db.execute('select id from jobs')])+1
		except:
			maxid=1

		apps=Get_application(search)
		apps=apps.applications(db,exceptions)
		if check == True:
			for job,link in apps.items():
				print(job,link,sep='|')
		elif check == False:
			jobs=Apply("https://www.rabota.ua")
			for job,link in apps.items():
				jobs.apply(link,cover)
				db.execute(f"insert into jobs values ({maxid},'{job}','{link}',datetime('now'))")
				db.commit()
				maxid = maxid+1
			jobs.Quit()

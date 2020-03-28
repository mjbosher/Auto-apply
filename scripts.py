import re
from bs4 import BeautifulSoup
from torrequest import TorRequest
from fake_useragent import UserAgent
import pandas as pd
import os

class Countries:
	'''
	GETS LINKS FOR INDEED.COM FOR EACH COMPANY, WRITE TO CSV OR RETURN DATA FRAME'''
	def __init__(self,site):
		self.tr=TorRequest(password='249smuss')
		self.tr.reset_identity()
		header = {'User-Agent':UserAgent().firefox}
		self.response= self.tr.get(site,headers=header)
		self.response = BeautifulSoup(self.response.text, 'html5lib')

	def getLink(self,write='no'):
		links=[x.next_element.next_element for x in self.response.find_all(src=re.compile('(/images/flags/)+(...png)+'))]
		links = [(x.text,'/'.join([x['href'],'jobs?q=(JOB)&l=(CITY)'])) for x in links if x.text != 'United States']
		links.append(('United States','https://www.indeed.com/jobs?q=(JOB)&l=(CITY)'))
		links = pd.DataFrame(links,columns=['Country','Link'])
		if write.lower() == 'yes':
			links.to_csv('Countries.csv')
			return(None)
		else:
			return(links)

class Load_Data:
	def __init__(self):
		self.countries = 'Countries.csv'
	def Load_Countries(self):
		if os.path.exists(self.countries):
			self.countries = pd.read_csv(self.countries)			
		elif not os.path.exists(self.countries):
			'''if true, need to show a message to show progress'''
			Countries('https://www.indeed.com/worldwide?&mobRdr=1').getLink('yes')
			self.countries = pd.read_csv(self.countries)
		return(self.countries)

class Entry:
	def __init__(self,file):
		self.file = file
		if not os.path.exists(self.file):
			self.entries = pd.DataFrame(columns=['job','country','city','cover','exceptions','cv'])
		elif os.path.exists(self.file):
			self.entries = pd.read_csv(self.file,usecols=[1,2,3,4,5,6])
	def __append__(self,data):
		self.entries.loc[len(self.entries)] = data
	def __read__(self):
		return(self.entries)
	def __drop__(self,TakeAt):
		if len(self.entries) != 1:
			self.entries.drop(self.entries.index[TakeAt],inplace=True)
			self.entries.reset_index(drop=True, inplace=True)
		elif len(self.entries) == 1:
			return("Can't delete the last item")
	def __write__(self):
		if os.path.exists(self.file):
			os.remove(self.file)
		self.entries.to_csv(self.file)
	def __delete__(self):
		if os.path.exists(self.file) and self.file == 'entries.csv':
			os.remove(self.file)
	def __getline__(self,line):
		return(self.entries.loc[line])
	def __setattr__(self,prop,val,read=True):
		super().__setattr__(prop,val)
		if prop == 'self.file':
			self.file = val
			if read == True:
				self.entries = pd.read_csv(self.file)


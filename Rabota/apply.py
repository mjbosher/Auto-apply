from Jobs import New


python_cover='''To whom it may concern,

I am a British citizen, currently living in Ukraine and have a Ukrainian temporary residency, giving me perm
ission to work.

So, I have all the paperwork already complete and can legally work here

I am a self taught Python Developer, looking for a junior position. I have no commercial experience but I ha
ve been training with a company in Kyiv to work with face detection and neural networks.

I am very competent at python and linux. I spend most of my time automating my linux machine and mundane tasks such as applying for jobs.
For example, I have applied for this job by using python to scrape rabota, and parse the results to find relevant matches and then store them in a database before automating the application with selenium.

I have a thirst for knowledge and would love to get the chance to be part of a team where I can develop my python skills and linux knowledge
Please find my CV attached.

Please find my CV attached.

Best regards,

Michael Bosher'''
python_exceptions=['senior','middle','lead','middle/senior','flask','golang','c++','mathematician','senior/lead','manager']

python_junior_search='https://rabota.ua/zapros/python-junior/киев/pg1'
python_dev_search='https://rabota.ua/zapros/python-developer/киев/pg1'
python_search='https://rabota.ua/zapros/python/киев/pg1'
python_intern_search='https://rabota.ua/zapros/python-intern/киев/pg1'
python_junior=New.job(python_junior_search,python_cover,python_exceptions)
python_dev=New.job(python_dev_search,python_cover,python_exceptions)
python=New.job(python_search,python_cover,python_exceptions)
python_intern=New.job(python_intern_search,python_cover,python_exceptions)

data_exceptions = ['lead','senior','head','middle','senior/lead']
data_cover = '''To whom it may concern,

I am a British citizen, currently living in Ukraine and have a Ukrainian temporary residency, giving me perm
ission to work.

So, I have all the paperwork already complete and can legally work here

I am a self taught Python Developer, looking for a junior position. I have no commercial experience but I ha
ve been training with a company in Kyiv to work with face detection and neural networks.

I am deeply interested in data scientist and analysis as data has always intrigued me and I am obsessed by statistics and automation.

For example, I have applied for this job by using python to scrape rabota, and parse the results to find relevant matches and then store them in a database before automating the application with selenium.
Please find my CV attached.

I am competent in Pandas, matplotlib, numpy and many more python modules.

Best regards,

Michael Bosher'''
data_junior_search='https://rabota.ua/zapros/junior-data-scientist/киев/pg1'
data_scientist_search='https://rabota.ua/zapros/data-scientist/киев/pg1'
data_junior=New.job(data_junior_search,data_cover,data_exceptions)
data_scientist=New.job(data_scientist_search,data_cover,data_exceptions)
qa_cover='''To whom it may concern,

I am a British citizen, currently living in Ukraine and have a Ukrainian temporary residency, giving me perm
ission to work.

So, I have all the paperwork already complete and can legally work here

I am a self taught Python Developer, looking for a junior position. I have no commercial experience but I ha
ve been training with a company in Kyiv to work with face detection and neural networks.

I am very competent at python and linux. I spend most of my time automating my linux machine and mundane tasks such as applying for jobs.
For example, I have applied for this job by using python to scrape rabota, and parse the results to find relevant matches and then store them in a database before automating the application with selenium.

I have a thirst for knowledge and would love to get the chance to be part of a team where I can develop my python skills and linux knowledge
Please find my CV attached.

Best regards,

Michael Bosher'''
qa_exceptions=['senior','middle','middle/senior','lead','senior/lead','junior/middle','junior/pre-middle','strong','manager','bss','junior+/middle']
qa_search='https://rabota.ua/zapros/qa/киев/pg1'
qa=New.job(qa_search,qa_cover,qa_exceptions)
qa_engineer_search='https://rabota.ua/zapros/qa-engineer/киев/pg1'
qa_engineer=New.job(qa_engineer_search,qa_cover,qa_exceptions)
qa_automation_engineer_search='https://rabota.ua/zapros/qa-automation-engineer/киев/pg1'
qa_automation_engineer=New.job(qa_automation_engineer_search,qa_cover,qa_exceptions)
qa_trainee_search='https://rabota.ua/zapros/qa-trainee/киев/pg1'
qa_trainee=New.job(qa_trainee_search,qa_cover,qa_exceptions)
junior_qa_engineer_search='https://rabota.ua/zapros/junior-qa-engineer/киев/pg1'
junior_qa_engineer=New.job(junior_qa_engineer_search,qa_cover,qa_exceptions)
junior_qa_automation_engineer_search='https://rabota.ua/zapros/junior-qa-automation-engineer/киев/pg1'
junior_qa_automation_engineer=New.job(junior_qa_automation_engineer_search,qa_cover,qa_exceptions)

dev_exceptions=[]
dev_cover='''To whom it may concern,

I am a British citizen, currently living in Ukraine and have a Ukrainian temporary residency, giving me perm
ission to work.

So, I have all the paperwork already complete and can legally work here

I am a self taught Python Developer, looking for a junior position. I have no commercial experience but I ha
ve been training with a company in Kyiv to work with face detection and neural networks.

I am very competent at python and linux. I spend most of my time automating my linux machine and mundane tasks such as applying for jobs.
For example, I have applied for this job by using python to scrape rabota, and parse the results to find relevant matches and then store them in a database before automating the application with selenium.
I have a thirst for knowledge and would love to get the chance to be part of a team where I can develop my python skills and linux knowledge
Please find my CV attached.

Best regards,

Michael Bosher'''
devops_search='https://rabota.ua/zapros/devops/киев/pg1'
devops=New.job(devops_search,dev_cover,qa_exceptions)
devops_engineer_search='https://rabota.ua/zapros/devops-engineer/киев/pg1'
devops_engineer=New.job(devops_engineer_search,dev_cover,qa_exceptions)
devops_junior_search='https://rabota.ua/zapros/junior-devops-engineer/киев/pg1'
devops_junior=New.job(devops_junior_search,dev_cover,qa_exceptions)

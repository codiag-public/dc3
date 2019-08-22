import requests, json, datetime
from collections import OrderedDict
from bs4 import BeautifulSoup

VERSION = "1.0"

def retrievePage(url, diagnosis, id):
	case = OrderedDict()

	page = requests.get(url)
	encoding = page.encoding if 'charset' in page.headers.get('content-type', '').lower() else None
	soup = BeautifulSoup(page.content, "html.parser", from_encoding=encoding)

	case["case-id"] = id
	case["title"] = soup.find_all('h1')[0].get_text()
	case["diagnosis"] = diagnosis

	narrative = soup.find_all('p', class_='f-body')

	if len(narrative) < 3:
		body = soup.find_all('div', class_='body-text')[0]
		narrative = body.find_all('p')

	notes = []
	noteid = 1
	for n in narrative:
		for e in n.find_all("em"):
			e.decompose()
		for e in n.find_all("span"):
			e.decompose()
		if n.get_text().startswith(":"):
			n.string = n.get_text()[1:]
		if  (len(n.get_text()) > 5) and (not "What is the diagnosis" in n.get_text()) and (not "Polling and commenting" in n.get_text()) and (not "Sign up for the" in n.get_text() and (not "Cast your vote" in n.get_text())):
			note = OrderedDict()
			note["note-id"] = noteid
			note["content"] = n.get_text().strip()
			notes.append(note)
			noteid += 1

	case["notes"] = notes
	return case

def retrieveAll():
	dc3 = OrderedDict()
	dc3["version"] = VERSION
	dc3["download-date"] = datetime.datetime.now().strftime("%Y-%m-%d")
	cases = []
	f = open("cases.url", "r")
	caseid = 1
	for line in f:
		print("Retrieving Case "+str(caseid)+".")
		cases.append(retrievePage(line.strip(), "Headache", caseid))
		caseid += 1
	f.close()
	dc3["cases"] = cases

	o = open("dc3.json", "w")
	o.write(json.dumps(dc3, indent=4, sort_keys=False))
	o.close()

retrieveAll()

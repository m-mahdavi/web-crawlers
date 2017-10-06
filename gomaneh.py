##########################################################
# A Web Crawler for gomaneh.com
# Mohammad Mahdavi
# moh.mahdavi.l@gmail.com
# June 2016
# All Rights Reserved
##########################################################


##########################################################
import os
import codecs
import requests
import bs4
##########################################################


##########################################################
URL_PREFIX = "http://www.gomaneh.com/"
MIN_DOCUMENT_SIZE = 1000
LAST_PAGE_NUMBER = 5300
DOCUMENT_SET_FOLDER = "document-set"
if not os.path.exists(DOCUMENT_SET_FOLDER):
	os.mkdir(DOCUMENT_SET_FOLDER)
##########################################################


##########################################################
def main():
	for i in range(LAST_PAGE_NUMBER, 1, -1):
		url = URL_PREFIX + str(i) + "/"
		r = requests.get(url, headers={"User-Agent": "Dommy!"}, proxies={"http":"http://127.0.0.1:60073"})
		html = ""
		if r.status_code == 200:
			html = r.text
		parsed_html = bs4.BeautifulSoup(html)
		title_list = parsed_html.select("div.post-inner h1")
		title = ""
		if title_list:
			title = title_list[0].text
		text_list = parsed_html.select("div.entry p")
		text_list = [x.text for x in text_list]
		text = "\n".join(text_list)
		if len(title + text) > MIN_DOCUMENT_SIZE:
			f = codecs.open(DOCUMENT_SET_FOLDER + "/" + str(i) + ".xml", "w", encoding="utf-8")
			f.write("<document>\n")
			f.write("<title>\n")
			f.write(title)
			f.write("\n</title>\n")
			f.write("<text>\n")
			f.write(text)
			f.write("\n</text>\n")
			f.write("</document>")
		print "Document Number " + str(i) + " Downloaded."
##########################################################


##########################################################
if __name__ == "__main__":
	main()
##########################################################
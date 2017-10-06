##########################################################
# A Web Crawler for maktabkhooneh.org
# Mohammad Mahdavi
# moh.mahdavi.l@gmail.com
# June 2016
# All Rights Reserved
##########################################################


##########################################################
import urllib2
import bs4
import wget
##########################################################


##########################################################
URL_COUNT = 10
URL_PREFIX = "http://maktabkhooneh.org/video/ekhtiari419-"
##########################################################


##########################################################
def main()
	for i in range(1, URL_COUNT):
		url = URL_PREFIX + str(i)
		html = urllib2.urlopen(url).read()
		parsed_html = bs4.BeautifulSoup(html)
		video_url = parsed_html.select("a.hq-video-dl")[0]["href"]
		wget.download(video_url)
##########################################################


##########################################################
if __name__ == "__main__":
	main()
##########################################################
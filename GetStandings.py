#!/usr/bin/env python
import urllib2, time

myTime = str((time.strftime("%m/%d/%Y")) + " at " + time.strftime("%I:%M %p"))

gaScript = """<script>
  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

  ga('create', 'UA-45186467-1', 'cartolabs.com');
  ga('send', 'pageview');

</script>"""

scoreString = """<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd"><html> <head> <meta http-equiv="content-type" content="text/html; charset=utf-8" />  <title>Startup MD Tally</title> <link rel="stylesheet" type="text/css" href="http://ajax.aspnetcdn.com/ajax/jquery.dataTables/1.9.1/css/jquery.dataTables.css"> <script type="text/javascript" charset="utf8" src="http://ajax.aspnetcdn.com/ajax/jQuery/jquery-1.7.1.min.js"></script> <script type="text/javascript" charset="utf8" src="http://ajax.aspnetcdn.com/ajax/jquery.dataTables/1.9.1/jquery.dataTables.min.js"></script> <script type="text/javascript" charset="utf8">  $(document).ready(function(){  $('#example').dataTable({"aaSorting": [[ 1, "asc" ],[2, "desc"]],"iDisplayLength": -1});  }); </script>""" + gaScript + """ <style>.dataTables_length{visibility: hidden;}</style></head> <body> This site was created by <a href='http://CartoLabs.com' target='_blank'>CartoLabs</a> to quickly compare Likes and View Counts for each video and stop.</br> You can sort by one column (or multiple columns by holding the shift key).</br>Last updated at:  <b>""" + myTime + """</b>, and is updated every thirty minutes.<div class="container">  <table cellpadding="0" cellspacing="0" border="0" class="dataTable" id="example"> <thead> <tr><th>Video Title</th><th>Stop Name</th><th>Likes</th><th>Views</th></tr></thead><tbody>"""

playlistArray = (("PLBN03TRv8YYdSElLZwRlxWXseYyAiHNOO","Ubalt"),\
					("PLBN03TRv8YYd_gFUeOLYg4d0kPBi1EGhE","Gov Fest"),\
					("PLBN03TRv8YYdxGqSqa8L-jPrQmRiNrshp","Innovation Celebration"),\
					("PLBN03TRv8YYdzCiK9N5W3W0hY1_eZDJH2","TEDCO"),\
					("PLBN03TRv8YYc9ewUF0i6YpDRg7VJl-sq_","TCS PRS"),\
					("PLBN03TRv8YYfZauU7DiUAYOvKpAHFW-Td","LSA"),\
					("PLBN03TRv8YYdC2nWciVWL5tCLm1QQuEDb","Havre de Grace"),\
					("PLBN03TRv8YYdmR7Vxe5biaLmRX6tXuMB2","Frederick"),\
					("PLBN03TRv8YYdbJz_h5VYkJDTZg6T9fKPw","Bethesda"),\
					("PLBN03TRv8YYc5_SxjHTydYOqJmtO6U6ob","Garrett County"),\
					("PLBN03TRv8YYfmD1OygCzflT8gU1m59bVE","Founder Corps"),\
					("PLBN03TRv8YYdIWWsaxn4PEqNuNJZHqbrB","CoFounders Lab"),\
					("PLBN03TRv8YYc-BB02cv1cShpfVJQuXFd-","Hagerstown"),\
					("PLBN03TRv8YYfomGTMETwHYDkbbhKFeLt1","Betamore"),\
					("PLBN03TRv8YYf-Ix-vl9CeZZHrS2aAX31H","MCE"),\
					("PLBN03TRv8YYf7Ei7PU6r-YnpAQlDNBfbe","Annapolis"),\
					("PLBN03TRv8YYdmQwG9cdcBsVXXo2AwpDC7","Howard Community College"),\
					("PLBN03TRv8YYcxIEBqDLFZZISjr3G08end","Washington College"),\
					("PLBN03TRv8YYdDqZIUTCxJVu27Zgh8cqKB","Salisbury"),\
					("PLBN03TRv8YYeMPddEmrFE-zxWcdM2GAdi","Easton"),\
					("PLBN03TRv8YYfbbzRAARYUu_awnvkK8FEw","Ocean City"))

for urlItem in playlistArray:
	for line in urllib2.urlopen(r'http://www.youtube.com/playlist?list=' + str(urlItem[0])).readlines():
		if '&amp;list=' + str(urlItem[0]) + '&amp;' in line and r'ux-thumb-wrap' not in line:
			try:
				vidURL = line.split('" title="')[0].strip('<a href="')
				vidTitle = line.split('" title="')[1].split('" class="yt-uix-sessionlink')[0]
				vidTitle = vidTitle.replace(",","")
				vidStop = str(urlItem[1])
				for moreinfo in urllib2.urlopen(r'http://www.youtube.com' + vidURL).readlines():
					if r'  <span class="likes-count">' in moreinfo:
						vidLikes = moreinfo.strip('<span class="likes-count">').strip('</span>\n')
					if 'views\n' in moreinfo:
						vidViews = moreinfo.strip('views\n').strip().replace("+","")
				scoreString = scoreString + "<tr><td><a href='http://www.youtube.com" + vidURL + "' target='_blank'>" + vidTitle + "</a></td><td>" + vidStop + "</td><td>" + vidLikes + "</td><td>" + vidViews + "</td></tr>"
			except:
				pass

outFile = open("index.html","w")

outFile.write(scoreString + "	</tbody></table></div></body></html>")

outFile.close()

#return scoreString

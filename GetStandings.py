import urllib2, time

myTime = str((time.strftime("%m/%d/%Y")) + " at " + time.strftime("%I:%M %p"))

scoreString = """<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd"><html> <head> <meta http-equiv="content-type" content="text/html; charset=utf-8" />  <title>Startup MD Tally</title> <link rel="stylesheet" type="text/css" href="http://ajax.aspnetcdn.com/ajax/jquery.dataTables/1.9.1/css/jquery.dataTables.css"> <script type="text/javascript" charset="utf8" src="http://ajax.aspnetcdn.com/ajax/jQuery/jquery-1.7.1.min.js"></script> <script type="text/javascript" charset="utf8" src="http://ajax.aspnetcdn.com/ajax/jquery.dataTables/1.9.1/jquery.dataTables.min.js"></script> <script type="text/javascript" charset="utf8">  $(document).ready(function(){  $('#example').dataTable({"iDisplayLength": -1});  }); </script> <style>.dataTables_length{visibility: hidden;}</style></head> <body> Last updated at:  """ + myTime + """<div class="container">  <table cellpadding="0" cellspacing="0" border="0" class="dataTable" id="example"> <thead> <tr><th>Video Title</th><th>Likes</th><th>Views</th></tr></thead><tbody>"""

playlistArray = ("PLBN03TRv8YYdSElLZwRlxWXseYyAiHNOO",\
					"PLBN03TRv8YYd_gFUeOLYg4d0kPBi1EGhE",\
					"PLBN03TRv8YYdxGqSqa8L-jPrQmRiNrshp",\
					"PLBN03TRv8YYdzCiK9N5W3W0hY1_eZDJH2",\
					"PLBN03TRv8YYc9ewUF0i6YpDRg7VJl-sq_",\
					"PLBN03TRv8YYfZauU7DiUAYOvKpAHFW-Td",\
					"PLBN03TRv8YYdC2nWciVWL5tCLm1QQuEDb",\
					"PLBN03TRv8YYdmR7Vxe5biaLmRX6tXuMB2",\
					"PLBN03TRv8YYdbJz_h5VYkJDTZg6T9fKPw",\
					"PLBN03TRv8YYc5_SxjHTydYOqJmtO6U6ob",\
					"PLBN03TRv8YYfmD1OygCzflT8gU1m59bVE",\
					"PLBN03TRv8YYdIWWsaxn4PEqNuNJZHqbrB",\
					"PLBN03TRv8YYc-BB02cv1cShpfVJQuXFd-",\
					"PLBN03TRv8YYfomGTMETwHYDkbbhKFeLt1",\
					"PLBN03TRv8YYf-Ix-vl9CeZZHrS2aAX31H",\
					"PLBN03TRv8YYf7Ei7PU6r-YnpAQlDNBfbe",\
					"PLBN03TRv8YYdmQwG9cdcBsVXXo2AwpDC7",\
					"PLBN03TRv8YYcxIEBqDLFZZISjr3G08end",\
					"PLBN03TRv8YYdDqZIUTCxJVu27Zgh8cqKB",\
					"PLBN03TRv8YYeMPddEmrFE-zxWcdM2GAd",\
					"PLBN03TRv8YYfbbzRAARYUu_awnvkK8FEw")

for urlItem in playlistArray:
	for line in urllib2.urlopen(r'http://www.youtube.com/playlist?list=' + urlItem).readlines():
		if '&amp;list=' + urlItem + '&amp;' in line and r'ux-thumb-wrap' not in line:
			try:
				vidURL = line.split('" title="')[0].strip('<a href="')
				vidTitle = line.split('" title="')[1].split('" class="yt-uix-sessionlink')[0]
				vidTitle = vidTitle.replace(",","")
				for moreinfo in urllib2.urlopen(r'http://www.youtube.com' + vidURL).readlines():
					if r'  <span class="likes-count">' in moreinfo:
						vidLikes = moreinfo.strip('<span class="likes-count">').strip('</span>\n')
					if 'views\n' in moreinfo:
						vidViews = moreinfo.strip('views\n').strip().replace("+","")
				scoreString = scoreString + "<tr><td>" + vidTitle + "</td><td>" + vidLikes + "</td><td>" + vidViews + "</td></tr>"
			except:
				pass

outFile = open("index.html","w")

outFile.write(scoreString + "	</tbody></table></div></body></html>")

outFile.close()

#return scoreString
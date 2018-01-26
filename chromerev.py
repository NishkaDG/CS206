def prettyPrinter(member,f, depth):
	if member[2]=='url':
		f.write((depth*'\t')+'<DT><A HREF="'+member[-1]+'" ADD_DATE="'+member[5]+'">'+member[3]+'</A>\n')
	elif member[2]=='folder':
		global c
		a=[]
		for each in c:
			if (each[1]==member[4]):
				a.append(each)
		b=[]
		for each in c:
			if each not in a:
				b.append(each)
		c=b
		f.write((depth*'\t')+'<DT><H3 ADD_DATE="'+member[5]+'" LAST_MODIFIED="'+member[6]+'">'+member[3]+'</H3>\n')
		f.write((depth*'\t')+'<DL><p>\n')
		for each in a:
			prettyPrinter(each, f, (depth+1))
		f.write((depth*'\t')+'</DL><p>\n')
f=open('bookmarks.csv','r')
k= f.readlines()
f.close()
topMessage='<!DOCTYPE NETSCAPE-Bookmark-file-1>\n<!-- This is an automatically generated file.\n\tIt will be read and overwritten.\n\tDO NOT EDIT! --> \n<META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=UTF-8">\n<TITLE>Bookmarks</TITLE>\n<H1>Bookmarks</H1>\n'
f=open('bookmarks.html', 'w')
f.write(topMessage)
c=[]
d=[]
for each in k:
	c.append((each[:-1]).split(','))
	d.append((each[:-1]).split(','))
LAST_MODIFIED=0
for each in c:
	if each[6]> LAST_MODIFIED:
		LAST_MODIFIED= each[6]
ADD_DATE=LAST_MODIFIED
for each in c:
	if each[5] < ADD_DATE:
		ADD_DATE= each[5]
f.write('<DL><p>\n\t<DT><H3 ADD_DATE="'+ADD_DATE+ '" LAST_MODIFIED="'+ LAST_MODIFIED +'" PERSONAL_TOOLBAR_FOLDER="true">Bookmarks bar</H3>\n\t<DL><p>\n')
for each in d:
	if (each[1]=='1') and (each[2]=='url'):
		prettyPrinter(each, f, 2)
for each in d:
	if (each[1]=='1') and (each[2]=='folder'):
		prettyPrinter(each, f, 2)
f.write('\t</DL><p>\n')
for each in d:
	if (each[1]=='2') and (each[2]=='url'):
		prettyPrinter(each, f, 1)
for each in d:
	if (each[1]=='2') and (each[2]=='folder'):
		prettyPrinter(each, f, 1)
for each in d:
	if (each[1]=='3') and (each[2]=='url'):
		prettyPrinter(each, f, 1)
for each in d:
	if (each[1]=='3') and (each[2]=='folder'):
		prettyPrinter(each, f, 1)
f.write('</DL><p>')
f.close()

import sqlite3
import unicodedata

def fromsql(fname):
    destination = open("bookmarks.csv", 'a')
    conn = sqlite3.connect(fname)
    db = dict()
    cursor = conn.execute("SELECT moz_bookmarks.parent, moz_bookmarks.type, moz_bookmarks.title, moz_bookmarks.id, moz_bookmarks.dateAdded, moz_bookmarks.lastModified, moz_places.url FROM moz_bookmarks, moz_places WHERE moz_bookmarks.fk = moz_places.id AND moz_bookmarks.type = 1 AND moz_bookmarks.title != '(NULL)'")
    getparent = conn.execute("SELECT id, title, parent, dateAdded, lastModified FROM moz_bookmarks WHERE type = 2")
    for item in getparent:
        db[item[0]] = item[1]
    getparent = conn.execute("SELECT id, title, parent, dateAdded, lastModified FROM moz_bookmarks WHERE type = 2 AND parent!=4")
    for item in getparent:
        parentid = item[2]
        #print(item[1])
        #print(parentid)
        parent = ""
        #print(parentid)
        try:
            parent = db[parentid]
        except KeyError:
            parent = ""
        #print(parent)
        destination.write(parent+","+str(parentid)+","+"folder,"+item[1]+","+str(item[0])+","+str(item[3])+","+str(item[4])+",NA")
        destination.write("\n")
    line = ""
    for row in cursor:
        line = ""
        parentid = row[0]
        parent = db[parentid]
        #print(parent)
        if(parent!=""):
            line = line + parent+","+str(parentid)+","+"url,"
        else:
            line = line + " "+","+str(parentid)+",url,"
        #print(row)
        destination.write(line)
        for entry in row[2:6]:
            output = ""
            if isinstance(entry, str):
                entry = entry.replace(","," ")
            try:
                output = str(entry)
                destination.write(output+",")
            except UnicodeEncodeError:
                output = unicodedata.normalize('NFD', line).encode('ascii', 'ignore')
                output = output.decode('ascii')
                destination.write(output)
                destination.write(",")
        destination.write(row[6])
        destination.write("\n")
            
    destination.close()
    conn.close()

fromsql("places.sqlite")

import zipfile
z = zipfile.ZipFile(r'/Users/chan/Applications/Dash.zip', "r")
for filename in z.namelist():
    print 'File: ', filename
    bytes = z.read(filename)
    print 'has', len(bytes), 'bytes'

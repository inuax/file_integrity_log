import os, hashlib, time, datetime


# improvise log function
def fim_log(msg):
    f = open('fimlog/fimlog.txt', 'a')
    f.write(msg + '\n')
    f.close()


files = {}
while True:
    for file in os.listdir('.'):
        if os.path.isfile(file):
            hash = hashlib.md5()
            with open(file, 'rb') as f:
                for chunk in iter(lambda: f.read(4096), b""):
                    hash.update(chunk)
                md5 = hash.hexdigest()
            if file in files and md5 != files[file]:
                msg = file + ' has been change at ' + str(datetime.datetime.now())
                print(msg)
                fim_log(msg)

            files[file] = md5
    time.sleep(1)

import id_scraper
import sys
import os

pack_name = input("Pack Name: ")
modfile = input("Path to Modfile: ")
assert os.path.exists(modfile), "ERROR:I did not find the file at, "+str(modfile)
user = input("Steam User: ")
pw = input("Steam Password: ")

f = open(f"modlistUpdater_{pack_name}.txt", "a")
f.write(f"login {user} {pw} \n")
i=0
for id in id_scraper.getIds(modfile):
    i=i+1
    f.write(f"workshop_download_item 107410 {id} \n" )
print (f"FINISHED: added {i} mods to the file.")
f.write("quit")
f.close()
id_scraper.getIds
    
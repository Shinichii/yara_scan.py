import os
import yara
import urllib

#Auteurs :
#Aurelien DENIS <aurelien.denis@efrei.net>
#Marc GAYRAUD <marc.gayraud@efrei.net>
#Vincent LAVERSANNE <vincent.laversanne@esigetel.net>

url = "https://github.com/Yara-Rules/rules/archive/master.zip"
dirToScanPath = "/home/user/Test" # A remplacer par le dossier desire

print('Downloading latest yara signatures....')
urllib.urlretrieve(url, "master.zip")
os.system("unzip master.zip")
print('Done')
print('Loading rules...')
rules = yara.compile("home/user/rules-master/index.yar")# Choisir l emplacement des regles
print('Starting scan in ' + dirToScanPath)

for file in os.listdir(dirToScanPath): #ne fonctionnera pas sur les dossiers
        print(file)
        try:
                     result = rules.match(dirToScanPath+"/"+file)
                 if(result == []):
                       print('Nothing found for this file')
                 else:
                       print(result)
           except:
                     print('Could not open' + file +  'ignoring it' )
print('Scan ended')

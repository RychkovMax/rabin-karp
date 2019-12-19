import logging
import threading #Подключение модуля threading
import time #Подключение модуля time
def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(2)
    logging.info("Thread %s: finishing", name) 
    
    def rk_search(string,pat):
    string = string.upper()
    pat = pat.upper()
    #ASSUMING ALL CHARACTERS ARE UPPPER_CASE,
    #Can be extended for lower case if necessary
    
    l = len(string)
    l_p = len(pat)
    con = 26 #The constant for base system 26
    
     x = threading.Thread(target=thread_function, args=(1,)) #Создается
    x.start()#и запускается поток

    hashval = 0    #For the pattern
    currhash = 0 #For each substring
    for i in range(l_p):
        hashval += (ord(pat[i])-ord('A')+1)*(con**(l_p-i-1))
        currhash += (ord(string[i])-ord('A')+1)*(con**(l_p-i-1)) 
    for ind in range(l-l_p+1):
        if ind!=0:
            currhash = con*(currhash-((ord(string[ind-1])-ord('A')+1)*(con**(l_p-1))))+(ord(string[ind+l_p-1])-ord('A')+1)
  
        if(currhash==hashval):
            print "Found at index",ind
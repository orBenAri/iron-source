# -*- coding: utf-8 -*-
import requests
import time
def main():
 #a = requests.get("https://api.github.com/repos/wequick/Small/stats/participation").json()
 #commits = a['all'][51]
 #print "number of commits in the past week - " + str(commits)
 #b = requests.get("https://api.github.com/repos/wequick/Small/stats/contributors").json()
 #c= b[:-6:-1]
 #print "top 5 conributors:"
 #for key in c:
 #    print key['author']['login']
 pulls = 0
 i = 0
 d = requests.get("https://api.github.com/repos/wequick/Small/pulls?state=all&page=i").json()
 now = time.strftime("%Y,%m")
 t = d[pulls%30]['created_at']
 t = t[0:4]+"," +t[5:7]

 if t==now:
  while now == t:
    pulls+=1
    t = d[pulls%30]['created_at']
    t = t[0:4]+"," +t[5:7]
    if pulls%30==0:
        i+=1
        d = requests.get("https://api.github.com/repos/wequick/Small/pulls?state=all&page=i").json()


if __name__ == '__main__':
    main()

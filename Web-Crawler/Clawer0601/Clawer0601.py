import requests
import BeautifulSoup

url = "http://shlanxin.w152.mc-test.com/"
if __name__ == '__main__':
    r = requests.get(url + "index.html")
    b = BeautifulSoup.BeautifulSoup(r.content)
    for i in b.findAll("tr"):
        for j in i.findAll("th"):
            print j.text+"\t",

        a = i.findAll("a")
        if len(a) > 0:
            h = a[0]['href']
            r = requests.get(url+h)
            br = BeautifulSoup.BeautifulSoup(r.content)
            for k in br.findAll("tr"):
                print k.find("th").text.replace("\n", "").replace("\t", "")+"\t",

            h = a[1]['href']
            r = requests.get(url+h)
            br = BeautifulSoup.BeautifulSoup(r.content)
            for aa in br.findAll("tr"):
                t = aa.find("th")
                if t != None and len(t.text) > 0:
                    print t.text.replace("\n", "").replace("\t", "") +"\t",
                else:
                    print "\t",
        print
import requests, json, os, time, random
from rich.progress import Progress

class Grabber():
    def __init__(self, headers:dict=None):
        self.headers = headers

    def buildUrl(self, baseUrl:str=None, pageNumbers:int=1, pageSep:str='?page='):
        self.pageNumbers = pageNumbers
        self.baseUrl = baseUrl
        self.urls = [baseUrl]
        if pageNumbers < 1:
            return ValueError()
        elif pageNumbers > 1:
            for i in range(1, pageNumbers+1):
                url = f'{self.baseUrl}{pageSep}{i}'
                self.urls.append(url)

    def __initSession(self):
        if self.headers is None:
            self.headers = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:50.0) Gecko/20100101 Firefox/50.0',
                'Accept-Language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7'
                }
        self.session = requests.Session()
        self.session.headers.update(self.headers)

    def run(self):
        pbar = Progress()
        self.__initSession()
        self.htmls = {}
        self.requests = {}
        pbar.start()
        task = pbar.add_task("[green]Processing...", total=self.pageNumbers)
        for urlnum, url in enumerate(self.urls, start=1):
            index = f'page{urlnum}'
            try:
                r = self.session.get(url)
                self.requests[index] = r
                if r.status_code == 200:
                    self.htmls[index] = r.text
            except:
                pass
            finally:
                time.sleep(random.uniform(3, 6))
                pbar.update(task, advance=1)
        pbar.stop()

    def exportHtml(self, filename:str):
        dir = os.path.split(filename)[0]
        if dir != '': 
            os.makedirs(dir, exist_ok=True)
        with open(filename, 'w') as f:
            json.dump(self.htmls, f, indent=4)
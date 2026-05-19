class Page:
    def __init__(self, page: str):
        self.url = page
        self.back = None
        self.forward = None

class BrowserHistory:
    def __init__(self, homepage: str):
        self.curr = Page(homepage)
        
    def visit(self, url: str) -> None:
        page = Page(url)
        self.curr.forward = page
        page.back = self.curr
        self.curr = page

    def back(self, steps: int) -> str:
        while self.curr.back is not None and steps>0:
            self.curr = self.curr.back
            steps-=1
        return self.curr.url        

    def forward(self, steps: int) -> str:
        while self.curr.forward is not None and steps>0:
            self.curr = self.curr.forward
            steps-=1
        return self.curr.url 
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
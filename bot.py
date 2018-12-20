from urllib.parse import urlencode
from urllib.request import urlopen, Request


class Bot:
    base_url = "https://api.telegram.org/bot%s/%s"

    def __init__(self, token):
        self.token = token

    def get_me(self):
        url = self.base_url % (self.token, "getMe")
        res = urlopen(url)
        json = res.read()
        res.close()
        return json

    def send_message(self, chat_id, text):
        url = self.base_url % (self.token, "sendMessage")
        params = urlencode({"chat_id": chat_id, "text": text})     #url encoding string == "chat_id=?&text=?"
        url = url + "?" + params
        req = Request(url)
        req.add_header("charset", "UTF-8")
        req.add_header("Content-Type", "application/json")
        urlopen(req)

    def send_photo(self, chat_id, photo_id, caption):
        url = self.base_url % (self.token, "sendPhoto")
        params  = urlencode({"chat_id" : chat_id, "photo" : photo_id, "caption" : caption, "parse_mode" : "HTML"})
        url = url + "?" + params
        req = Request(url)
        req.add_header("charset", "UTF-8")
        req.add_header("Content-Type", "application/json")
        urlopen(req)

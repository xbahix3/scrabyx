# Scraby-Project

---

# Introduction :

scraby is web scraper that scrapes and parse specific data from response using regex, json to parse it.

# How does it work ? :

Simply it do this steps :

- Make a request using provided url and return response.
- Check if response represents success, fail, custom, ban according to sentence that refers to  and do retry if you need to do.
    - [x]  do retry
- (optional) Parse data, cookies from response.
    - [x]  using regex

see the examples provided (mail access, Mimo, Euler)

---

P.s : Make sure to install :

`pip3 install requests`

`pip3 install pysocks`

## 1. The Basic HTTP GET/response interaction
1. Is your browser running HTTP version 1.0, 1.1, or 2? What version of HTTP is the server running?
```sh
1.1
```

2. What languages (if any) does your browser indicate that it can accept to the server?
```sh
en-us, en 
```

3. What is the IP address of your computer? What is the IP address of the gaia.cs.umass.edu server?
```sh
src: 192.168.31.26 
dst: 128.119.245.12 
```

4. What is the status code returned from the server to your browser?
```sh
200 
```

5. When was the HTML file that you are retrieving last modified at the server?
```sh
Fri, 14 Jun 2024 05:59:02 GMT
```

6. How many bytes of content are being returned to your browser?
```sh
128 bytes 
```

7. By inspecting the raw data in the packet content window, do you see any headers within the data that are not displayed in the packet-listing window? If so, name one.
```sh
No (yeah I don't see any difference fr)
```

## 2. The HTTP Conditional GET/response interaction 
8. Inspect the contents of the first HTTP GET request from your browser to the server. Do you see an “IF-MODIFIED-SINCE” line in the HTTP GET?
```sh
I don't 
```

9. Inspect the contents of the server response. Did the server explicitly return the contents of the file? How can you tell?
```sh
Yes
```

10. Now inspect the contents of the second HTTP GET request from your browser to the server. Do you see an “IF-MODIFIED-SINCE:” line in the HTTP GET6? If so, what information follows the “IF-MODIFIED-SINCE:” header?
```sh
Yes, the date and time being modified? 
If-Modified-Since: Fri, 14 Jun 2024 05:59:02 GMT
```

11. What is the HTTP status code and phrase returned from the server in response to this second HTTP GET? Did the server explicitly return the contents of the file? Explain.
```sh
304 Not Modified 
It did not explicitly return the contents of the file because it's already in the cache. 
```

## 3. Retrieving long documents 
12. How many HTTP GET request messages did your browser send? Which packet number in the trace contains the GET message for the Bill or Rights?
```sh
One. For my 'live' session in Wireshark, it's number 104.
```

13. Which packet number in the trace contains the status code and phrase associated with the response to the HTTP GET request?
```sh
110 
```

14. What is the status code and phrase in the response?
```sh
HTTP/1.1 200 OK (text/html)
```

15. How many data-containing TCP segments were needed to carry the single HTTP response and the text of the Bill of Rights?
```sh
4 where 3 contain a packet with 1506 bytes, and 1 contains 559 bytes. 
```

## 4. HTML Documents with Embedded Objects 
16. How many HTTP GET request messages did your browser send? To which Internet addresses were these GET requests sent?
```sh
3 GET requests messages. 
1. GET /wireshark-labs/HTTP-wireshark-file4.html HTTP/1.1 
2. GET /pearson.png HTTP/1.1 
3. GET /8E_cover_small.jpg HTTP/1.1 
```
17. Can you tell whether your browser downloaded the two images serially, or whether they were downloaded from the two web sites in parallel? Explain.
```sh
The browser downloads in parallel, fetch them simultaenoulsy. 
```

## 5. HTTP Authentication
18. What is the server’s response (status code and phrase) in response to the initial HTTP GET message from your browser?
```sh
771	HTTP/1.1 401 Unauthorized  (text/html)
```

19. When your browser’s sends the HTTP GET message for the second time, what new field is included in the HTTP GET message?
```sh
Basic d2lyZXNoYXJrLXN0dWRlbnRzOm5ldHdvcms=
```
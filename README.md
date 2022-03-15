# tping
							 
tping it's another script on the block for making ping requests through TCP. 
Just specify the host and port and TPING will make requests till you close it. It actually does TCP full scan, so it isn't a tool for stealthy fellows.
Works both on Windows and Linux as long as you have **python** and **pip** installed.   
 
## Getting started

Install requirements with:
```
pip install -r requirements.txt
```

### Syntax
```
python tping.py <IP or hostname> <TCP port>
```
	
### Example
```
python tping.py 8.8.8.8 443
```






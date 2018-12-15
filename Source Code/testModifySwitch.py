import sys

try:
    import urllib.request as urllib2
except ImportError:
    import urllib2


print("Turn on switch.")
response = urllib2.urlopen('http://localhost:8083/ZWaveAPI/Run/devices[2].instances[0].commandClasses[0x25].Set(0)')
# response = urllib2.urlopen('http://localhost:8083/Run/ZWaveAPI/devices[2].instances[0].commandClasses[0x25].Set(255)', data = None)
html = response.read()
print(html)
""" \file utils.py
\brief Utility functions to help with windows package management.
"""

import urllib2
import re

def getPage(url):
    """Returns the contents of a url as a string.

    This currently doesn't do anything to handle exceptions.

    \param url The url to grab a page from.
    \return A string containing the page contents of url.
    """
    f=urllib2.urlopen(url)
    page = f.read()
    f.close()
    return page

def scrapePage(reg, url, pos=0):
    """Scrapes the page from url for the reg at position pos.

    This will return the pos'th match of the regular expression reg from the
    page at url. pos defaults to 0.

    \param reg The regular expression to match.
    \param url The page to scrape.
    \param pos Which regulare expression match to return, defaults to 0.
    \return The pos'th reg match on the page at url.
    """
    return re.findall(reg, getPage(url))[pos]

def scrapePageDict(d):
    """Scrapes the page from d['url'] for the d['reg'] at position d['pos'].

    This will return the d['pos']'th match of the regular expression d['reg']
    from the page at d['url'].

    \param d A dictionary that contains 'reg' The regular expression to match.
    'url' The page to scrape.
    'pos' Which regulare expression match to return, defaults to 0.
    \return The pos'th reg match on the page at url.
    """
    return re.findall(d['reg'], getPage(d['url']))[d['pos']]

def getWebVersion(d):
    """Get the version from the web of the catalog entry in d

    Use the page at the url specified in d['version']['url'], and the regular
    expression specified in d['version']['reg'] to find the latest version
    number of the passed package. The d['version']['pos']'th match of the
    regular expression is returned.

    \param d The dictionary entry for a package, containing at least an entry
    for 'version' that is a dictionary that contains a 'url', 'reg', and 'pos'
    \return the version number matched by the regular expression and page
    passed in.
    """
    return scrapePageDict(d['version'])

def getDownloadURL(d):
    """Get the DownloadURL from the web of the catalog entry in d

    Use the page at the url specified in d['download']['url'], and the regular
    expression specified in d['download']['reg'] to find the download url of
    the latest version of the passed package. The d['download']['pos']'th match
    of the regular expression is returned.

    \param d The dictionary entry for a package, containing at least an entry
    for 'download' that is a dictionary that contains a 'url', 'reg' and 'pos'
    \return the download url matched by the regular expression and page passed
    in.
    """
    downurl = scrapePageDict(d['download'])
    fredirectedurl = urllib2.urlopen(downurl)
    redirectedurl = fredirectedurl .geturl()
    fredirectedurl .close()
    return redirectedurl

def downloadLatest(d, location='downloads\\'):
    """Download the latest version of the package d.

    Use the information specified in the package d to download the latest
    version of the package from the web. The default download location is
    './downloads'

    \param d The dictionary entry for a package, containing at least a 'name', 
    as well as a 'version', and 'download' dict containing 'url', 'reg', and
    'pos'.
    \return the path to the downloaded file.
    """
    name = d['name']
    version = getWebVersion(d)
    furl = urllib2.urlopen(getDownloadURL(d))
    filecontents = furl.read()
    furl.close()
    parsed=urllib2.urlparse.urlparse(furl.geturl())
    pathname = urllib2.url2pathname(parsed.path)
    filename = pathname.split("\\")[-1]
    newfileloc = location + name + '---' + version + '---' + filename
    with open(newfileloc, "wb") as f:
        f.write(filecontents)
    return newfileloc

def getInstalledVersion(d):
    return 0

def installLatest(d, location='downloads\\'):
    return 0

def uninstall(d):
    return 0

def upgrade(d):
    return 0

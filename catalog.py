name = 'name'
url = 'url'
reg = 'reg'
version = 'version'
download = 'download'
pos = 'pos'
silentflags = 'silentflags'
installversion = 'installversion'
key = 'key'
subkey = 'subkey'
value = 'value'
querytype = "querytype"

catalog={"Firefox":{name:'Firefox',
          url:'http://www.mozilla.org/en-US/firefox/new/',
          version:{url:'http://www.mozilla.org/en-US/firefox/new/',
            reg:'<li><a href="http://download\.mozilla\.org/\?product=firefox-([0-9]+(?:\.[0-9]+)+)&amp;os=win&amp;lang=en-US">Windows</a></li>',
            pos:0},
          download:{url:'http://www.mozilla.org/en-US/firefox/new/',
            reg:'<li><a href="(http://download\.mozilla\.org/\?product=firefox-[0-9]+(?:\.[0-9]+)+&amp;os=win&amp;lang=en-US)">Windows</a></li>',
            pos:0},
          silentflags:" -ms",
          installversion:{querytype:"reg",
            key:'HKLM',
            subkey:'SOFTWARE\Mozilla\Mozilla Firefox',
            value:'CurrentVersion'}
          }}

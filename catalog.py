name = 'name'
category = 'category'
description = 'description'
url = 'url'
regex = 'regex'
version = 'version'
download = 'download'
regexpos = 'regexpos'
silentflags = 'silentflags'
installversion = 'installversion'
key = 'key'
subkey = 'subkey'
value = 'value'
querytype = "querytype"

catalog={
    'EMPTY':{
        name:'',
        category:'',
        description:'',
        url:'',
        version:{
            url:'',
            regex:'',
            regexpos:0},
        download:{
            url:'',
            regex:'',
            regexpos:0},
        silentflags:'',
        installversion:{
            querytype:'',
            key:'',
            subkey:'',
            value:'',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    '7-Zip':{
        name:'7-Zip',
        category:'Utilities',
        description:'Multiple format file compression and decompression',
        url:'http://7-zip.org',
        version:{
            url:'http://7-zip.org',
            regex:'<P><B>Download 7-Zip ([0-9]+(?:\.[0-9]+)+) \(',
            regexpos:0},
        download:{
            url:'http://7-zip.org',
            regex:'<A href="(.*/sevenzip/7z[0-9]+.exe)',
            regexpos:0},
        silentflags:'/S',
        installversion:{
            querytype:'reg',
            key:'HKLM',
            subkey:'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\7-Zip',
            value:'DisplayName',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'Firefox':{
        name:'Firefox',
        category:'Internet Tools',
        description:'The Mozilla Firefox browser',
        url:'http://www.mozilla.org/en-US/firefox/new/',
        version:{
            url:'http://www.mozilla.org/en-US/firefox/new/',
            regex:'<li><a href="http://download\.mozilla\.org/\?product=firefox-([0-9]+(?:\.[0-9]+)+)&amp;os=win&amp;lang=en-US">Windows</a></li>',
            regexpos:0},
        download:{
            url:'http://www.mozilla.org/en-US/firefox/new/',
            regex:'<li><a href="(http://download\.mozilla\.org/\?product=firefox-[0-9]+(?:\.[0-9]+)+&amp;os=win&amp;lang=en-US)">Windows</a></li>',
            regexpos:0},
        silentflags:'-ms',
        installversion:{
            querytype:'reg',
            key:'HKLM',
            subkey:'SOFTWARE\\Mozilla\\Mozilla Firefox',
            value:'CurrentVersion',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        }
    }

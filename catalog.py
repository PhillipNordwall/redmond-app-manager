name = 'name'
category = 'category'
description = 'description'
url = 'url'
regex = 'regex'
version = 'version'
download = 'download'
downloadtype = 'downloadtype'
regexpos = 'regexpos'
silentflags = 'silentflags'
installversion = 'installversion'
key = 'key'
subkey = 'subkey'
value = 'value'
querytype = "querytype"


#####ROLE YOUR OWN CAPTURING GROUPS
months="Janurary|February|March|April|May|June|July|August|September|October|November|December"
alphabeta="Alpha|Beta|alpha|beta"


#####
minimal_list = [ 'Ghostscript', 'GSview 32bit', 'Gimp', 'ImageMagick',
    '7-Zip', 'Firefox', 'Scribus' ]
broken_localversion_minimal_list = [ 'Gimp', 'AdobeReader' ]
broken_download_minimal_list = [ 'Inkscape', 'TrueCrypt', 'AdobeReader','Flash-InternetExplorer']
broken_silent_minimal_list = [ 'GSview 32bit', 'AdobeReader' ]

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
            downloadtype:'pagesearch',
            url:'',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'',
            key:'HKLM',
            subkey:'SOFTWARE\\',
            value:'',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'AdobeReader':{
        name:'AdobeReader',
        category:'Editors and Viewers',
        description:'PDF viewer',
        url:'http://get.adobe.com/reader/',
        version:{
            url:'',
            regex:'',
            regexpos:0},
        download:{
            downloadtype:'pagesearch',
            downloadtype:'direct', #not implemented yet
            #enterprise URL can not be shared but may be substituted below
            url:'http://download\.adobe\.com/pub/adobe/reader/win/##MAJOR##.x/##VERSION##/en_US/AdbeRdr##DOTLESSVERSION##_en_US.exe',
            },
        silentflags:'',
        installversion:{
            querytype:'',
            key:'HKLM',
            subkey:'SOFTWARE\\',
            value:'',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'Scribus':{
        name:'Scribus',
        category:'Editors and Viewers',
        description:'Opensource Page Layout',
        url:'http://www.scribus.net/',
        version:{
            url:'http://wiki.scribus.net/canvas/Download',
            regex:'Current stable version is ([0-9]+(?:\.[0-9])+)',
            regexpos:0},
        download:{
            downloadtype:'pagesearch',
            url:'http://wiki.scribus.net/canvas/Download',
            regex:'http://sourceforge\.net/projects/scribus/files/scribus/[0-9]+(?:\.[0-9]+)+/scribus-[0-9]+(?:\.[0-9]+)+-win32-install.exe/download',
            regexpos:0},
        silentflags:'/S',
        installversion:{
            querytype:'regkey',
            key:'HKLM',
            subkey:'SOFTWARE\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Uninstall',
            regex:'Scribus ([0-9]+(?:\.[0-9]+)+)',
            regexpos:-1
            }
        },
    'Inkscape':{
        name:'Inkscape',
        category:'Multimedia',
        description:'Opensource Vector Graphics Editor',
        url:'http://inkscape.org/',
        version:{
            url:'http://inkscape.org/download/',
            regex:'Stable release <b>([0-9]+(?:\.[0-9]+)+)</b>',
            regexpos:0},
        download:{
            downloadtype:'pagesearch',
            url:'http://sourceforge.net/projects/inkscape/files/inkscape/##VERSION##/',
            regex:'<a href="(http://sourceforge\.net/projects/inkscape/files/inkscape/[0-9]+(?:\.[0-9]+)+/Inkscape-[0-9]+(?:\.[0-9]+)+-[0-9]-win32\.exe/download)" ',
            regexpos:0},
        silentflags:'/S',
        installversion:{
            querytype:'regval',
            key:'HKLM',
            subkey:'SOFTWARE\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\Inkscape',
            value:'DisplayVersion',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'Gimp':{
        name:'Gimp',
        category:'Multimedia',
        description:'GNU Image Manipulation Program.',
        url:'http://www.gimp.org/',
        version:{
            url:'http://www.gimp.org/downloads/',
            regex:'<a href="http://downloads\.sourceforge\.net/gimp-win/gimp-([0-9](?:\.[0-9]+)+)-i686-setup-[0-9]+.exe">',
            regexpos:0},
        download:{
            downloadtype:'pagesearch',
            url:'http://www.gimp.org/downloads/',
            regex:'<a href="(http://downloads\.sourceforge\.net/gimp-win/gimp-[0-9](?:\.[0-9]+)+-i686-setup-[0-9]+.exe)">',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'regvalsearch', #not yet implemented
            key:'HKLM',
            subkey:'SOFTWARE\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Uninstall',
            value:'DisplayName',
            regex:'GIMP ([0-9]+(?:\.[0-9]+)+)',
            regexpos:-1
            }
        },
    'TrueCrypt':{
        name:'TrueCrypt',
        category:'Encryption',
        description:'Virtual disk encryption',
        url:'http://www.truecrypt.org/',
        version:{
            url:'http://www.truecrypt.org/downloads',
            regex:'Latest Stable Version - ([0-9]+(?:\.[0-9]+)+[a-zA-Z]?)',
            regexpos:0},
        download:{
            downloadtype:'pagesearch',
            url:'',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'regval',
            key:'HKLM',
            subkey:'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\TrueCrypt',
            value:'DisplayVersion',
            regex:'([0-9]+(?:\.[0-9]+)+[a-zA-Z]?)',
            regexpos:0
            }
        },
    'ImageMagick':{
        name:'ImageMagick',
        category:'Multimedia',
        description:'A software suite to create, edit, compose, or convert bitmap images.',
        url:'http://www.imagemagick.org',
        version:{
            url:'http://www.imagemagick.org/www/binary-releases.html',
            regex:'<a href= "http://www\.imagemagick\.org/download/binaries/ImageMagick-([0-9]+(?:\.[0-9]+)+-[0-9]+)-Q16-windows-dll\.exe">',
            regexpos:0},
        download:{
            downloadtype:'pagesearch',
            url:'http://www.imagemagick.org/www/binary-releases.html',
            regex:'<a href= "(http://www\.imagemagick\.org/download/binaries/ImageMagick-[0-9]+(?:\.[0-9]+)+-[0-9]+-Q16-windows-dll\.exe)">',
            regexpos:0},
        silentflags:'/VERYSILENT',
        installversion:{
            querytype:'regval',
            key:'HKLM',
            subkey:'SOFTWARE\\ImageMagick\\Current',
            value:'Version',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'GSview 32bit':{
        name:'GSview 32bit',
        category:'Utilities',
        description:'GSview is a graphical interface for Ghostscript',
        url:'http://pages.cs.wisc.edu/~ghost/gsview/index.htm',
        version:{
            url:'http://pages.cs.wisc.edu/~ghost/gsview/index.htm',
            regex:'>Obtaining GSview ([0-9]+(?:\.[0-9]+)+)<',
            regexpos:0},
        download:{
            downloadtype:'pagesearch',
            url:'http://pages.cs.wisc.edu/~ghost/gsview/get##DOTLESSVERSION##.htm',
            regex:'<a href="(http://mirror\.cs\.wisc\.edu/pub/mirrors/ghost/ghostgum/gsv[0-9]+w32\.exe)">',
            regexpos:0},
        silentflags:'/auto',
        installversion:{
            querytype:'regvalname',
            key:'HKLM',
            subkey:'SOFTWARE\\Ghostgum\\GSView',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:-1
            }
        },
    'Ghostscript':{
        name:'Ghostscript',
        category:'Utilities',
        description:'An interpreter for the PostScript language and for PDF.',
        url:'http://www.ghostscript.com/',
        version:{
            url:'http://www.ghostscript.com/download/',
            regex:'<a href="gsdnld.html">Ghostscript ([0-9]+(?:\.[0-9]+)+)</a>',
            regexpos:0},
        download:{
            downloadtype:'pagesearch',
            url:'http://www.ghostscript.com/download/gsdnld.html',
            regex:'<a href="(http://downloads\.ghostscript\.com/public/gs[0-9]+w32\.exe)">',
            regexpos:0},
        silentflags:'/S',
        installversion:{
            querytype:'regkey',
            key:'HKLM',
            subkey:'SOFTWARE\\GPL Ghostscript',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:-1
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
            downloadtype:'pagesearch',
            url:'http://7-zip.org',
            regex:'<A href="(.*/sevenzip/7z[0-9]+.exe)',
            regexpos:0},
        silentflags:'/S',
        installversion:{
            querytype:'regval',
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
            downloadtype:'pagesearch',
            url:'http://www.mozilla.org/en-US/firefox/new/',
            regex:'<li><a href="(http://download\.mozilla\.org/\?product=firefox-[0-9]+(?:\.[0-9]+)+&amp;os=win&amp;lang=en-US)">Windows</a></li>',
            regexpos:0},
        silentflags:'-ms',
        installversion:{
            querytype:'regval',
            key:'HKLM',
            subkey:'SOFTWARE\\Mozilla\\Mozilla Firefox',
            value:'CurrentVersion',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
     'Notepad++':{
        name:'Notepad++',
        category:'Multimedia',
        description:'An Editor that knows about \\n',
        url:'http://notepad-plus-plus.org/',
        version:{
            url:'http://notepad-plus-plus.org/download/',
            regex:'v([0-9]+(?:\.[0-9]+)*)',
            regexpos:0},
        download:{
            downloadtype:'pagesearch',
            url:'http://notepad-plus-plus.org/download/',
            regex:'http://download.tuxfamily.org/notepadplus/[0-9]+(?:\.[0-9]+)+/npp.[0-9]+(?:\.[0-9]+)+.Installer.exe',
            regexpos:0},
        silentflags:'-ms',
        installversion:{
            querytype:'regval',
            key:'HKLM',
            subkey:'SOFTWARE\\Mozilla\\Mozilla Firefox',
            value:'CurrentVersion',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'GVim':{
        name:'GNU Vim',
        category:'Editors',
        description:'Vi Improved Editing Environment',
        url:'http://www.vim.org',
        version:{
            url:'http://www.vim.org/download.php',
            regex:'"Vim (7.3) is the latest stable version"',
            regexpos:0},
        download:{
            downloadtype:'pagesearch',
            url:'http://www.vim.org/download.php',
            regex:'(ftp://ftp.vim.org/pub/vim/pc/gvim[0-9]+_[0-9]+.exe)',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'',
            key:'HKLM',
            subkey:'SOFTWARE\\',
            value:'',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
   
   'Flash-Firefox':{
        name:'Adobe Flash Player (Firefox)',
        category:'Multimedia',
        description:'Web Plugin Framework for Firefox',
        url:'http://www.adobe.com/products/flashplayer.html ',
        version:{
            url:'http://get.adobe.com/flashplayer/',
            regex:'<span id="clientversion">([0-9]+(?:\.[0-9]+)+)</span>',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://aihdownload.adobe.com/bin/live/install_flashplayer11x32_mssd_aih.exe'},
        silentflags:'/verysilent',
        installversion:{    
            querytype:'',
            key:'HKLM',
            subkey:'SOFTWARE\\',
            value:'',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'Flash-InternetExplorer':{
        name:'Adobe Flash Player (IE)',
        category:'Multimedia',
        description:'Virus Plugin Framework for IE',
        url:'http://www.adobe.com/products/flashplayer.html ',
        version:{
            url:'http://get.adobe.com/flashplayer/',
            regex:'<span id="clientversion">([0-9]+(?:\.[0-9]+)+)</span>',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://aihdownload.adobe.com/bin/live/install_flashplayer11x32ax_mssd_aih.exe'},
        silentflags:'/verysilent',
        installversion:{    
            querytype:'',
            key:'HKLM',
            subkey:'SOFTWARE\\',
            value:'',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'Thunderbird':{
        name:'Thunderbird',
        category:'Internet Tools',
        description:'Bayes Classifier Spam Detector',
        url:'http://www.mozilla.org/en-US/thunderbird/',
        version:{
            url:'http://www.mozilla.org/en-US/thunderbird/15.0.1/releasenotes/',
            regex:'v\.([0-9]+(?:\.[0-9]+)+)',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://download.cdn.mozilla.net/pub/mozilla.org/thunderbird/releases/##VERSION##/win32/en-US/Thunderbird%20Setup%20##VERSION##.exe',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'',
            key:'HKLM',
            subkey:'SOFTWARE\\',
            value:'',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'VirtualBox':{
        name:'VirtualBox',
        category:'Virtual Machine',
        description:'x86 and AMD64/Intel64 virtualization product',
        url:'https://www.virtualbox.org/',
        version:{
            url:'https://www.virtualbox.org/wiki/Downloads',
            regex:'VirtualBox ([0-9]+(?:\.[0-9]+)+) for Windows',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://download.virtualbox.org/virtualbox/##VERSION##/VirtualBox-##VERSION##-80657-Win.exe',
            regex:'0',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'',
            key:'HKLM',
            subkey:'SOFTWARE\\',
            value:'',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'Python2':{
        name:'Python 2',
        category:'Programming',
        description:'T3h l337t3st Programming Language Yo',
        url:'python.org',
        version:{
            url:'http://python.org/download/',
            regex:'Python (2(?:\.[0-9]+)+)',
            regexpos:1},
        download:{
            downloadtype:'directurl',
            url:'http://python.org/ftp/python/##VERSION##/python-##VERSION##.msi',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'',
            key:'HKLM',
            subkey:'SOFTWARE\\',
            value:'',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'Python3':{
        name:'Python 3',
        category:'Programming',
        description:'If you are into that New Age Stuff',
        url:'',
        version:{
            url:'http://python.org/download/',
            regex:'Python (3(?:\.[0-9]+)+)',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://python.org/ftp/python/##VERSION##/python-##VERSION##.msi',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'',
            key:'HKLM',
            subkey:'SOFTWARE\\',
            value:'',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'SmartGit':{
        name:'SmartGit',
        category:'Source Control Management',
        description:'The Smart way to git',
        url:'http://www.syntevo.com/smartgit/index.html',
        version:{
            url:'http://www.syntevo.com/smartgit/index.html',
            regex:'Version:  <span>([0-9]+(?:\.[0-9]+)+)',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://www.syntevo.com/download/smartgit/smartgit-win32-setup-jre-##UNDERSCOREVERSION##.zip',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'',
            key:'HKLM',
            subkey:'SOFTWARE\\',
            value:'',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
   
    'rwhod':{
        name:'Windows R Who Daemon',
        category:'Utilities',
        description:'Answers linux rwho requests for finding people on your network',
        url:'http://matthew.loar.name/software/rwho/',
        version:{
            url:'http://matthew.loar.name/software/rwho/',
            regex:'([0-9]+(?:\.[0-9]+)+)</td>',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://matthew.loar.name/software/archives/rwho/##VERSION##/rwho.msi',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'',
            key:'HKLM',
            subkey:'SOFTWARE\\',
            value:'',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'ScreenRecorder':{
        name:'Screen Recorder',
        category:'Utilities',
        description:'For Recording Screens',
        url:'http://technet.microsoft.com/en-us/magazine/2009.03.utilityspotlight2.aspx?pr=blog',
        version:{
            url:'http://technet.microsoft.com/en-us/magazine/2009.03.utilityspotlight2.aspx?pr=blog',
            regex:'UtilityOnline((?:'+months+')[0-9]+_[0-9]+)',
            regexpos:1},
        download:{
            downloadtype:'directurl',
            url:'http://download.microsoft.com/download/f/d/0/fd05def7-68a1-4f71-8546-25c359cc0842/UtilityOnlineMarch092009_03.exe',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'',
            key:'HKLM',
            subkey:'SOFTWARE\\',
            value:'',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'SysinternalsSuite':{
        name:'Sysinternals Suite',
        category:'Utilities',
        description:'Collection of Mark Russinovich system utilities',
        url:'http://technet.microsoft.com/en-us/sysinternals',
        version:{
            url:'http://technet.microsoft.com/en-us/sysinternals/bb842062',
            regex:'<p>Updated: ((?:'+months+') [0-9]+, [0-9]+)</p>',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://download.sysinternals.com/files/SysinternalsSuite.zip',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'',
            key:'HKLM',
            subkey:'SOFTWARE\\',
            value:'',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
        'CamStudioCodec':{
        name:'CamStudio Video Codec',
        category:'Multimedia',
        description:'The Codec for Camstudio',
        url:'http://camstudio.org/',
        version:{
            url:'http://camstudio.org/',
            regex:'Lossless Video Codec v([0-9]+(?:\.[0-9]+)+)',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://voxel.dl.sourceforge.net/project/camstudio/legacy/CamStudioCodec-##VERSION##-w32.zip',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'',
            key:'HKLM',
            subkey:'SOFTWARE\\',
            value:'',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'Putty':{
        name:'Putty',
        category:'Utilties',
        description:'Windows SSH and telenet client',
        url:'http://www.chiark.greenend.org.uk/~sgtatham/putty/',
        version:{
            url:'http://www.chiark.greenend.org.uk/~sgtatham/putty/',
            regex:'The latest version is ((?:'+alphabeta+') [0-9]+(?:\.[0-9]+)+)',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://the.earth.li/~sgtatham/putty/latest/x86/putty.exe',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',  
        installversion:{
            querytype:'',
            key:'HKLM',
            subkey:'SOFTWARE\\',
            value:'',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }   
        },
    'WinSCP':{
        name:'WinSCP',
        category:'Utilties',
        description:'Secure Copy for Windows',
        url:'http://winscp.net/eng/index.php',
        version:{
            url:'http://winscp.net/eng/download.php',
            regex:'WinSCP ([0-9]+(?:\.[0-9]+)+)',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://download.winscp.net/download/files/201209112230068836a699a59f83af7546a9597cf90b/winscp##DOTLESSVERSION##setup.exe',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'',
            key:'HKLM',
            subkey:'SOFTWARE\\',
            value:'',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'WindowsSystemControlCenter':{
        name:'Windows System Control Center',
        category:'Utilities ',
        description:'Utility Organizer',
        url:'http://www.kls-soft.com/wscc/index.php',
        version:{
            url:'http://www.kls-soft.com/wscc/index.php',
            regex:'Latest version:</font></strong> ([0-9]+(?:\.[0-9]+)+)',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://www.kls-soft.com/downloads/wscc.zip',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'',
            key:'HKLM',
            subkey:'SOFTWARE\\',
            value:'',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'VioletUML':{
        name:'Violet UML Editor',
        category:'Programming',
        description:'A UML editor with nice benefits',
        url:'http://alexdp.free.fr/violetumleditor/page.php',
        version:{
            url:'http://sourceforge.net/projects/violet/',
            regex:'com.horstmann.violet-([0-9]+(?:\.[0-9]+)+)',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://superb-dca2.dl.sourceforge.net/project/violet/violetumleditor/##VERSION##/com.horstmann.violet-##VERSION.jar',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'',
            key:'HKLM',
            subkey:'SOFTWARE\\',
            value:'',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'Racket':{
        name:'Racket',
        category:'Programming',
        description:'A Lisp',
        url:'http://racket-lang.org/',
        version:{
            url:'http://racket-lang.org/download/',
            regex:'Download Racket v([0-9]+(?:\.[0-9]+)+)',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://download.racket-lang.org/installers/##VERSION##/racket/racket-##VERSION##-bin-i386-win32.exe',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'',
            key:'HKLM',
            subkey:'SOFTWARE\\',
            value:'',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'Netbeans':{
        name:'Netbeans',
        category:'Programming',
        description:'Java IDE',
        url:'netbeans.org',
        version:{
            url:'http://netbeans.org/features/index.html',
            regex:'NetBeans IDE ([0-9]+(?:\.[0-9]+)+) Features',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://download.netbeans.org/netbeans/##VERSION##/final/bundles/netbeans-##VERSION##-ml-javase-windows.exe',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'',
            key:'HKLM',
            subkey:'SOFTWARE\\',
            value:'',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'MySQLJDBC':{
        name:'MySQLJDBC',
        category:'Database',
        description:'Java Database Connector for Mysql',
        url:'http://www.mysql.com/downloads/connector/j/?product=c-j',
        version:{   
            url:'http://www.mysql.com/downloads/connector/j/?product=c-j',
            regex:'Connector/J ([0-9]+(?:\.[0-9]+)+)',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://www.mysql.com/get/Downloads/Connector-J/mysql-connector-java-##VERSION##.tar.gz/from/http://cdn.mysql.com/',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'',
            key:'HKLM',
            subkey:'SOFTWARE\\',
            value:'',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'MySQLWorkbench':{
        name:'MySQL Workbench',
        category:'Database',
        description:'GUI Mysql editor',
        url:'http://www.mysql.com/products/workbench/',
        version:{
            url:'http://dev.mysql.com/downloads/workbench/',
            regex:'MySQL Workbench ([0-9]+(?:\.[0-9]+)+)',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://dev.mysql.com/get/Downloads/MySQLGUITools/mysql-workbench-gpl-##VERSION##-win32.msi/from/http://cdn.mysql.com/',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'',
            key:'HKLM',
            subkey:'SOFTWARE\\',
            value:'',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'Squeak':{
        name:'Squeak',
        category:'http://www.squeak.org ',
        description:'',
        url:'',
        version:{
            url:'http://www.squeakvm.org/win32/',
            regex:'SqueakVM-Win32-([0-9]+(?:\.[0-9]+)+)-bin.zip</a>. ',
            regexpos:0},
        download:{
            downloadtype:'directurl',
            url:'http://www.squeakvm.org/win32/release/SqueakVM-Win32-##VERSION##-bin.zip',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'',
            key:'HKLM',
            subkey:'SOFTWARE\\',
            value:'',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        },
    'EMPTYEND':{
        name:'',
        category:'',
        description:'',
        url:'',
        version:{
            url:'',
            regex:'',
            regexpos:0},
        download:{
            downloadtype:'pagesearch',
            url:'',
            regex:'',
            regexpos:0},
        silentflags:'/verysilent',
        installversion:{
            querytype:'',
            key:'HKLM',
            subkey:'SOFTWARE\\',
            value:'',
            regex:'([0-9]+(?:\.[0-9]+)+)',
            regexpos:0
            }
        }
     }

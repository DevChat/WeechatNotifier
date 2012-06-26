SCRIPT_NAME = "Weechat Notifier"
SCRIPT_AUTHOR = "Bernard McKeever"
SCRIPT_VERSION = "0.1"
SCRIPT_LICENSE = "GPL3"
SCRIPT_DESC = " Send notifications to an android phone.\
                This is a port from IRSSI's IRRSI Notifier\
                Perl script."

import_ok = True

try:
    import weechat as w
except:
    print("This script must be run under Weechat.\
         Get weechat now at: http://www.weechat.org")

lastMsg = ""
lastServer = ""
lastNick = ""
lastAddress = ""
lastTarget = ""
lastKeyboardActivity = ""

def private:
    return

def public:
    return

def print_text:
    return

def activity_allows_hilight:
    return

def dangerous_string:
    return

def hilight:
    return

def sanitize:
    return

def encrypt:
    return

def decrypt:
    return

def setup_keypress_handler:
    return

def even_key_pressed:
    return


if __name__ = "__main__" and import_ok:
    w.register( SCRIPT_NAME, SCRIPT_AUTHOR, SCRIPT_VERSION, SCRIPT_LICENSE, SCRIPT_DESC, "", "")

    w.hook_print( "", "", "", 1, "hlpv_print_cb", "" )
    

import clr
import System
import Microsoft
import Microsoft.Win32.Registry as Registry

def get_default_browser():
    try:
        key = Registry.ClassesRoot.OpenSubKey("HTTP\shell\open\command", False)
        browser = key.GetValue(None).ToString().ToLower().Replace("\"", "")
        browser = browser.split('-')[0]
        browser = browser.strip()
        return browser
    finally:
        if key:
            key.Close()
    
def launch_default_browser(destination):
    p = System.Diagnostics.Process()
    p.StartInfo.FileName = get_default_browser()
    #print "%s %s" % (get_default_browser(), url)
    p.StartInfo.Arguments = "%s" % destination
    p.Start()
    
    

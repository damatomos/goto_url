import webbrowser as wb
import re
import os

import sys

args = sys.argv

url_pattern = "^https?:\\/\\/(?:www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)$"

def change_browser(name):
    path = "prefs.txt"
    file = open("prefs.txt", 'a')
    file.close()
    file = open(path, 'r+')

    lines = []
    while True:
        line = file.readline()
        if '-b' in line or line == '\n':
            continue
        else:
            lines.append(line)
        if not line:
            break
    file.seek(0)
    file.truncate()
    lines.append('\n-b {}'.format(name))
    file.writelines(lines)
    file.close()
    return

def add_new_browser(name, path):
    path_file = "prefs.txt"
    file = open("prefs.txt", 'a')
    lines = ''
    with open(path_file, 'r') as f:
        lines = f.readlines()
    with open(path_file, 'w') as f:
        for line in lines:
            if '{}$'.format(name) in line:
                f.write('\n-r {}${}'.format(name,path))
                return
    file.write('-r {}${}'.format(name,path))
    file.close()
    return

def get_browser_list():
    browsers = []
    path = "prefs.txt"
    if os.path.exists(path):
        file = open(path, 'r+')
        while True:
            line = file.readline()
            
            if not line:
                break
            
            if '-r' in line:
                print(line)
                browsers.append(line.split('-r')[1].strip())
            else:
                continue
    return browsers

def read_prefs():
    
    path = "prefs.txt"
    if os.path.exists(path):
        file = open(path, 'r')
        while True:
            line = file.readline()
            print(line)
            if not line:
                break
            

def register_new_browser(name, path):
    pass

def get_browser_pref():
    path = "prefs.txt"
    if os.path.exists(path):
        file = open(path, 'r')
        result = file.read()
        if '-b' in result:
            print('has b')
            return result.split('-b')[1].strip()
    return None

def _help():
    print('Use -b to define browser ex: chrome, opera, operagx, firefox\nUse -s to save favorite browser ex: -s operagx\nUse "to -r browser_name path" to register new browser\nUse app ex: to https://github.com/damatomos -b chrome')

def main():
    browser = get_browser_pref()
    url = None

    for b in get_browser_list():
        values = b.split('$')
        wb.register(values[0], None, wb.GenericBrowser([values[1], "-incognito", "%s"]))
        

    for arg in range(len(args)):
        
        if args[arg] in ['help', '--help', '-help', 'h', '-h']:
            _help()
            return
        elif args[arg] == '-r' and len(args) > arg + 1:
            name = args[arg + 1]
            path = ''
            for x in range(arg + 2, len(args)):
                path += ' ' + args[x]
                if '.exe' in args[x]:
                    break
            add_new_browser(name, path.strip())
            return
        elif args[arg] == '-b' and len(args) > arg:
            browser = args[arg + 1]
        elif args[arg] == '-s' and len(args) > arg:
            change_browser(args[arg + 1])
            return
        elif re.match(url_pattern, args[arg]):
            url = args[arg]

    if url == None:
        print('URL is not defined')
        return

    if browser != None:
        wb.get(browser).open_new_tab(url)
    else:
        wb.open_new_tab(url)
            

if __name__ == '__main__':
    main()

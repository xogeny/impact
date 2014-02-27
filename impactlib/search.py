from impactlib.load import load_repo_data
from fnmatch import fnmatch

try:
    import colorama
    colorama.init()
    use_color = True
except:
    use_color = False

def search(term, verbose):
    repo_data = load_repo_data()

    matches = []
    for repo in repo_data:
        match = False
        data = repo_data[repo]
        if repo.find(term)>=0:
            match = True
        if fnmatch(repo, term):
            match = True
        if "description" in data and data["description"].find(term)>=0:
            match = True
        if match:
            matches.append((repo, data["description"], data["versions"],
                            data.get("homepage", None)))
    if len(matches)==0:
        print "No matches found for search term '"+term+"'"
    else:
        for m in sorted(matches):
            libname = m[0]
            libpage = m[3]
            libdesc = m[1]
            libvers = m[2]
            if verbose:
                if len(libvers.keys())==0:
                    versions = "None"
                else:
                    versions = ", ".join(sorted(libvers.keys()))
                msg = "\n  Available versions: "+versions
                if use_color:
                    print (colorama.Fore.YELLOW+libname+" "
                           +colorama.Fore.RED+"<"+libpage+">"
                           +colorama.Fore.RESET+" - "
                           +colorama.Fore.GREEN+libdesc+colorama.Fore.CYAN + msg)
                else:
                    print libname+" <"+libpage+"> - "+libdesc + msg
            else:
                if use_color:
                    print (colorama.Fore.YELLOW+libname+" "
                           +colorama.Fore.RED+"<"+libpage+">")
                else:
                    print libname+" <"+libpage+">"

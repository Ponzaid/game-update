init python:

    import urllib.request
    import json

    update_available = False
    latest_version = ""
    update_url = ""

    def check_update():

        global update_available
        global latest_version
        global update_url

        try:

            url = "https://raw.githubusercontent.com/USUARIO/repositorio/main/update.json"

            data = urllib.request.urlopen(url).read()
            info = json.loads(data)

            latest_version = info["version"]
            update_url = info["url"]

            if latest_version != game_version:
                update_available = True

        except:
            pass
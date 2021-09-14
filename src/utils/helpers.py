import os


def download_tarball(username, repository):
    # Download the latest release tarball and return the name of it.
    # FIXME: Handle errors from curl and wget
    if repository == "goverlay":
        command = "curl -sL https://api.github.com/repos/{}/{}/releases/latest |  jq '.assets[].browser_download_url'".format(
            username, repository)
    else:
        command = "curl -sL https://api.github.com/repos/{}/{}/releases/latest |  jq '.assets[].browser_download_url | select(endswith(\"tar.gz\"))'".format(
            username, repository)

    tarball = os.popen(command).read()
    os.system("wget {}".format(tarball))

    return tarball.split("/")[8]

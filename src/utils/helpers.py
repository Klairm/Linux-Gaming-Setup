import os


def download_tarball(username, repository):
    # Download the latest release tarball and return the name of it.
    # FIXME: Handle errors from curl and wget
    extension = "tar.gz"
    if repository == "wine-ge-custom":
        extension = "tar.xz"

    if repository == "goverlay":
        command = "curl -sL https://api.github.com/repos/{}/{}/releases/latest |  jq '.assets[].browser_download_url'".format(
            username, repository)

    else:
        command = "curl -sL https://api.github.com/repos/{}/{}/releases/latest |  jq '.assets[].browser_download_url | select(endswith(\"{}\"))'".format(
            username, repository, extension)

    tarball = os.popen(command).read()
    os.system("wget {}".format(tarball))

    return tarball.split("/")[8]

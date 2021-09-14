import os


def download_tarball(username, repository, tar_format):
    # Download the latest release tarball and return the name of it.
    # FIXME: Handle errors from curl and wget
    command = "curl -sL https://api.github.com/repos/{}/{}/releases/latest |  jq '.assets[].browser_download_url | endswith((""{}""))'".\
        format(
            username, repository, tar_format)

    tarball = os.popen(command).read()

    os.system("wget {}".format(tarball))

    return tarball.split("/")[8]

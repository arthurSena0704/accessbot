import versioneer


def task_release():
    version = versioneer.get_version()

    return {
        "actions": [f'git tag -a {version} -m "Automatic version"'],
    }

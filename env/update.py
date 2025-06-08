import os


def update_environment_yml():
    os.system('conda env export --no-builds | grep -v "^prefix: " > environment.yml')
    print("environment.yml updated")


if __name__ == "__main__":
    update_environment_yml()

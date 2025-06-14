import os

def update_environment_yml():
    # 匯出 conda 環境，去掉 prefix 行
    os.system('conda env export --no-builds | grep -v "^prefix: " > environment.yml')
    print("environment.yml updated")

def generate_clean_requirements():
    # pip freeze 產生 requirements.txt
    os.system('pip list --format=freeze > requirements.txt')

if __name__ == "__main__":
    update_environment_yml()
    generate_clean_requirements()

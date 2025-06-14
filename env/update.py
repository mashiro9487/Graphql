import os

def update_environment_yml():
    # 匯出 conda 環境，去掉 prefix 行
    os.system('conda env export --no-builds | grep -v "^prefix: " > environment.yml')
    print("environment.yml updated")

def generate_clean_requirements():
    # pip freeze 產生 requirements.txt
    os.system('pip freeze > requirements.txt')
    print("requirements.txt generated")

    # 讀取並過濾包含本地路徑的套件
    with open("requirements.txt", "r") as f:
        lines = f.readlines()

    clean_lines = []
    for line in lines:
        if " @ file://" in line:
            # 跳過或你也可以在這裡做進一步處理
            continue
        else:
            clean_lines.append(line)

    with open("requirements.txt", "w") as f:
        f.writelines(clean_lines)
    print("requirements.txt cleaned from local path entries")

if __name__ == "__main__":
    update_environment_yml()
    generate_clean_requirements()

import os
import subprocess
def update_environment_yml():
    # 匯出 conda 環境，去掉 prefix 行

    with open("environment.yml", "w") as f:
        result = subprocess.run(
            ["conda", "env", "export", "--name", "Graphql", "--no-builds"],
            stdout=f,
            stderr=subprocess.PIPE,
            text=True
        )

    if result.returncode == 0:
        print("✅ environment.yml updated.")
    else:
        print("❌ Failed to export environment:", result.stderr)

def generate_clean_requirements():
    # pip freeze 產生 requirements.txt
    os.system('pip list --format=freeze > requirements.txt')

if __name__ == "__main__":
    update_environment_yml()
    generate_clean_requirements()

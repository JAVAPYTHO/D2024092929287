import argparse
import subprocess
from pathlib import Path


def run_script(script_path: Path):
    print(f"[RUN] {script_path}")
    subprocess.run(["python", str(script_path)], check=True)


def main():
    parser = argparse.ArgumentParser(description="Unified runner for D2024092929287")
    parser.add_argument("--task", choices=["q1", "q2", "q3", "all"], default="all")
    args = parser.parse_args()

    root = Path(__file__).resolve().parent
    code_root = root / "Python Code and data" / "Python Code and data"

    task_scripts = {
        "q1": [code_root / "question1" / "Q1_1.py"],
        "q2": [
            code_root / "question2" / "Python code" / "Calculate the total number of services.py",
            code_root / "question2" / "Python code" / "Service density of two cities.py",
            code_root / "question2" / "Python code" / "Solve for density index.py",
            code_root / "question2" / "Python code" / "Solve for density coefficient.py",
            code_root / "question2" / "Python code" / "city scores.py",
        ],
        "q3": [
            code_root / "question3" / "q3.py",
            code_root / "question3" / "02.py",
        ],
    }

    if args.task == "all":
        scripts = task_scripts["q1"] + task_scripts["q2"] + task_scripts["q3"]
    else:
        scripts = task_scripts[args.task]

    for s in scripts:
        if s.exists():
            run_script(s)
        else:
            print(f"[SKIP] not found: {s}")


if __name__ == "__main__":
    main()

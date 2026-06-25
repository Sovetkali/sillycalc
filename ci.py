import subprocess

steps = [
    ["python", "-m", "pytest"],
    ["python", "-m", "flake8"]
]

for step in steps:
    result = subprocess.run(step)

    if result.returncode != 0:
        print(f'Step failed: {" ".join(step)}')
        exit(1)

print("Pipeline passed!")

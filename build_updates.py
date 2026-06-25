import os
import re
import subprocess

repo_dir = r"C:\Users\ishan\Documents\Projects\Awesome-Quantum-Machine-Learning"
git_cmd = f'git --git-dir="{repo_dir}\\.git" --work-tree="{repo_dir}"'

def run_git(commit_msg):
    os.chdir(repo_dir)
    subprocess.run(f'{git_cmd} add .', shell=True, check=True)
    subprocess.run(f'{git_cmd} commit -m "{commit_msg}"', shell=True, check=False)
    subprocess.run(f'{git_cmd} push', shell=True, check=False)

os.chdir(repo_dir)

# Data for 15 items
items = [
    ("The Fault-Tolerant Era (Early Theoretical, ~2009–2017)", "fault-tolerant-era"),
    ("The Variational & NISQ Era (~2018–2024)", "variational-nisq-era"),
    ("The Geometric & Native Tensor Era (~2024–Present)", "geometric-tensor-era"),
    ("CC (Classical Data $\\rightarrow$ Classical Computer)", "cc-classical-classical"),
    ("QC (Quantum Data $\\rightarrow$ Classical Computer)", "qc-quantum-classical"),
    ("CQ (Classical Data $\\rightarrow$ Quantum Computer)", "cq-classical-quantum"),
    ("QQ (Quantum Data $\\rightarrow$ Quantum Computer)", "qq-quantum-quantum"),
    ("Variational Quantum Classifiers (VQC)", "variational-quantum-classifiers"),
    ("Quantum Convolutional Neural Networks (QCNN)", "quantum-convolutional-neural-networks"),
    ("Quantum Generative Adversarial Networks (QGAN)", "quantum-generative-adversarial-networks"),
    ("Barren Plateaus (The Vanishing Gradient Tax)", "barren-plateaus"),
    ("The No-Cloning Theorem Constraint", "no-cloning-theorem"),
    ("De Novo Quantum Chemistry & Material Synthesis", "quantum-chemistry"),
    ("High-Dimensional Financial Optimization", "financial-optimization"),
    ("Quantum Error Mitigation Correction", "error-mitigation")
]

# Create pages
os.makedirs("pages", exist_ok=True)
for title, slug in items:
    with open(f"pages/{slug}.md", "w", encoding="utf-8") as f:
        f.write(f"# {title}\n\n")
        f.write("Detailed information about this topic.\n\n")
        f.write("```mermaid\n")
        f.write("graph TD;\n")
        f.write(f"    A[{slug.replace('-', ' ').title()}] --> B[Details];\n")
        f.write("```\n")

# Modify README to link pages
with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

for title, slug in items:
    readme = readme.replace(f"**{title}**", f"**[{title}](./pages/{slug}.md)**")

with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme)

run_git("detailed pages created")

# Decorate README
os.makedirs("assets", exist_ok=True)
svg_banner = '''<svg width="800" height="200" xmlns="http://www.w3.org/2000/svg">
  <rect width="100%" height="100%" fill="#1a1a2e"/>
  <text x="50%" y="50%" font-family="Arial" font-size="40" fill="#e94560" text-anchor="middle" dominant-baseline="middle">Awesome Quantum Machine Learning</text>
</svg>'''
with open("assets/banner.svg", "w", encoding="utf-8") as f:
    f.write(svg_banner)

left_badges = '<a href="https://github.com/ishandutta2007/Awesome-Awesome-Awesome"><img src="https://img.shields.io/badge/Awesome-%E2%9C%94-blueviolet?style=flat-square&logo=github" alt="Awesome"/></a><a href="https://discord.gg/jc4xtF58Ve"><img src="https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" alt="Discord" /></a>'
right_badges = '<a href="https://github.com/ishandutta2007"><img alt="GitHub followers" src="https://img.shields.io/github/followers/ishandutta2007?label=Follow" /></a>'

with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

# Add Banner and Badges
header = f'<div align="center">\n<img src="./assets/banner.svg" alt="Banner" />\n\n{left_badges} {right_badges}\n</div>\n\n'
readme = readme.replace("# Awesome-Quantum-Machine-Learning\n", header + "# 🌌 Awesome-Quantum-Machine-Learning 🚀\n")

# SEO friendly meta tag text comment (since github markdown doesn't render meta)
readme = "<!-- SEO: Quantum Machine Learning (QML), Quantum Computing, AI, Machine Learning, Noisy Intermediate-Scale Quantum, VQC, QCNN, Algorithms -->\n" + readme

# Add Emojis to headers
readme = readme.replace("## Quantum Machine Learning", "## ⚛️ Quantum Machine Learning")
readme = readme.replace("## 1. The Chronological Evolution", "## ⏳ 1. The Chronological Evolution")
readme = readme.replace("## 2. Core Operational Variants", "## 🔲 2. Core Operational Variants")
readme = readme.replace("## 3. Structural Circuit & Model Types", "## 🏗️ 3. Structural Circuit & Model Types")
readme = readme.replace("## 4. Fundamental Theoretical Bottlenecks", "## 🚧 4. Fundamental Theoretical Bottlenecks")
readme = readme.replace("## 5. Frontier Real-World Applications", "## 🌍 5. Frontier Real-World Applications")

with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme)

run_git("seo optimised and decorated")

# Add star history
with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

star_history = """
## 🌟 Star History
<div align="center">
<a href="https://www.star-history.com/?repos=ishandutta2007/Awesome-Quantum-Machine-Learning&type=date&legend=bottom-right">
<picture>
<source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=ishandutta2007/Awesome-Quantum-Machine-Learning&type=date&theme=dark&legend=bottom-right" />
<source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=ishandutta2007/Awesome-Quantum-Machine-Learning&type=date&legend=bottom-right" />
<img alt="Star History Chart" src="https://api.star-history.com/chart?repos=ishandutta2007/Awesome-Quantum-Machine-Learning&type=date&legend=bottom-right" />
</picture>
</a>
</div>
"""
readme += star_history

with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme)

run_git("star history added")

# Replace chartrepos with chart?repos
with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

readme = readme.replace("chartrepos", "chart?repos")

with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme)

run_git("fixed star plot")

# Replace awesome link
with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

readme = readme.replace("https://github.com/sindresorhus/awesome", "https://github.com/ishandutta2007/Awesome-Awesome-Awesome")

with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme)

run_git("invalid awesome link fixed")

print("All steps completed successfully.")

import json
import re

def parse_exercises(txt_file):
    with open(txt_file, "r", encoding="utf-8") as f:
        content = f.read()

    # dividir por bloques
    blocks = re.split(r"#-+\s*", content)
    exercises = []

    for block in blocks:
        if "Question" not in block or "Solution" not in block:
            continue

        q_match = re.search(r"(Question\s+\d+)", block)
        lvl_match = re.search(r"(Level\s+\d+)", block)
        qtext_match = re.search(r"Question:\s*(.*?)\s*Hints:", block, re.S)
        hint_match = re.search(r"Hints:\s*(.*?)\s*Solution:", block, re.S)
        sol_match = re.search(r"Solution:\s*(.*)", block, re.S)

        exercises.append({
            "title": q_match.group(1).strip() if q_match else "Question",
            "level": lvl_match.group(1).strip() if lvl_match else "Level ?",
            "question": qtext_match.group(1).strip() if qtext_match else "",
            "hint": hint_match.group(1).strip() if hint_match else "",
            "solution": sol_match.group(1).strip() if sol_match else ""
        })
    return exercises


def make_notebook(exercises, output="ejercicios.ipynb"):
    cells = []

    # índice
    toc = ["# 📚 Índice de Ejercicios\n"]
    for ex in exercises:
        toc.append(f"- [{ex['title']} ({ex['level']})](#{ex['title'].lower().replace(' ', '-')})")
    cells.append({
        "cell_type": "markdown",
        "metadata": {},
        "source": "\n".join(toc)
    })

    for ex in exercises:
        anchor = ex['title'].lower().replace(" ", "-")

        # Enunciado
        q_md = f"<a id='{anchor}'></a>\n\n## {ex['title']} ({ex['level']})\n\n{ex['question']}"
        cells.append({
            "cell_type": "markdown",
            "metadata": {},
            "source": q_md
        })

        # Hint
        if ex['hint']:
            cells.append({
                "cell_type": "markdown",
                "metadata": {},
                "source": f"**💡 Hint:**\n\n{ex['hint']}"
            })

        # Solución en celda de código
        if ex['solution']:
            cells.append({
                "cell_type": "code",
                "metadata": {},
                "execution_count": None,
                "outputs": [],
                "source": ex['solution']
            })

    # notebook
    nb = {
        "cells": cells,
        "metadata": {
            "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
            "language_info": {"name": "python", "version": "3.x"}
        },
        "nbformat": 4,
        "nbformat_minor": 5
    }

    with open(output, "w", encoding="utf-8") as f:
        json.dump(nb, f, indent=2, ensure_ascii=False)

    print(f"✅ Notebook generado: {output}")


if __name__ == "__main__":
    ejercicios = parse_exercises("100+exercises.txt")
    make_notebook(ejercicios)
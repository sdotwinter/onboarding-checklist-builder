import json
from pathlib import Path

def export_json(rows, out: Path):
    out.write_text(json.dumps([{"id":r[0],"title":r[1],"owner":r[2],"completed":bool(r[3])} for r in rows], indent=2)+"\n", encoding='utf-8')

def export_md(rows, out: Path):
    lines=["# Onboarding Checklist",""]
    for r in rows:
        lines.append(f"- [{'x' if r[3] else ' '}] {r[1]}" + (f" (@{r[2]})" if r[2] else ""))
    out.write_text("\n".join(lines)+"\n", encoding='utf-8')

import argparse
from pathlib import Path
from store import init_db,add_item,list_items,assign_item,complete_item
from templates import TEMPLATES
from exporter import export_json,export_md

def run(argv=None):
    p=argparse.ArgumentParser(prog='onboarding-checklist-builder',description='Build and track onboarding checklists.')
    sub=p.add_subparsers(dest='cmd',required=True)
    a=sub.add_parser('init'); a.add_argument('path',nargs='?',default='.'); a.add_argument('--template',choices=['backend','frontend','devops'],default='backend')
    b=sub.add_parser('add-item'); b.add_argument('title'); b.add_argument('--owner',default=''); b.add_argument('path',nargs='?',default='.')
    c=sub.add_parser('assign'); c.add_argument('item_id',type=int); c.add_argument('owner'); c.add_argument('path',nargs='?',default='.')
    d=sub.add_parser('complete'); d.add_argument('item_id',type=int); d.add_argument('path',nargs='?',default='.')
    e=sub.add_parser('report'); e.add_argument('path',nargs='?',default='.')
    f=sub.add_parser('export'); f.add_argument('path',nargs='?',default='.'); f.add_argument('--format',choices=['json','md'],default='md'); f.add_argument('--out',default='checklist.md')
    args=p.parse_args(argv); root=Path(getattr(args,'path','.')).resolve(); init_db(root)
    if args.cmd=='init':
        for item in TEMPLATES[args.template]: add_item(root,item)
        print(f"Initialized checklist with '{args.template}' template at {root}"); return 0
    if args.cmd=='add-item': add_item(root,args.title,args.owner); print('Item added')
    elif args.cmd=='assign': assign_item(root,args.item_id,args.owner); print('Item assigned')
    elif args.cmd=='complete': complete_item(root,args.item_id); print('Item completed')
    elif args.cmd=='report':
        rows=list_items(root); done=sum(r[3] for r in rows); total=len(rows); print(f"Progress: {done}/{total} ({(done/total*100) if total else 0:.1f}%)")
        [print(('✅' if r[3] else '⬜')+f" [{r[0]}] {r[1]}"+(f" @{r[2]}" if r[2] else '')) for r in rows]
    elif args.cmd=='export':
        rows=list_items(root); out=Path(args.out); out=out if out.is_absolute() else root/out
        export_json(rows,out) if args.format=='json' else export_md(rows,out); print(f"Exported: {out}")
    return 0

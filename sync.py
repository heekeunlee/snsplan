# 본 저장소의 할 일 목록(tools/report/todo.json)을 이 페이지용 todos.js로 옮긴다.
#   python3 sync.py [todo.json 경로]
# 공개 저장소이므로 보안·세금 등 개인적인 항목은 HIDE로 뺀다.
import json, os, sys
SRC = sys.argv[1] if len(sys.argv) > 1 else os.path.expanduser('~/projects/simulatiolab/tools/report/todo.json')
HIDE_ID = {'miner-check', 'adsense-apply'}
HIDE_WORD = ('채굴', 'miner', '세금', 'W-8BEN', '비밀번호', '열쇠', 'API 키')
d = json.load(open(SRC, encoding='utf-8'))
out = []
for t in d['items']:
    s = t.get('title', '') + t.get('why', '')
    if t['id'] in HIDE_ID or any(w in s for w in HIDE_WORD):
        continue
    out.append({k: t.get(k) for k in ('id', 'title', 'who', 'due', 'status', 'why', 'done')})
here = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(here, 'todos.js'), 'w', encoding='utf-8') as f:
    f.write('// sync.py가 만든 파일 — 직접 고치지 말고 본 저장소 todo.json을 고친 뒤 sync.py 실행\n')
    f.write('window.TODOS = ' + json.dumps({'updated': d.get('updated'), 'items': out}, ensure_ascii=False, indent=1) + ';\n')
print('todos.js', len(out), '개 (숨김', len(d['items']) - len(out), ')')

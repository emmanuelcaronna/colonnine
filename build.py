import json,datetime
t=open('template.html').read()
p=json.load(open('pagamento.json'))
t=t.replace('__GRATIS__',open('gratis.json').read()).replace('__PAG__',json.dumps(p,ensure_ascii=False)).replace('__NPAG__',str(len(p))).replace('__DATA__',datetime.date.today().strftime('%d/%m/%Y'))
open('index.html','w').write(t); print('ok',len(t))

#!/usr/bin/env python3
"""Gera index.html a partir de looks.json (que vem do Notion)."""
import json, html, pathlib, hashlib

root = pathlib.Path(__file__).parent
d = json.loads((root / "looks.json").read_text(encoding="utf-8"))
e = html.escape

def foto_url(caminho):
    """Foto local ganha ?v=<hash do arquivo>: quando a foto muda, o endereço muda e ninguém vê cópia antiga."""
    f = root / caminho
    if not caminho.startswith("http") and f.exists():
        return f"{caminho}?v={hashlib.md5(f.read_bytes()).hexdigest()[:8]}"
    return caminho

cards = []
for l in d["looks"]:
    badge = '<span class="badge">Em promoção</span>' if l.get("promocao") else ""
    cor = f' <span class="cor">· {e(l["cor"])}</span>' if l.get("cor") else ""
    cards.append(f"""
    <article class="card">
      <div class="foto">{badge}<img src="{e(foto_url(l['foto']))}" alt="{e(l['nome'])}" loading="lazy" referrerpolicy="no-referrer"></div>
      <div class="info">
        <p class="cat">{e(l.get('categoria',''))}</p>
        <h2>{e(l['nome'])}{cor}</h2>
        <a class="btn" href="{e(l['link'])}" target="_blank" rel="sponsored noopener">Comprar</a>
      </div>
    </article>""")

page = f"""<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(d['titulo'])} · @{e(d['instagram'])}</title>
<meta name="description" content="{e(d['subtitulo'])} — looks da Renner escolhidos por Nicole Dagostim.">
<style>
  :root {{ --bg:#faf6f3; --ink:#2a2224; --muted:#7d6f72; --acc:#b4415a; --card:#fff; }}
  * {{ box-sizing:border-box; margin:0; }}
  body {{ background:var(--bg); color:var(--ink); font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif; line-height:1.3; }}
  header {{ text-align:center; padding:18px 16px 10px; }}
  header h1 {{ font-family:Georgia,"Times New Roman",serif; font-size:22px; letter-spacing:.2px; }}
  header p {{ color:var(--muted); margin-top:3px; font-size:13px; }}
  main {{ max-width:640px; margin:0 auto; padding:6px 10px 20px; display:grid; gap:10px; grid-template-columns:repeat(2,1fr); }}
  @media (min-width:560px) {{ main {{ grid-template-columns:repeat(4,1fr); max-width:760px; }} }}
  .card {{ background:var(--card); border-radius:12px; overflow:hidden; box-shadow:0 1px 8px rgba(60,30,40,.08); display:flex; flex-direction:column; }}
  .foto {{ position:relative; aspect-ratio:4/5; background:#eee6e2; }}
  .foto img {{ width:100%; height:100%; object-fit:cover; display:block; }}
  .badge {{ position:absolute; top:6px; left:6px; background:var(--acc); color:#fff; font-size:10px; font-weight:600; padding:3px 7px; border-radius:99px; }}
  .info {{ padding:8px 9px 10px; display:flex; flex-direction:column; gap:6px; flex:1; }}
  .cat {{ display:none; }}
  h2 {{ font-size:12px; font-weight:600; flex:1; display:-webkit-box; -webkit-line-clamp:2; -webkit-box-orient:vertical; overflow:hidden; }}
  .cor {{ font-weight:400; color:var(--muted); }}
  .btn {{ display:block; text-align:center; background:var(--ink); color:#fff; text-decoration:none; font-weight:600; font-size:13px; padding:9px; border-radius:9px; }}
  .btn:active {{ background:var(--acc); }}
  footer {{ text-align:center; color:var(--muted); font-size:11px; padding:4px 20px 28px; max-width:520px; margin:0 auto; }}
</style>
</head>
<body>
<header>
  <h1>{e(d['titulo'])} 🛍️</h1>
  <p>{e(d['subtitulo'])} · <a href="https://instagram.com/{e(d['instagram'])}" style="color:inherit">@{e(d['instagram'])}</a></p>
</header>
<main>{''.join(cards)}
</main>
<footer>
  Os links desta página são de afiliada: se você comprar por eles, posso receber uma comissão, sem custo extra pra você. Preços e disponibilidade são os da Renner.
</footer>
</body>
</html>
"""
(root / "index.html").write_text(page, encoding="utf-8")
print("index.html gerado com", len(d["looks"]), "looks")

import pandas as pd

def to_proba(item):
    d = {x["label"]: x["score"] for x in item}
    return d.get("LABEL_1", d.get("1", 0.0))


def format_markdown(text_md):

    lines = []
    for l in text_md.split("\n"):

        if "<!--" in l:
            continue
        
        text = (l.replace("  ", " ")
              .replace("\t", " ")
              .replace("..", "")
              .replace("\\_", "")
              .replace("_", "")
              .replace("##", "")
              .strip(" "))
        
        while "  " in text:
            text = text.replace("  ", " ")
        
        if len(text) == 0:
            continue
        
        if text in lines:
            continue
        
        lines.append(text)
    text = "\n\n".join(lines)
    return text


def format_text(row):
    text_template = """Partido: {partido}; Genero: {genero}; UF: {uf}; Conteúdo: {texto}"""
    text = text_template.format(partido=row["partido"], genero=row["genero"], uf=row["uf"], texto=row["textInteiroTeorFormatFill"])
    return text


def df_transform(df):
    df = df.copy()
    df["id"] = df["id"].astype(str)
    df["textInteiroTeorFormat"] = df["textInteiroTeor"].apply(format_markdown)
    df["textInteiroTeorFormatFill"] = df["textInteiroTeorFormat"].replace("", pd.NA).fillna(df["ementa"])
    df["genero"] = df["genero"].apply(lambda x: x.upper() if pd.notna(x) else "")
    df["partido"] = df["partido"].fillna("")
    df["text"] = df.apply(format_text, axis=1)
    return df
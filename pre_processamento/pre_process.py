# %%
import os
import sys
import dotenv
dotenv.load_dotenv()

DATA_PATH = os.getenv("DATA_PATH")

import pandas as pd
from sklearn import model_selection

# %%

def format_markdown(text_md):

    lines = []
    for l in text_md.split("\n"):

        if "<!--" in l:
            continue
        
        text = (l.replace("  ", " ")
              .replace("\t", " ")
              .replace("..", "")
              .replace("\_", "")
              .replace("##", "")
              .strip(" "))
        
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


# %%

if DATA_PATH.endswith("xlsx"):
    df = pd.read_excel(DATA_PATH)

elif DATA_PATH.endswith("csv"):
    df = pd.read_csv(DATA_PATH)

else:
    print("Formato de arquivo não suportado. Use xlsx ou csv")
    sys.exit(1)


# %%

columns = {
    'casa':'casa',
    'id':'id',
    'uri':'uri',
    'codTipo':'codTipo',
    'Nome':'nome',
    'ano':'ano',
    'Ementa':'ementa',
    'urlInteiroTeor':'urlInteiroTeor',
    'textoInteiroTeor': 'textoInteiroTeor',
    'partido':'partido',
    'UF':'uf',
    'gênero':'genero',
    'Avaliação':'avaliacao',
    'Relevância':'relevancia',
    'Tema (class humana)':'tema',
}

df = (df[list(columns.keys())].rename(columns=columns)
                              .drop_duplicates(subset=["nome"], keep="first")
                              .dropna(subset=["nome"])
                              .reset_index(drop=True))

# %%
df_abt = df.copy()
df_abt["id"] = df_abt["id"].astype(str)
df_abt["textoInteiroTeor"] = df_abt["textoInteiroTeor"].apply(format_markdown)
df_abt["textoInteiroTeorFormatFill"] = df_abt["textoInteiroTeor"].replace("", pd.NA).fillna(df_abt["ementa"])
df_abt["genero"] = df_abt["genero"].apply(lambda x: x.upper() if pd.notna(x) else "")
df_abt["partido"] = df_abt["partido"].fillna("")
df_abt["fl_desfavoravel"] = (df_abt["avaliacao"] == 'Desfavorável').astype(int)
df_abt["textFormat"] = df_abt.apply(format_text, axis=1)

# %%

X = df_abt[["textFormat", "tema"]]
y = df_abt["fl_desfavoravel"]

X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y,
                                                                    test_size=0.1,
                                                                    random_state=42,
                                                                    stratify=y,
                                                                    )


X_train, X_val, y_train, y_val = model_selection.train_test_split(X_train, y_train,
                                                                    test_size=0.2,
                                                                    random_state=42,
                                                                    stratify=y_train,
                                                                    )


print("Tamanho do treino:", X_train.shape[0])
print("Tamanho do validação:", X_val.shape[0])
print("Tamanho do teste:", X_test.shape[0])

print("Taxa resposta do treino:", y_train.mean())
print("Taxa resposta do validação:", y_val.mean())
print("Taxa resposta do teste:", y_test.mean())
# %%

df_train = pd.DataFrame({"textFormat": X_train["textFormat"], "tema": X_train["tema"], "fl_desfavoravel": y_train})
df_val = pd.DataFrame({"textFormat": X_val["textFormat"], "tema": X_val["tema"], "fl_desfavoravel": y_val})
df_test = pd.DataFrame({"textFormat": X_test["textFormat"], "tema": X_test["tema"], "fl_desfavoravel": y_test})

df_train.to_parquet("../dados/train.parquet", index=False)
df_val.to_parquet("../dados/validation.parquet", index=False)
df_test.to_parquet("../dados/test.parquet", index=False)
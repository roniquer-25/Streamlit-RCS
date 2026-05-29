import streamlit as st
import pandas as pd

st.set_page_config(page_title="Finanças", page_icon="🚀")

st.markdown("""
# Boas vindas!

## Nosso App Finaceiro!  

Traremos a melhor solução finaceira para você.          

            """)

# Widget de upload de dados
file_upload = st.file_uploader(label="Faça o upload dos dados aqui", type=['csv'])

# Verificar se algum arquivo foi feito upload
if file_upload:

    # Leitura dos dados
    df = pd.read_csv(file_upload, sep=";")
    df["Data"] = pd.to_datetime(df["Data"], format="%d/%m/%Y").dt.date
    
    # Exibição dos dados no App
    exp1 = st.expander("Dados Brutos")
    columns_fmt = {"Valor":st.column_config.NumberColumn("valor", format="R$ %f")}
    exp1.dataframe(df, hide_index=True, column_config=columns_fmt)

    # Visão instituição
    exp2 = st.expander("Instituições")
    df_instituicao = df.pivot_table(index="Data", columns="Instituição", values="Valor")

    # Abas para diferentes visualizações
    tab_data, tab_history, tb_share = exp2.tabs(["Dados", "Histórico", "DIstribuição"]) 

    # Exibe DataFrame
    tab_data.dataframe(df_instituicao)

     # Exibe Data
    with tab_data:
        st.dataframe(df_instituicao)
    
    # Exibe Histórico
    with tab_history:
        st.line_chart(df_instituicao)
    
    # Exibe Distribuição
    with tb_share:

        # Filtro de data
        date = st.selectbox("Filtro Data", options=df_instituicao.index)

        # Gráfico de distribuição
        st.bar_chart(df_instituicao.loc[date])

        
        


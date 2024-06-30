import streamlit as st
import pandas as pd

# Título da aplicação
st.title('Minha Carteira de Ações')

# DataFrame inicial vazio para armazenar as ações
carteira = pd.DataFrame(columns=['Símbolo', 'Quantidade', 'Preço de Compra'])

# Função para adicionar ação à carteira
def adicionar_acao(symbol, quantity, purchase_price):
    global carteira
    carteira = carteira.append({
        'Símbolo': symbol,
        'Quantidade': quantity,
        'Preço de Compra': purchase_price
    }, ignore_index=True)

# Função para calcular o preço médio da carteira
def calcular_preco_medio():
    global carteira
    if not carteira.empty:
        preco_medio = (carteira['Quantidade'] * carteira['Preço de Compra']).sum() / carteira['Quantidade'].sum()
        return preco_medio
    else:
        return None

# Função para exibir a carteira completa
def exibir_carteira():
    st.subheader('Carteira Atualizada')
    st.write(carteira)

# Barra de navegação
menu = ['Minha Carteira', 'Adicionar Ações', 'Calcular Preço Médio']
choice = st.sidebar.selectbox('Menu', menu)

# Lógica para as opções do menu
if choice == 'Minha Carteira':
    exibir_carteira()
elif choice == 'Adicionar Ações':
    st.subheader('Adicionar Ações à Carteira')
    symbol = st.text_input('Digite o símbolo da ação (ex: AAPL para Apple)')
    quantity = st.number_input('Digite a quantidade de ações', min_value=1)
    purchase_price = st.number_input('Digite o preço de compra por ação', min_value=0.01)
    
    if st.button('Adicionar à Carteira'):
        adicionar_acao(symbol, quantity, purchase_price)
        st.success('Ação adicionada com sucesso!')
        exibir_carteira()

elif choice == 'Calcular Preço Médio':
    st.subheader('Calcular Preço Médio da Carteira')
    preco_medio = calcular_preco_medio()
    if preco_medio is not None:
        st.write(f'O preço médio da carteira é: R$ {preco_medio:.2f}')
    else:
        st.warning('A carteira está vazia. Adicione ações primeiro.')

# Rodapé
st.info('Desenvolvido por Tiago F. Holanda')

# Panda, Panda, Panda, Panda, Panda I got broads in Atlanta
import pandas as pd

# Link from where the tickers will be scraped
page = "https://www.infomoney.com.br/cotacoes/empresas-b3/"

# Read the tables with the tickers
tables = pd.read_html(page) # Returns list of all tables on page

# Concat
tickers = pd.DataFrame()
for i in tables:
    tickers = tickers.append(i, ignore_index=True)

# Rename columns
columns = []

for i in range(1,len(tickers.columns)):
    columns.append('Ativo' + str(i))

columns.insert(0,'Empresa')

tickers.columns = columns

# Save in a CSV
tickers.to_csv('tickers.csv', index=False)
import requests
import os

def download_data(league_name, years, league_codes):
    base_url = 'https://www.football-data.co.uk/mmz4281/'
    base_path = 'C:/Users/Gabriel Lima/Documents/github/FootballScrapeML/Historical'

    # Check if the base directory exists, if not, create it
    # Verifica se o diretório base existe, se não existir, cria-o
    if not os.path.exists(base_path):
        os.makedirs(base_path)

    # Iterate over the years and league codes to download data
    # Itera sobre os anos e códigos das ligas para baixar os dados
    for year in years:
        for league_code, league_label in league_codes.items():
            file_name = f'{league_label} - {year}.csv'
            file_path = os.path.join(base_path, file_name)

            # Construct the URL for the data file
            # Constrói a URL para o arquivo de dados
            url = f"{base_url}{year[:2]}{year[3:]}/{league_code}.csv"
            response = requests.head(url)

            # Check if the file exists on the server
            # Verifica se o arquivo existe no servidor
            if response.status_code == 200:
                try:
                    # Download the file and save it
                    # Baixa o arquivo e o salva
                    response = requests.get(url)
                    response.raise_for_status()  # Check for HTTP request errors
                    with open(file_path, 'wb') as f:
                        f.write(response.content)
                    print(f'File {file_name} downloaded successfully.')
                except requests.exceptions.RequestException as e:
                    print(f'Failed to download {file_name}: {e}')
            else:
                print(f'The file {file_name} does not exist on the server. It was not downloaded.')

def search():
    # Define the years to search for data
    # Define os anos para procurar os dados
    years = ['93-94', '94-95', '95-96', '96-97', '97-98', '98-99', '99-00',
             '00-01', '01-02', '02-03', '03-04', '04-05', '05-06', '06-07',
             '07-08', '08-09', '09-10', '10-11', '11-12', '12-13', '13-14',
             '14-15', '15-16', '16-17', '17-18', '18-19', '19-20', '20-21', '21-22', '22-23']

    # Define the league codes and their respective labels
    # Define os códigos das ligas e seus respectivos rótulos
    league_codes = {
        "E0": "Premier League",
        "E1": "Championship",
        "E2": "League 1",
        "E3": "League 2",
        "EC": "Conference",
        "SC0": "Premier League (Scotland)",
        "SC1": "Division 1 (Scotland)",
        "SC2": "Division 2 (Scotland)",
        "SC3": "Division 3 (Scotland)",
        "D1": "Bundesliga",
        "D2": "Bundesliga 2",
        "I1": "Serie A",
        "I2": "Serie B",
        "SP1": "La Liga",
        "SP2": "La Liga 2",
        "F1": "Ligue 1",
        "F2": "Ligue 2",
        "N1": "Eredivisie",
        "B1": "Jupiler League",
        "P1": "Liga Portugual",
        "T1": "Super Lig",
        "G1": "Super League (Greece)"
    }

    # Call the download_data function with the defined parameters
    # Chama a função download_data com os parâmetros definidos
    download_data("Football", years, league_codes)

if __name__ == "__main__":
    search()

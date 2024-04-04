info = {
  'times': {
    'Corinthians': ['Copa do Brasil', 'Libertadores', 'Mundial'],
    'Palmeiras': ['Libertadores', 'Copa do Brasil', 'Sem Mundial'],
    'Flamengo': ['Libertadores', 'Taça Rio', 'Mundial'],
    'Vasco': ['Libertadores', 'Taça Guanabara', 'Mundial']}
}

def Visual(separador = '.'):
  print(separador * 20)
  print(separador * 20)



for time in info['times']:
  print(f"\033[1;33mTime:\033[m {time}")
  print(f"\033[4;37mTítulos:\033[m {info['times'][time]}")
  Visual()


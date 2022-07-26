pais = [
    'Equador', 'Holanda', 'Qatar', 'Senegal', 'Inglaterra', 'Irã', 'Pais de Gales', 'Estados Unidos America',
    'Arábia Saudita', 'Argentina', 'México', 'Polônia', 'Austrália', 'Dinamarca', 'França', 'Tunísia',
    'Alemanha', 'Costa Rica', 'Espanha', 'Japão', 'Bélgica', 'Canadá', 'Croácia', 'Marrocos',
    'Brasil', 'Camarões', 'Sérvia', 'Suíça', 'Coreia do Sul', 'Gana', 'Portugal', 'Uruguai'
]

for align, text in zip('<^>', ['left', 'center', 'right']):
    print('{0:{fill}{align}16}'.format(text, fill=align, align=align))

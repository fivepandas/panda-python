cities = {
    'beijing' : {'country':'china',
                 'population' : 3000,
                 'fact' : 'beijing is the capital of china'},
    'shanghai' : {'country':'china',
                 'population' : 3000,
                 'fact' : 'shanghai is the chinese economical center'
    },
    "chengdu" : {
        'country':'china',
        'population' : 2000,
        'fact' : 'chengdu has panda'
    }
}
for city , infos in cities.items():
    print(f"{city} blongs to:{infos['country']}")

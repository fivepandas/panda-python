unprinted_designs = ['phone case','robot pendant','dodecahedron']
complete_models = []
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f'Printing model : {current_design}')
    complete_models.append(current_design)
print("\nThe following models have been printed:")
for complete_model in complete_models:
    print(complete_model)
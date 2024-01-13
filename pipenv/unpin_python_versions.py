import toml

# Load Pipfile as a dictionary
with open('Pipfile', 'r') as file:
    pipfile_data = toml.load(file)

sections_to_change = ['packages', 'dev-packages']

for section in sections_to_change:
  if section in pipfile_data:
    for package, version in pipfile_data[section].items():
      pipfile_data[section][package] = "*"

# Save the modified Pipfile
with open('Pipfile', 'w') as file:
    toml.dump(pipfile_data, file)
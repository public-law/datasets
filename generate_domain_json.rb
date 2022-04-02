#!/usr/bin/env ruby
require 'yaml'
require 'json'

# Generate the JSON file from the YAML source.

data = YAML.load_file 'governmental_domains.yaml'
json_text = JSON.pretty_generate(data)

File.write("governmental_domains.json", json_text)
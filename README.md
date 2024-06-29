# Prompt test data
This is a repository containing test data for a number of markup and programming languages It also contains a
set of prompts to generate test data for each of the targets identified in the dataset.

## Fuzzing target test data

Test data for the following targets: 
1. [Python](test%20files/python#readme)
2. [PHP](/test%20files/php/README.md)
3. [Text files](/test%20files/txt/README.md)
4. [YAML](/test%20files/yaml/README.md)
5. [XML](/test%20files/xml/README.md)
6. [SQL](/test%20files/sql/README.md)
7. [Javascript](/test%20files/js/README.md)
8. [JSON](/test%20files/json/README.md)
9. [C](/test%20files/c/README.md)

## Generated Prompts
There are twenty unique prompts for each target. Each prompt has a unique identifier in the format: specification:template_id:error_id[:promptchaining_id]

**Specification** - The markup language or programming language samples will be generated for.
**template_id** - The particular template used to create the prompt
**error_id** - A potential error statement added to the prompt
**promptchaining_id** - There is an additional prompting statement to further mutate the output.
The 

- [prompts.parquet](test@20files/prompts.parquet)

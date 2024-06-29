from string import Template
from pathlib import Path
from collections import namedtuple

from pandas import DataFrame

from prompt_templates import text_ss, text_fs, code_ss, code_fs, code_pc, text_pc

errors = [
    "",
    " The example should include a syntax error.",
    " The example should include a semantic error.",
    " The example should include a common error for this format.",
]
formal_name = {
    "c": "C",
    "js": "Javascript",
    "json": "JSON",
    "php": "PHP",
    "python": "Python",
    "sql": "SQL",
    "txt": "text",
    "xml": "xml",
    "yaml": "yaml",
}


my_test_files = {
    "c": ["main.c", "test.c"],
    "js": [
        "regress-crbug-1006592.js",
        "debug.js",
    ],
    "json": [
        "package.json",
        "ref-and-defs.json",
    ],
    "php": [
        "file2.php",
        "file1.php",
    ],
    "python": [
        "file1.py",
        "file5.py",
    ],
    "sql": [
        "02-04.sql",
        "04-05.sql",
    ],
    "txt": [
        "file1.txt",
        "file0.txt",
    ],
    "xml": [
        "simpleCSV.xml",
        "csv.cfg.xml",
    ],
    "yaml": [
        "deployment.yaml",
        "tags.yaml",
    ],
}

symbols = {
    "c": "//",
    "js": "//",
    "json": "",
    "php": "//",
    "python": "#",
    "sql": "--",
    "txt": "",
    "xml": "",
    "yaml": "#",
}


def get_examples(format_folder: str):
    folder = Path(format_folder)

    file1, file2 = my_test_files[format_folder]

    with open(folder / file1, "r") as ex1:
        example1 = ex1.read()

    with open(folder / file2, "r") as ex2:
        example2 = ex2.read()

    return (example1, example2)


Format = namedtuple(
    "Input", ["fml_name", "comment_symbol", "testfiles", "prompt_templates"]
)

formats = []
for f_name in formal_name:
    if f_name in ["c", "js", "php", "python", "sql"]:
        formats.append(
            Format(
                formal_name[f_name],
                comment_symbol=symbols[f_name],
                testfiles=get_examples(f_name),
                prompt_templates=(code_ss, code_fs, code_pc),
            )
        )
    else:
        formats.append(
            Format(
                formal_name[f_name],
                comment_symbol=symbols[f_name],
                testfiles=get_examples(f_name),
                prompt_templates=(text_ss, text_fs, text_pc),
            )
        )

from pprint import pp


def create_prompts(input_fmt: Format, error_list: list):
    # pp(input_fmt)
    name, cmt_sbl, file_text_list, templates = input_fmt

    prompt_list = []
    for tid, template in enumerate(templates):
        t = Template(template=template)
        for eid, error_val in enumerate(error_list):
            substituted = t.substitute(
                code=name,
                example1=file_text_list[0],
                example2=file_text_list[1],
                comment=cmt_sbl,
                error=error_val,
            )
            if tid == 2:
                prompt_list.append(
                    (f"{name}:template{tid}:error{eid}",)
                    + tuple(substituted.splitlines())
                )
            else:
                prompt_list.append((f"{name}:template{tid}:error{eid}", substituted))
                prompt_list.append(
                    (
                        f"{name}:template{tid}:error{eid}:pc",
                        substituted,
                        "Without explanatory text use the example generated above to create another example.",
                    )
                )

    return prompt_list


prompts = []
for a_format in formats:
    prompts.extend(create_prompts(a_format, errors))

from pprint import pp

pp(prompts)
pp(len(prompts))

prompt_df = DataFrame(prompts, columns=['id','prompt0','prompt1'])
prompt_df.to_parquet('prompts.parquet')

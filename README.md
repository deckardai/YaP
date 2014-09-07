
# Design Goals

## Safe:

Syntax independent of variables content. Well-defined data structure.
Not based on spaces in variables, quotes, escaping. No empty strings on unknown variables.
Check that all executables are there before even starting.

## Easy:

Mix Python and Bash freely. Solve each task with the best suited
language. Conversion of string for common patterns (read lines, read fields).

## Powerful:

All the power of Python for logic and of Bash for system
interaction.

## Simple:

Single file, no-dependencies compiler. On-the-fly or pre-compiled to
pure Python.

## Readable:

Avoid quotes and escaping hell. Common functions and patterns
readily available: os, sys.argv[1] as $1, $env_var, listdir, re.*
Command interpolation.


# Syntax:

## Output

* Default: Capture stdout, print stderr
    some_python = 'full output: ' + ! shell command

    some_integer = 2 + i! echo 2
    return_code = c! false
    stdout, stderr, return_code = sec! false
    list_of_lines = l! ls
    rows_then_fields = f! ls -l
    fields_then_rows = r! ls -l
    json = j! ls -l
    print(!(date +%s))

    output = !input|(wc)
    output = se!input| wc

    ! echo { some_python.upper() }
    ! echo $env_variable
    print($env_variable)
    if $1 == "first argument": pass
    $unset_env_variable is None
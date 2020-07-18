# Bysh

Bash interpreter in Python

Continuation of <https://github.com/idank/bashlex>. The bashlex files may have been modified.

## Notes

### tkt

|| & && ; ;; ( ) | \n

- Simple Command
    - Noms separes par des espaces (+redirections) + control operator
- Pipeline
    - Simple commands séparées par des pipes
- List
    - pipelines séparées par des control operators
- Compound Commands
    - list mais avec des infos en plus
        - {} -> execute dans current shell
        - () -> execute subshell
        - (()) -> arithmetic
        - [[ ]] -> tests
- Shell functions
    - fonctions

### stdin

Plus tard il faudra  
msvcrt.getche() in (b'\x00', b'\xe0'):  
<https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/getch-getwch?view=vs-2019>

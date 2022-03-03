# Subset of UML language
Using EBNF (Extended Backus-Naur Form) as in USE


## Useful commands:

### Output formats for graphviz (dot)
    https://graphviz.org/docs/outputs/

### To re-generate metamodel uml.dot and to visualize in PDF
    rm uml.dot || textx generate uml.tx --target dot &&  dot -Tpdf uml.dot -o uml.pdf && open uml.pdf

### To generate any .model in PDF
    Example company.model:
    rm company.dot || textx generate company.model --grammar uml.tx --target dot &&  dot -Tpdf company.dot -o company.pdf && open company.pdf

    Example graph.model:
    rm graph.dot || textx generate graph.model --grammar uml.tx --target dot &&  dot -Tpdf graph.dot -o graph.pdf && open graph.pdf

## Other people work:

    I used textX for metamodeling:
        https://github.com/textX/textX

    Also I look into UML-based Specification Environment (USE) to copy follow UML syntax:
        https://github.com/useocl/use
    
    By doing that I end up using EBNF:
        https://en.wikipedia.org/wiki/Extended_Backus%E2%80%93Naur_form
# compiler/semantic.py

def semantic_check(tokens):
    declared_vars = set()
    
    for i, (token_type, token_value, line_no) in enumerate(tokens):
        if token_type == 'KEYWORD' and token_value in ['int', 'float']:
            # e.g., int x;
            if i+1 < len(tokens) and tokens[i+1][0] == 'IDENTIFIER':
                declared_vars.add(tokens[i+1][1])
        
        if token_type == 'IDENTIFIER':
            if token_value not in declared_vars:
                raise NameError(f"Variable '{token_value}' used without declaration at line {line_no}")
    
    return "Semantic Check OK"

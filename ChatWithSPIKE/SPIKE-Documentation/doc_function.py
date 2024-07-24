def doc(path):
    parts = path.rsplit('.', 2)
    if len(parts) == 3:
        _, module_name, function_name = parts
    elif len(parts) == 2:
        module_name, function_name = parts
    else:
        module_name = parts[0]
        function_name = None
    
    if function_name:
        
        module = __import__("modules." + module_name, None, None, ['functions'])
       
        functions = module.functions
        print(functions.get(function_name, f"No documentation available for {path}"))
    else:
        from doc_strings import doc_data
        print(doc_data.get(module_name, f"No documentation available for {module_name}"))
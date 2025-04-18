# Función principal para validar HTML
def is_html_balanced(html: str) -> bool:
    import re
    tag_pattern = re.compile(r'<\s*(/?)([a-zA-Z0-9]+)[^>]*?(/?)\s*>')
    stack = []

    for match in tag_pattern.finditer(html):
        is_closing, tag_name, is_self_closing = match.groups()
        tag_name = tag_name.lower()

        if is_self_closing:
            continue
        elif is_closing:
            if not stack or stack[-1] != tag_name:
                return False
            stack.pop()
        else:
            stack.append(tag_name)

    return not stack

#TEST
def test_html_balancer():
    assert is_html_balanced("<div><p>Hello</p></div>") == True
    assert is_html_balanced("<div><p>Texto</div>") == False
    assert is_html_balanced("<div><img src='x.png' /></div>") == True
    print("✅ Todos los test cases pasaron correctamente.")


test_html_balancer()

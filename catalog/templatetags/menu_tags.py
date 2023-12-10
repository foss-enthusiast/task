from django import template
from catalog.models import Item, Menu, Node

from django.utils.html import mark_safe

from urllib import parse


register = template.Library()


@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    # Получить текущий URL страницы
    current_url = context['request'].get_full_path()

    # Парсим аргументы url
    raw_url_arguments = parse.urlsplit(current_url).query
    parsed_url_arguments = parse.parse_qs(raw_url_arguments)

    # Берём значение аргумента menu_name из url
    active_node_link = parsed_url_arguments.get(menu_name, menu_name)[0]

    path_to_node = active_node_link.split('/')
    
    # Берём меню из базы меню по названию
    menu = Menu.objects.get(title=menu_name)
    
    return mark_safe(build_tree(menu, path_to_node, current_url))


def build_tree(node: Node, path_to_node, current_url):
    """
    node: корневой элемент.
    path_to_node: путь от корневого элемента до активного элемента
    
    Функция рекурсивно строит дерево, где узел это объект модели Node
    """

    node_link = get_node_link(node, current_url)
    is_active = len(path_to_node) == 1

    node_html = '<ul>'
    node_html += f'<li class="{"active" if is_active else "inactive"}"><a href="{node_link}">{node.title}</a></li>'

    childs = node.child_nodes.all()

    if len(path_to_node) > 1:
        del path_to_node[0]

        for child in childs:
            if path_to_node[0] == child.title:

                node_html += build_tree(child, path_to_node, current_url)
                break

    elif is_active:
        node_html += '<ul>'
        for child in childs:
            child_node_link = get_node_link(child, current_url)
            node_html += f'<li><a href="{child_node_link}">{child.title}</a>'

        node_html += '</ul>'


    node_html += '</ul>'
    return node_html
 

def get_node_link(node: Node, current_url):
    path_to_node = [node.title]

    while hasattr(node, 'parent_node'):
        node = node.parent_node
        path_to_node.append(node.title)

    path_to_node = reversed(path_to_node)

    url_parts = list(parse.urlparse(current_url))
    query = dict(parse.parse_qsl(url_parts[4]))

    query[node.menu_name] = '/'.join(path_to_node)

    url_parts[4] = parse.urlencode(query)
    
    return parse.urlunparse(url_parts)


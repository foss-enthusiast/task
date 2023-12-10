from django.db import models


class Node(models.Model):
    title = models.CharField(max_length=255, default='')
    menu_name = models.CharField(max_length=255, default='')
    
    def __str__(self):
        return self.title


class Menu(Node):
    pass


class Item(Node):

    parent_node = models.ForeignKey(Node, null=True, blank=True, on_delete=models.CASCADE, related_name='child_nodes')


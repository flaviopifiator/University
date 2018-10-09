from django.apps import AppConfig

from suit.apps import DjangoSuitConfig
from suit.menu import ParentItem, ChildItem


class CoreConfig(AppConfig):
    name = 'core'


class SuitConfig(DjangoSuitConfig):
    layout = 'vertical'
    menu_show_home = False

    menu = (
        ParentItem('General', url='/admin/general/', icon='fa fa-globe'),

        ParentItem('Universidades', children=[
            ChildItem(model='universidad.universidad'),
            ChildItem(model='universidad.aula'),
            ], icon='fa fa-fort-awesome',
        ),

        ParentItem('Facultades', children=[
            ChildItem(model='facultad.facultad'),
            ChildItem(model='facultad.departamentofacultad'),
            ChildItem(model='facultad.carrera'),
            ChildItem(model='facultad.profesor'),
            ChildItem(model='facultad.planestudio'),
            ], icon='fa fa-institution',
        ),

        ParentItem('Materias', children=[
            ChildItem(model='materia.materia'),
            ChildItem(model='materia.horariomateria'),
            ChildItem(model='materia.modoprofesor'),
            
        ], icon='fa fa-plus'),
        
        ParentItem(
            'Administración de Usuarios',
            url='/admin/user/',
            children=[
                ChildItem(model='user.user'),
                ChildItem(model='auth.group'),
            ],
            icon='fa fa-cog',
            permissions=('auth.add_user', )
        )
        
    )

from kivy.lang import Builder
from kivy.app import runTouchApp
runTouchApp(Builder.load_string('''
#:include kvext.kv

#:import Factory kivy.factory.Factory
#:import r random.random

BoxLayout:
    orientation: 'vertical'
    BoxLayout:
        BoxLayout:
            orientation: 'vertical'
            Button:
                text: '_for'
                on_release: _for(5, print, (str(r()), ))
            Button:
                text: '_forc'
                on_release: _forc(5, print, r)
        BoxLayout:
            orientation: 'vertical'
            Button:
                text: '_forw'
                on_release:
                    _forw(grid, 5, Factory.ForWidget, {'text': 'Hello!'})
            Button:
                text: '_forws'
                on_release:
                    _forws(grid, [
                    [Factory.Spinner, {}], [Factory.Button, {'text':'blob'}],
                    [Factory.Label, {'color': (1, 0, 0, 1), 'text':'blob'}]])
            Button:
                text: 'clear grid'
                on_release: grid.clear_widgets()
        BoxLayout:
            orientation: 'vertical'
            Button:
                id: id_a
                text: 'a'
            Button:
                id: id_b
                text: 'b'
            Button:
                id: id_c
                text: 'c'
            Button:
                id: id_d
                text: 'd'
        BoxLayout:
            orientation: 'vertical'
            Button:
                text: 'swap a<->d'
                on_release: _swapw(id_a, id_d)
            Button:
                text: 'swap b<->c'
                on_release: _swapw(id_b, id_c)
    GridLayout:
        id: grid
        cols: 20

<ForWidget@ButtonBehavior+Label>:
    on_parent: self.dummy += 1
    dummy: 0
    on_dummy: if self.dummy <= 2: _forw(self.parent, 6, Factory.Button)
'''))

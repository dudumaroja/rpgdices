import flet as ft
import dadoflet as dd

def main(page: ft.Page):
    c1=ft.Container (
        content=ft.Text("Dados para RPG",text_align='CENTER', size='24'),
        margin=10,
        padding=10,
        alignment=ft.alignment.center,
        width=150,
        height=150,
        border_radius=10,
    )
    l = ft.Text('4')
    q = ft.Text('1')
    r = ft.Text('\nAguardado usuário',text_align='CENTER')

    def l_dados(e):
        l.value = e.control.value
        page.update()

    def q_dados(e):
        q.value = e.control.value
        page.update()

    def arremessa(e):
        r.value = dd.joga_dados(int(l.value) , int(q.value))
        page.update()

    page.title = "Dados Para RPG"
    page.padding = 30
   # page.window_width = 100
    page.window_width = 270
    l_titulo = ft.Text("Quantos lados tem os Dados?")
    q_titulo = ft.Text("Quantos Dados lançar?")
    button = ft.Container ( content=ft.ElevatedButton("Rolar Dados", on_click = arremessa ),
                   alignment=ft.alignment.center,
                   padding=10
                )



    page.add(c1,l_titulo,
             ft.Slider( min=4, max=20, divisions=16, label="{value} Lados", on_change=l_dados),
             q_titulo,
             ft.Slider(min=1, max=11, divisions=10, label="{value} Dados", on_change=q_dados) ,
             button, r)


ft.app( target=main)


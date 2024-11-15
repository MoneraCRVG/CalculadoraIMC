import flet as ft

def main(page: ft.Page):
    page.title = "Calculadora IMC"

    altura_field = ft.TextField(label="Informe a altura")
    peso_field = ft.TextField(label="Informe o peso")
    result_text = ft.Text(
        value="Insira as informações para começar!",
        size=22,
        width=150
    )

    result_img = ft.Image(src="src/img.png", width=150, height=150)
    page.add(result_text, result_img, altura_field, peso_field)


ft.app(main)
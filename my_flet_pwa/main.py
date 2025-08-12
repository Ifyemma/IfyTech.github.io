import flet as ft

def main(page: ft.Page):
    page.title = "Flet PWA from Codespaces"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Make app installable as PWA
    #page.pwa = True

    page.add(
        ft.Text("🚀 Hello from Flet in GitHub Codespaces (PWA Mode)!", size=25, weight="bold"),
        ft.ElevatedButton("Click Me", on_click=lambda e: page.add(ft.Text("You clicked the button!"))))

ft.app(target=main, view=ft.WEB_BROWSER)
    
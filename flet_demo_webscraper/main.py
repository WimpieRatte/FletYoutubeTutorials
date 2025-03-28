import flet as ft
from flet import Page, Column, Text, TextField, ElevatedButton  # https://flet.dev/docs/controls
import requests
import json

def main(page: Page):
    page.title = "Web Scraper"
    
    url_field = TextField(value="", hint_text="URL", text_align="left", autofocus=True)
    result_txt = Text(value="", text_align="left")
    
    def scrape(e):
        """Scrape button click"""
        url = url_field.value
        url_field.value = ""
        
        response = requests.get(url)  # send get request
        json_data = json.loads(response.text)  # convert json string to dictionary
        
        names = [item["name"] for item in json_data]  # get names
        
        result_txt.value = "\n".join(names)  # names to string
        
        page.update()  # update UI
    
    page.add(
        Column(
            [
                url_field,  # when adding widgets, we can save widgets in a variable first
                ElevatedButton(text="Scrape", on_click=scrape),  # or insert them directly
                ft.Divider(),  # can insert without importing first
                result_txt,
            ]
        )
    )

ft.app(target=main, port=8550)  # execute given function on specific port to start Flet app
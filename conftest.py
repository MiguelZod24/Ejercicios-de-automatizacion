import re
import time
import random
import pytest
from playwright.sync_api import Page, expect, Playwright, sync_playwright

tiempo = 3
ruta= "Estudiantes/mv_estudiantes/Imagenes/"
foto1 = "C:/Users/migue/Desktop/Curso-Playwright/aficiones.png"
url = "https://demoqa.com/automation-practice-form"

@pytest.fixture(scope="function")
def set_up(playwright:Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context=browser.new_context(
        viewport={'width':1500, 'height':800}
        #record_video_dir="Videos/checkbox"
    )
    #Inicia Trace Viewer
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()
    page.goto(url)
    page.set_default_timeout(5000)
    #Cierre de Trace Viewer:
    context.tracing.stop(path="trace.zip")
    yield page
    context.close()
    browser.close()





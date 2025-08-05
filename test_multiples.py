import re
import time
import pytest
from playwright.sync_api import Page, expect, Playwright, sync_playwright
from funciones import Funciones_Globales

# PARA OBTENER EL REPORTE:
#pytest -s -v test_multiples.py -n 6 --html=report.html

# Generar reporte con captura:
# pytest -s -v test_multiples.py -n 6 --html=report_2.html --capture=tee-sys

# Generar reportes con graficos chulos:
# pytest test_multiple.py -s -v -n 6 --template=html1/index.html --report=reporte_tres.html

# pytest --headed test_multiples.py -s -v
# pytest --headed test_multiples.py::test_checkbox

# Primero se crea al archivo .zip y luego se corre el comando
# Comando para correr Trace Viewer:
# playwright show-trace trace.zip

# Variables globales
tiempo = 3
ruta= "Estudiantes/mv_estudiantes/Imagenes/"
foto1 = "C:/Users/migue/Desktop/Curso-Playwright/totti.png"


def test_multiples(set_up) -> None:
    page=set_up
    # Creando nuestro objeto de tipo Funciones Globales:
    F=Funciones_Globales(page)
    #time.sleep(1)
    page.mouse.wheel(0,400) # Coordenadas X y Y, X=0 Y=400
    F.Scroll_xy(0,400)
    F.Esperar(tiempo)
    

def test_carga_textos(set_up) -> None:
    page = set_up
    # Creando nuestro objeto de tipo Funciones Globales:
    F=Funciones_Globales(page)
    #time.sleep(1)
    page.mouse.wheel(0,400) # Coordenadas X y Y, X=0 Y=400
    F.Scroll_xy(0,400)
    F.Esperar(tiempo)

    #Textos 
    F.Campos_de_texto_img("//input[@id='firstName']", "Jack", ruta+"nombre.png")
    F.Campos_de_texto_img("//input[@id='lastName']", "Alejandro", ruta+"apellido.png")
    F.Campos_de_texto_img("//input[@id='userEmail']", "pruebas@gmail.com", ruta+"email.png")
    F.Campos_de_texto_img("//input[@id='userNumber']", "2365984122", ruta+"telefono.png")
    F.Campos_de_texto_img("//textarea[@id='currentAddress']", "Direccion falsa 1", ruta+"direccion.png")
    F.Campos_de_texto_img("input[id='subjectsInput']", "Futbol y Musica", ruta+"aficiones.png")
    

def test_checkbox(set_up) -> None:
    page = set_up
    # Creando nuestro objeto de tipo Funciones Globales:
    F=Funciones_Globales(page)
    #time.sleep(1)
    page.mouse.wheel(0,400) # Coordenadas X y Y, X=0 Y=400
    F.Scroll_xy(0,400)
    F.Esperar(tiempo)

    # Check box:
    F.Click_img("//label[.='Music" \
    "']", ruta+"check.png", tiempo)
    # Radio button:
    F.Click("//label[.='Male']", tiempo)
    # Calendario:
    F.Seleccionar_fecha(año="2000", mes=7, dia=19)

   
#@pytest.mark.skip(reason="Este modulo esta inhabilitado")
def test_upload(set_up) -> None:
    page = set_up
    # Creando nuestro objeto de tipo Funciones Globales:
    F=Funciones_Globales(page)
    #time.sleep(1)
    page.mouse.wheel(0,400) # Coordenadas X y Y, X=0 Y=400
    F.Scroll_xy(0,400)
    F.Esperar(tiempo)

    # Cargar archivos:
    F.Upload_file("//input[@id='uploadPicture']", foto1,tiempo)

    # Textos (obligatorios):
    F.Campos_de_texto_img("//input[@id='firstName']", "Jack", ruta+"nombre.png")
    F.Campos_de_texto_img("//input[@id='lastName']", "Alejandro", ruta+"apellido.png")
    F.Campos_de_texto_img("//input[@id='userNumber']", "2365984122", ruta+"telefono.png")
    
    # Radio button (obligatorio):
    F.Click("//label[.='Male']", tiempo)
    
    # Combos box:
    F.Combo_value("#state", "Haryana", tiempo)
    F.Combo_value("#city", "Karnal", tiempo)

    F.Click_submit()

    # Validar Modal:
    Funciones_Globales(page).Validar_texto_modal("#example-modal-sizes-title-lg", "Thanks for submitting the form")
   
    # Validar URL: 
    F.Validar_url("https://demoqa.com/automation-practice-form", tiempo=0.3)
    
    

    
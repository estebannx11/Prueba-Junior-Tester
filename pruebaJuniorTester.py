import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def creacion_usuario():
    #Abrir el navegador Firefox
    a = webdriver.Firefox()
    #Abrir la página web
    url = "https://salinaka-ecommerce.web.app/"
    #Ir a la página web
    a.get(url)
    #Esperamo 10 segundos para que carga la página
    time.sleep(10)
    #Buscamos el boton Sign Up y se le da click para ingresar
    a.find_element(By.LINK_TEXT, "Sign Up").click()
    
    #Llenar datos del formulario de registro
    a.find_element(By.ID, "fullname").send_keys("prueba")
    a.find_element(By.ID, "email").send_keys("prueba@prueba.prueba.com")
    a.find_element(By.ID, "password").send_keys("Prueba123*")
    #Enviar los datos del formulario
    #Se usa la funcion XPATH para el boton enviar
    a.find_element(By.XPATH, "/html/body/div[1]/main/div/div[1]/div[1]/form/div[4]/button").click()
    print("Creación de Usuario con todos los datos requeridos:")
    print("El usuario se ha creado con éxito!!")
    print("--------------------------------------")
    time.sleep(10)
    #Cerramos la página 
    a.quit()
   
#Creamos un usuario con un dato requerido faltante 
def creacion_usuario_con_validacion_errores():
    # Abrir el navegador Firefox
    a = webdriver.Firefox()
    # Abrir la página web
    url = "https://salinaka-ecommerce.web.app/"
    a.get(url)
    # Esperamos 10 segundos para que cargue la página
    time.sleep(10)
    # Buscamos el botón Sign Up y se le da click para ingresar
    a.find_element(By.LINK_TEXT, "Sign Up").click()
    

    # Llenamos los datos de formulario para crear un usuario, pero no vamos a ingresar el correo
    a.find_element(By.ID, "fullname").send_keys("Prueba1")
    # a.find_element(By.ID, "email").send_keys("prueba@prueba.prueba.com")  # Este campo queda vacío
    a.find_element(By.ID, "password").send_keys("Prueba123*")
    # Enviamos la solicitud
    a.find_element(By.XPATH, "/html/body/div[1]/main/div/div[1]/div[1]/form/div[4]/button").click()

    # Vemos el error del campo vacío
    try:
        # Capturar el mensaje de error específico por no llenar el campo email
        error_email = a.find_element(By.XPATH, "/html/body/div[1]/main/div/div[1]/div[1]/form/div[2]/div/span") #Lo capturamos con la funcion XPATH
        #Mostramos el mensaje de Error
        print("Creación de Usuario sin un dato requerido:")
        print("Error capturado en el campo 'email': ", error_email.text)
        print("--------------------------------------")
    except:
        print("No se detectó error específico por el campo 'email'.")
    
    time.sleep(10)
    a.quit()



#Creamos un usuario con un dato requerido faltante 
def creacion_usuario_con_validacion_errores_password():
    # Abrir el navegador Firefox
    a = webdriver.Firefox()
    # Abrir la página web
    url = "https://salinaka-ecommerce.web.app/"
    a.get(url)
    # Esperamos 10 segundos para que cargue la página
    time.sleep(10)
    # Buscamos el botón Sign Up y se le da click para ingresar
    a.find_element(By.LINK_TEXT, "Sign Up").click()
    

    # Llenamos los datos de formulario para crear un usuario, pero no vamos a ingresar el password
    a.find_element(By.ID, "fullname").send_keys("Prueba")
    a.find_element(By.ID, "email").send_keys("prueba@prueba.prueba.com")  
    # a.find_element(By.ID, "password").send_keys("Prueba123*") # Este campo queda vacío
    # Enviamos la solicitud
    a.find_element(By.XPATH, "/html/body/div[1]/main/div/div[1]/div[1]/form/div[4]/button").click()

    # Vemos el error del campo vacío
    try:
        # Capturar el mensaje de error específico por no llenar el campo password
        error_password = a.find_element(By.XPATH, "/html/body/div[1]/main/div/div[1]/div[1]/form/div[3]/div/span") #Lo capturamos con la funcion XPATH
        #Mostramos el mensaje de Error
        print("Creación de Usuario sin un dato requerido passoword:")
        print("Error capturado en el campo 'password': ", error_password.text)
        print("--------------------------------------")
    except:
        print("No se detectó error específico por el campo 'password'.")
    
    time.sleep(10)
    a.quit()
    
    
    #Creamos un usuario con un dato requerido faltante 
def creacion_usuario_con_validacion_errores_name():
    # Abrir el navegador Firefox
    a = webdriver.Firefox()
    # Abrir la página web
    url = "https://salinaka-ecommerce.web.app/"
    a.get(url)
    # Esperamos 10 segundos para que cargue la página
    time.sleep(10)
    # Buscamos el botón Sign Up y se le da click para ingresar
    a.find_element(By.LINK_TEXT, "Sign Up").click()
    

    # Llenamos los datos de formulario para crear un usuario, pero no vamos a ingresar el fullname
    # a.find_element(By.ID, "fullname").send_keys("Prueba") # Este campo queda vacío
    a.find_element(By.ID, "email").send_keys("prueba@prueba.prueba.com")  
    a.find_element(By.ID, "password").send_keys("Prueba123*") 
    # Enviamos la solicitud
    a.find_element(By.XPATH, "/html/body/div[1]/main/div/div[1]/div[1]/form/div[4]/button").click()

    # Vemos el error del campo vacío
    try:
        # Capturar el mensaje de error específico por no llenar el campo fullname
        name_password = a.find_element(By.XPATH, "/html/body/div[1]/main/div/div[1]/div[1]/form/div[1]/div/span") #Lo capturamos con la funcion XPATH
        #Mostramos el mensaje de Error
        print("Creación de Usuario sin un dato requerido Full name:")
        print("Error capturado en el campo 'Full name': ", name_password.text)
    except:
        print("No se detectó error específico por el campo 'Full name'.")
    
    time.sleep(10)
    a.quit()

if __name__ == "__main__":
    creacion_usuario()
    creacion_usuario_con_validacion_errores()
    creacion_usuario_con_validacion_errores_password()
    creacion_usuario_con_validacion_errores_name()

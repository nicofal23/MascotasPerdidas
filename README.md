# 🐾 Mascotas Perdidas Rosario

Mascotas Perdidas Rosario es una plataforma diseñada para ayudar a encontrar mascotas perdidas en la ciudad de Rosario. Los usuarios pueden publicar anuncios con información sobre sus mascotas perdidas, ver anuncios de otras personas, y contactar directamente con los dueños de mascotas que han sido encontradas.

## 🚀 Características

- **Publicación de anuncios**: Los usuarios pueden crear publicaciones con detalles sobre su mascota perdida, incluyendo imágenes, descripción, y detalles de contacto.
- **Filtrado de publicaciones**: Filtra las publicaciones por categoría, color y zona para encontrar la información que necesitas rápidamente.
- **Perfil de usuario**: Los usuarios pueden actualizar su perfil, incluyendo nombre, correo electrónico, teléfono, y una foto de perfil.
- **Interacción con otros usuarios**: Posibilidad de contactar directamente con otros usuarios a través de WhatsApp.

## 🛠️ Tecnologías Utilizadas

- **Django**: Framework principal utilizado para desarrollar la aplicación web.
- **Bootstrap**: Utilizado para el diseño responsivo y los estilos CSS.
- **Font Awesome**: Iconos para mejorar la interfaz de usuario.
- **JavaScript**: Para la funcionalidad interactiva, como los modales de imágenes.

## 🎨 Diseño y Estilo

La aplicación cuenta con un diseño amigable y accesible. Se utilizan componentes de Bootstrap para asegurar que la experiencia de usuario sea intuitiva y fluida. A continuación, se detallan algunos de los elementos estilizados:

- **Botones**: Se han utilizado colores contrastantes y bordes redondeados para los botones, ofreciendo una apariencia moderna.
- **Cards**: Las publicaciones y detalles de usuario se muestran en tarjetas con sombras sutiles, mejorando la legibilidad y el enfoque en el contenido.
- **Formulario de edición**: Los formularios tienen un diseño limpio y están alineados para facilitar la entrada de datos.

## 📸 Vista Previa

![Vista Previa](https://i.ibb.co/k2Z6NVT/web.png)

## 📂 Estructura del Proyecto

```bash
├── accounts/
│   ├── migrations/
│   ├── templates/
│   │   ├── accounts/
│   │       ├── profile.html
│   │       └── ...
│   ├── templatetags/
│   │   ├── __init__.py
│   │   ├── form_tags.py
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── ...
├── blog/
│   ├── migrations/
│   ├── templates/
│   │   ├── blog/
│   │       ├── crear_post.html
│   │       ├── editar_post.html
│   │       ├── lista_posts.html
│   ├── templatetags/
│   │   ├── __init__.py
│   │   ├── custom_filters.py
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
├── templates/
│   ├── base_generic.html
├── manage.py
```

## 📄 Cómo Empezar

Sigue estos pasos para configurar el proyecto en tu máquina local:

### 1. Clona el repositorio:

```bash
git clone https://github.com/nicofal23/MascotasPerdidas.git
cd MascotasPerdidas
```

## 2. Instala las dependencias:
```bash
pip install -r requirements.txt
```

## 3. Configura la base de datos:
```bash
python manage.py migrate
```

## 4. Ejecuta el servidor:

```bash
python manage.py runserver
```


## 5. Accede a la aplicación:

Abre tu navegador y ve a <a href="http://127.0.0.1:8000/" target="_blank">http://127.0.0.1:8000/</a>.

## 📧 Contacto
Si tienes alguna pregunta o sugerencia, no dudes en ponerte en contacto:

Email: falciglionicolas@gmail.com   
LinkedIn: https://www.linkedin.com/in/nicolasfalciglio
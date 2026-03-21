import streamlit as st
import pandas as pd
import django
import os
import sys

# Configurar Django para que funcione dentro de Streamlit
sys.path.append(os.path.join(os.getcwd(), 'musicdb'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'musicdb.settings')
django.setup()

from albums.models import Artist, Album, Song

# Obtener datos desde Django ORM
albums = Album.objects.select_related('artist').all()
data = [
    {
        'Título': album.title,
        'Año': album.year,
        'Artista': album.artist.name,
    }
    for album in albums
]
df = pd.DataFrame(data)

st.write("Columnas del DataFrame:", df.columns.tolist())
st.dataframe(df)

# Interfaz Streamlit
st.title("🎶 Dashboard de Álbumes Musicales")
st.subheader("Distribución de álbumes por año")
st.bar_chart(df['Año'].value_counts().sort_index())

st.subheader("Álbumes por artista")
st.bar_chart(df['Artista'].value_counts())

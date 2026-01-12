from django.contrib import admin
from django.utils.html import format_html
from .models import Artist, Album, Song

# Configuración para Artist
@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name',)  # muestra el nombre en la lista

# Inline para mostrar canciones dentro de cada álbum
class SongInline(admin.TabularInline):  # puedes usar StackedInline si prefieres
    model = Song
    extra = 1  # cuántas filas vacías aparecen por defecto
    readonly_fields = ('admin_link', 'duration')
    fields = ('title', 'duration')  # campos que se muestran en el inline
    can_delete = False
    show_change_link = False

# Configuración para Album
@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'year', 'image')  # columnas en la lista
    inlines = [SongInline]  # canciones aparecen dentro del álbum

# Configuración para Song como modelo independiente
@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ('title', 'album', 'duration')  # columnas en la lista
    list_filter = ('album',)  # filtro por álbum
    search_fields = ('title',)  # barra de búsqueda por título
    readonly_fields = ('title', 'album', 'duration', 'lyrics')
    fields = ('title', 'album', 'duration', 'lyrics')

    def has_add_permission(self, request):
        return False
    def has_change_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False
    @admin.display(description="Add lyric")
    def add_lyrick_button(self, obj):
        return format_html('<a class="button" href="/admin/albums/song/{}/change/">Add lyric</a>',
            obj.id)

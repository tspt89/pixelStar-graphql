import graphene
from graphene_django import DjangoObjectType
from django.contrib.auth import get_user_model

from .models import mostrarPlaylist

class mostrarPlaylistType(DjangoObjectType):
    class Meta:
        model = mostrarPlaylist


class Query(graphene.ObjectType):
    mostrarPlaylist = graphene.List(mostrarPlaylistType)

    def resolve_mostrarPlaylist(self, info, **kwargs):
        Playlist = info.context.user
        if not Playlist.is_authenticated:
            raise Exception('Not logged in!')

        return mostrarPlaylist.objects.all()

class CreatemostrarPlaylist(graphene.Mutation):
    id = graphene.Int()
    name = graphene.String()
    artist = graphene.String()
    album = graphene.String()
    release = graphene.Date()
    duration = graphene.Int()

    #2
    class Arguments:
        name = graphene.String()
        artist = graphene.String()
        album = graphene.String()
        release = graphene.Date()
        duration = graphene.Int()

    #3
    def mutate(self, info, name, artist, album, release, duration):
        mostrarPlaylist = mostrarPlaylist(name=name, artist=artist, album=album, release=release, duration=duration)
        mostrarPlaylist.save()

        return CreatemostrarPlaylist(
            id=mostrarPlaylist.id,
            name=mostrarPlaylist.name,
            artist=mostrarPlaylist.artist,
            album=mostrarPlaylist.album,
            release=mostrarPlaylist.release,
            duration=mostrarPlaylist.duration,
        )


#4
class Mutation(graphene.ObjectType):
    create_mostrarPlaylist = CreatemostrarPlaylist.Field()
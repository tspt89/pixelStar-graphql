INSTALLED_APPS = (
    # After the default packages
    'graphene_django',
)

GRAPHENE = {
    'SCHEMA': 'hackernews.schema.schema',
}
class Translator:
    def __init__(self, language='en'):
        self.language = language
        self.translations = {
            'en': {
                'title': 'ConnectDot – AI Transformation Hub',
                'loaded': 'Loaded {count} products.',
                'ready': 'System ready. Awaiting further commands...'
            },
            'pl': {
                'title': 'ConnectDot – Centrum Transformacji AI',
                'loaded': 'Załadowano {count} produktów.',
                'ready': 'System gotowy. Czekam na dalsze komendy...'
            },
            'nl': {
                'title': 'ConnectDot – AI Transformatiecentrum',
                'loaded': '{count} producten geladen.',
                'ready': 'Systeem klaar. Wacht op verdere opdrachten...'
            },
            'de': {
                'title': 'ConnectDot – KI-Transformationszentrum',
                'loaded': '{count} Produkte geladen.',
                'ready': 'System bereit. Warte auf weitere Befehle...'
            },
            'fr': {
                'title': 'ConnectDot – Centre de transformation IA',
                'loaded': '{count} produits chargés.',
                'ready': 'Système prêt. En attente de nouvelles commandes...'
            },
            'es': {
                'title': 'ConnectDot – Centro de Transformación IA',
                'loaded': 'Se han cargado {count} productos.',
                'ready': 'Sistema listo. Esperando más comandos...'
            }
        }

    def translate(self, key, **kwargs):
        text = self.translations.get(self.language, self.translations['en']).get(key, key)
        return text.format(**kwargs)

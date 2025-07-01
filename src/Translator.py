class Translator:
    def __init__(self, language='pl'):
        self.language = language
        self.translations = {
            'pl': {
                'title': 'ConnectDot – Centrum Transformacji AI',
                'loaded': 'Załadowano {count} produktów.',
                'ready': 'System gotowy. Czekam na dalsze komendy...'
            },
            'en': {
                'title': 'ConnectDot – AI Transformation Hub',
                'loaded': 'Loaded {count} products.',
                'ready': 'System ready. Awaiting further commands...'
            },
            'nl': {
                'title': 'ConnectDot – AI Transformatiecentrum',
                'loaded': '{count} producten geladen.',
                'ready': 'Systeem klaar. Wacht op verdere opdrachten...'
            }
        }

    def translate(self, key, **kwargs):
        text = self.translations.get(self.language, {}).get(key, key)
        return text.format(**kwargs)

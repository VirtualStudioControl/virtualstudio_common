class ObjectDeserialisationException(Exception):

    def __init__(self, t, obj):
        super.__init__(t, obj)
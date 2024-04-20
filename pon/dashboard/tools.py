

def recomend_filter(obj):
    if obj.tags.filter(picked=True).exists():
        pass

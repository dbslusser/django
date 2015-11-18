"""
DECRIPTION:
    collection of functions to assist with handling Django queries

AUTHOR:
    David Slusser

REVISION:
    0.0.1
"""


def getObjectOrNone(model, field, value):
    """
    Description:
        Get query response or return None
    
    Parameters:
        model  - model object
        field  - field to search against
        value  - field value to search for
    
    Returns:
        query response or None
    """
    try:
        queryset = model.objects.get(**{field:value})
        return queryset
    except:
        return None


def getLatestOrNone(model, field=None):
    """
    Description:
        Get the most recent row of a model or return None
    
    Parameters:
        model  - model object
        field  - field to search against (string)
    
    Returns:
        query response or None
    """
    try:
        if field:
            return model.objects.latest(field)
        else: 
            return model.objects.latest()
    except:
        return None



import requests
import json

def query(type, id, scorevalue_min=0):
    '''
    Queries the Open Targets Platform returning the overall association score for each disease and target ID.

    Args:
    type (str): type of parameter requested to the API: disease or target.
    id (str): the disease or target identifier
    scorevalue_min (float): to filter associations or evidence according to a minimum score value 
        (default is 0)

    Returns:
    d: a dictionary with each of the associations between target and disease with its overall association score.
    '''

    url = "https://platform-api.opentargets.io/v3/platform/public/association/filter"

    params = {type: id,
            "size": "10000",
            "direct": "True",
            "scorevalue_min": scorevalue_min}

    res = requests.get(url, params=params).json()

    d = {}
    for index, record in enumerate(res["data"]):
        d[index + 1] = {"disease_id": record["id"].split("-")[1],
                "target_id": record["id"].split("-")[0],
                "association_score.overall": record['association_score']["overall"]}

    return d

def export(dictionary, filename):
    '''
    Exports a dictionary to JSON format

    Args:
    dictionary (dict): the dictionary to be converted
    filename (str): the filename of the output file

    Returns:
    None
    '''

    with open(filename, "w") as outfile:  
        json.dump(dictionary, outfile) 


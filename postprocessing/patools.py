import re
import logging
import collections
from datetime import datetime

logger = logging.getLogger(__name__)

# pa_parse_dir('/volume1/Volume1/Private/Scene/DigitalPlayground.18.12.12.Elsa.Jean.And.Romi.Rain.The.Secret.Life.Of.A.Housewife.XXX.1080p.MP4-KTRR')
# returns: dictionary of
    # shoot = {
    #     'studio': "DigitalPlayground",
    #     'date': "2018-12-12",
    #     'filename_title': 'Elsa Jean And Romi Rain The Secret Life Of A Housewife'
    # }
# returns: None (if groks don't match)
def pa_parse_dir(dir, use_filename):
    
    shoot = {
        'studio': "",
        'date': "",
        'filename_title': ""
    }
    
    search_string = dir
    logger.info("The Dir is: %s" % search_string)

    # logger.info("Processing: %s" % search_string)
    search_string = search_string.split('\\')[-1]
    search_string = search_string.split('.XXX')[0]
    search_string = search_string.split(' XXX')[0]
    dir_pattern = re.compile(r'^([a-zA-Z0-9-]+)(\s|.|\s-\s)(([0-9]{2,4})[\s|.]([0-9]{2})[\s|.]([0-9]{2})[\s|.]([\s.a-zA-Z0-9]+)|([\s.a-zA-Z0-9]+)[\s|.][(]([0-9]{2,4})[\s|.-]([0-9]{2})[\s|.-]([0-9]{2})[)])')
    if use_filename:
        search_string = search_string.split('.')[0]
    

    match_object = re.search(dir_pattern, search_string)
    if match_object is None:
        logger.critical("Failed to match directory string: %s" % search_string)
        return None

    # Studio Match
    # TODO: determine based on collections.py

    shoot['studio'] = match_object.group(1).replace('-','')

    # Segment matches
    if match_object.group(9) is not None:
        year = match_object.group(9)
        month = match_object.group(10)
        day = match_object.group(11)
        title = match_object.group(8)
    elif match_object.group(4) is not None:
        year = match_object.group(4)
        month = match_object.group(5)
        day = match_object.group(6)
        title = match_object.group(7)
    date = year + " " + month + " " + day
    if len(year) == 2:
        format = '%y %m %d'
    elif len(year) == 4:
        format = '%Y %m %d'
    else:
        logger.critical("Couldn't determine date, exiting.")
        return None
    datetime_object = datetime.strptime(date, format)
    shoot['date'] = datetime_object.strftime('%Y-%m-%d')
    logger.debug("Date string determined to be: %s " % shoot['date'])

    # Rest of filename match
    # TODO: should determine if we are title based or date/model based and output
    # appropriately
    
    shoot['filename_title'] = title.replace('.',' ')

    return shoot

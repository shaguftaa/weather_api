# ----------------------------------------------------------- #
# Demonstrates Weather Api
# Author - Shagufta <shagufta2905@gmail.com>
# ----------------------------

import logging
from flask import Blueprint
from model import RegionalForecast

forecast_api = Blueprint('forecast_api', __name__)
logger = logging.getLogger(__name__)


@forecast_api.route('/location_list', methods=['GET'])
def get_location_list():
    """
    List of all available locations with id.
    """
    return RegionalForecast().list_all_regions()


@forecast_api.route('/', methods=['GET'], defaults={'location_id': None})
@forecast_api.route('/<location_id>', methods=['GET'])
def get_forecast(location_id):
    """
    Last 30 days weather forecast for particular region if location id is not None
    else for all the regions.
    :param location_id:
    """
    regional_forecast = RegionalForecast()
    print(location_id)
    if location_id:
        return regional_forecast.get_particular_region_forecast(location_id)
    else:
        return regional_forecast.get_all_regions_forecast()

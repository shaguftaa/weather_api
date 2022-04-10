# ----------------------------------------------------------- #
# Demonstrates Weather Forecast related functions
# Author - Shagufta <shagufta2905@gmail.com>
# ----------------------------

import json
import logging
import requests
from constants import URL, SITE_LIST_URL, KEY, FORECAST_URL
from typing import Dict

logger = logging.getLogger(__name__)


class RegionalForecast:

    @staticmethod
    def list_all_regions() -> Dict:
        """
        This function returns list of all available regions.
        :return: Site list with location id and name
        """
        response = {}
        try:
            url = URL.format(SITE_LIST_URL, KEY)
            site_list_response = requests.get(url)
            response = site_list_response.content
            response = json.loads(response)
        except Exception as e:
            logger.error(e)
        finally:
            return response

    @staticmethod
    def get_particular_region_forecast(location_id: int) -> Dict:
        """
        This function return 30 days weather forecast for particular region
        :param location_id: Location id in Integer
        :return: 30 days detailed weather forecast
        """
        response = {}
        try:
            location_forecast_url = FORECAST_URL.format(location_id)
            url = URL.format(location_forecast_url, KEY)
            location_forecast_response = requests.get(url)
            response = location_forecast_response.content
            response = json.loads(response)
        except Exception as e:
            logger.error(e)
        finally:
            return response

    def get_all_regions_forecast(self) -> Dict:
        """
        This function return 30 days weather forecast for all regions
        :return: 30 days detailed weather forecast
        """
        response = {"RegionalFcst": {}, "RegionCount": 0}
        try:
            region_list = self.list_all_regions()
            region_list = region_list.get("Locations", {}).get("Location", {})
            if region_list:
                location_id_list = [i.get("@id") for i in region_list]
                for location_id in location_id_list:
                    region_forecast = self.get_particular_region_forecast(location_id)
                    region_forecast_data = region_forecast.get("RegionalFcst", {})
                    region = region_forecast_data.get("regionId")
                    if region_forecast_data:
                        response["RegionalFcst"][region] = region_forecast_data
                        response["RegionCount"] += 1

        except Exception as e:
            logger.error(e)
        finally:
            return response

#!/usr/bin/env python
from sys import exit

from services_data import exceptions
from services_data.technical_data import Exceptions
from services.user_input import user_request
from services.get_coordinates import get_coordinates
from services.work_with_api import get_response_from_api
from services.print_response import print_response


def main():
    try:
        city, radius = user_request()
    except exceptions.InputError:
        print(Exceptions.INPUT_ERROR.value)
        exit(1)
    try:
        coordinates = get_coordinates(city)
    except exceptions.CantGetGPSCoordinates:
        print(Exceptions.COORDINATES_ERROR.value)
        exit(1)
    try:
        count_of_earthquakes = get_response_from_api(*coordinates, radius)
    except exceptions.CantGetResponseFromApi:
        print(Exceptions.API_ERROR.value)
        exit(1)

    print_response(city, radius, *coordinates,  count_of_earthquakes)


if __name__ == "__main__":
    main()

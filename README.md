# Rent-a-Bike

The data that this program works with is provided by the Toronto bike share network. The data contains information about the docking stations, such as the location of the station and how many bikes are currently available.

This program uses data from a Comma Separated Value (CSV) file named stations.csv. Each row of this file contains the following information about a single docking station:

station ID: the unique identification (ID) number of the station
name: the name of the station (not necessarily unique)
latitude: the latitude of the station location
longitude: the longitude of the station location
capacity: the total number of bike docks (empty or with bike) at the station
bikes available: the number of bikes currently available to rent at the station
docks available: the number of docks at the station that currently do not have a bike attached to them
is renting: whether or not a station is currently allowing bike rentals
is returning: whether or not a station is currently allowing bike returns

This program works with real world data. 

The City of Toronto Bike Share website (https://www.toronto.ca/city-government/data-research-maps/open-data/open-data-catalogue/transportation/#84045f23-7465-0892-8889-7b6f91049b29) provides data about stations in a file format called JSON. Rent-a-Bike uses two of the City's bike share JSON files, one with station information and another with station status.

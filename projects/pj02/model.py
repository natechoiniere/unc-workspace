"""The model classes maintain the state and logic of the simulation."""

from __future__ import annotations
from projects.pj02.constants import CELL_RADIUS
from typing import List
from random import random
from projects.pj02 import constants
from math import sin, cos, pi, sqrt


__author__ = "730443739"


class Point:
    """A model of a 2-d cartesian coordinate Point."""
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Construct a point with x, y coordinates."""
        self.x = x
        self.y = y

    def add(self, other: Point) -> Point:
        """Add two Point objects together and return a new Point."""
        x: float = self.x + other.x
        y: float = self.y + other.y
        return Point(x, y)
    
    def distance(self, other_point: Point) -> float:
        """Returns the distance between two points."""
        dist: float = sqrt((self.x - other_point.x) ** 2 + ((self.y - other_point.y) ** 2))
        return dist


class Cell:
    """An individual subject in the simulation."""
    location: Point
    direction: Point
    sickness: int = constants.VULNERABLE

    def __init__(self, location: Point, direction: Point):
        """Construct a cell with its location and direction."""
        self.location = location
        self.direction = direction
        
    def tick(self) -> None:
        """Performs an update for the cell object each time the method is called."""
        self.location = self.location.add(self.direction)
        if self.is_infected():
            self.sickness += 1
        if self.sickness > constants.RECOVERY_PERIOD:
            self.immunize()

    def color(self) -> str:
        """Return the color representation of a cell."""
        if self.is_vulnerable():
            return "gray"
        elif self.is_infected():
            return "red"
        elif self.is_immune():
            return "green"
        return "orange"

    def contract_disease(self) -> None:
        """Sets the cell's sickness to INFECTED."""
        self.sickness = constants.INFECTED
    
    def is_vulnerable(self) -> bool:
        """Returns True if the cell is vulnerable."""
        if self.sickness == constants.VULNERABLE:
            return True
        else:
            return False

    def is_infected(self) -> bool:
        """Returns True if the cell is infected."""
        if self.sickness >= constants.INFECTED:
            return True
        else:
            return False

    def contact_with(self, cell_object: Cell) -> None:
        """Infects vulnerable cells and bounces all cells off eachother."""
        if self.is_infected() and cell_object.is_vulnerable():
            cell_object.contract_disease()
            cell_object.direction.x *= -1
            cell_object.direction.y *= -1
            self.direction.x *= -1
            self.direction.y *= -1
        elif self.is_vulnerable() and cell_object.is_infected():
            self.contract_disease()
            cell_object.direction.x *= -1
            cell_object.direction.y *= -1
            self.direction.x *= -1
            self.direction.y *= -1
        else:
            cell_object.direction.x *= -1
            cell_object.direction.y *= -1
            self.direction.x *= -1
            self.direction.y *= -1
    
    def immunize(self) -> None:
        """Sets the cell's sickness to IMMUNE."""
        self.sickness = constants.IMMUNE
    
    def is_immune(self) -> bool:
        """Returns True if the cell is immune."""
        if self.sickness == constants.IMMUNE:
            return True
        else:
            return False


class Model:
    """The state of the simulation."""
    population: List[Cell]
    time: int = 0
    
    def __init__(self, cells: int, speed: float, infected: int, immune: int = 0):
        """Initialize the cells with random locations and directions."""
        if infected >= cells or infected <= 0:
            raise ValueError("Error: # of infected cells is >= to # of cells, or is <= to 0.")
        if immune >= cells or immune < 0:
            raise ValueError("Error: # of immune cells is >= to # of cells or is < 0.")
        self.population = []
        i: int = 0
        j: int = 0
        k: int = 0
        for _ in range(0, cells):
            start_loc = self.random_location()
            start_dir = self.random_direction(speed)
            self.population.append(Cell(start_loc, start_dir))
            if i < infected:
                self.population[i].contract_disease()
                i += 1
        if immune > 0:
            for _ in range(0, cells):
                if self.population[k].is_infected():
                    k += 1
                elif self.population[k].is_vulnerable():
                    if j < immune:
                        self.population[k].immunize()
                        j += 1
                    k += 1
        
    def tick(self) -> None:
        """Update the state of the simulation by one time step."""
        self.time += 1
        for cell in self.population:
            cell.tick()
            self.enforce_bounds(cell)
        self.check_contacts()

    def random_location(self) -> Point:
        """Generate a random location."""
        start_x = random() * constants.BOUNDS_WIDTH - constants.MAX_X
        start_y = random() * constants.BOUNDS_HEIGHT - constants.MAX_Y
        return Point(start_x, start_y)

    def random_direction(self, speed: float) -> Point:
        """Generate a 'point' used as a directional vector."""
        random_angle = 2.0 * pi * random()
        dir_x = cos(random_angle) * speed
        dir_y = sin(random_angle) * speed
        return Point(dir_x, dir_y)

    def enforce_bounds(self, cell: Cell) -> None:
        """Cause a cell to 'bounce' if it goes out of bounds."""
        if cell.location.x > constants.MAX_X:
            cell.location.x = constants.MAX_X
            cell.direction.x *= -1
        if cell.location.x < constants.MIN_X:
            cell.location.x = constants.MIN_X
            cell.direction.x *= -1
        if cell.location.y > constants.MAX_Y:
            cell.location.y = constants.MAX_X
            cell.direction.y *= -1
        if cell.location.y < constants.MIN_Y:
            cell.location.y = constants.MIN_Y
            cell.direction.y *= -1

    def check_contacts(self) -> None:
        """Checks all cells to see if they are in contact with any other cell."""
        for cell in range(len(self.population)):
            for other_cells in range(cell + 1, len(self.population)):
                if self.population[cell].location.distance(self.population[other_cells].location) < CELL_RADIUS:
                    self.population[cell].contact_with(self.population[other_cells])
                else:
                    ...

    def is_complete(self) -> bool:
        """Method to indicate when the simulation is complete."""
        i: int = 0
        for _ in self.population:
            if _.is_infected():
                i += 1
            else:
                ...
        if i > 0:
            return False
        else:
            return True
        return False
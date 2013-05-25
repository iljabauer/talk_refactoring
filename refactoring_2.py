class Movie:
    CHILDRENS = 2
    REGULAR = 0
    NEW_RELEASE = 1

    _title = None
    _priceCode = None

    def __init__(self, title, priceCode):
        self._title = title
        self._priceCode = priceCode

    def getPriceCode(self):
        return self._priceCode

    def setPriceCode(self, arg):
        self._priceCode = arg

    def getTitle(self):
        return self._title


class Rental:
    _movie = None
    _daysRented = None

    def __init__(self, movie, daysRented):
        self._movie = movie
        self._daysRented = daysRented

    def getDaysRented(self):
        return self._daysRented

    def getMovie(self):
        return self._movie


class Customer:
    _name = None
    _rentals = []

    def __init__(self, name):
        self._name = name

    def addRental(self, arg):
        self._rentals.append(arg)

    def getName(self):
        return self._name

    def amountFor(self, aRental):
        result = 0
        priceCode = aRental.getMovie().getPriceCode()
        if priceCode == Movie.REGULAR:
            result += 2
            if aRental.getDaysRented() > 2:
                result += (aRental.getDaysRented() - 2) * 1.5
        elif priceCode == Movie.NEW_RELEASE:
            result += aRental.getDaysRented() * 3
        elif priceCode == Movie.CHILDRENS:
            result += 1.5
            if aRental.getDaysRented() > 3:
                result += (aRental.getDaysRented() - 3) * 1.5

        return result

    def statement(self):
        totalAmount = 0
        frequentRenterPoints = 0
        result = "Rental Record for %s\n" % self.getName()

        # determine amounts for each line
        for each in self._rentals:

            thisAmount = self.amountFor(each)

            # add frequent renter points
            frequentRenterPoints += 1

            # add bonus for a two day new release rental
            if (each.getMovie().getPriceCode() == Movie.NEW_RELEASE) & (each.getDaysRented() > 1):
                frequentRenterPoints += 1

            # show figures for this rental
            result += "\t%s\t%s\n" % (each.getMovie().getTitle(), thisAmount)
            totalAmount += thisAmount

        # add footer lines
        result += "Amount owed is %s\n" % totalAmount
        result += "You earned %s frequent renter points" % frequentRenterPoints

        return result

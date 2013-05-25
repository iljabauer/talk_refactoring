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

    def getCharge(self):
        result = 0
        priceCode = self.getMovie().getPriceCode()
        if priceCode == Movie.REGULAR:
            result += 2
            if self.getDaysRented() > 2:
                result += (self.getDaysRented() - 2) * 1.5
        elif priceCode == Movie.NEW_RELEASE:
            result += self.getDaysRented() * 3
        elif priceCode == Movie.CHILDRENS:
            result += 1.5
            if self.getDaysRented() > 3:
                result += (self.getDaysRented() - 3) * 1.5
        return result

    def getFrequentPoints(self):
        if (self.getMovie().getPriceCode() == Movie.NEW_RELEASE) & (self.getDaysRented() > 1):
            return 2
        else:
            return 1


class Customer:
    _name = None
    _rentals = []

    def __init__(self, name):
        self._name = name

    def addRental(self, arg):
        self._rentals.append(arg)

    def getName(self):
        return self._name

    def getTotalCharge(self):
        result = 0

        for each in self._rentals:
            result += each.getCharge()

        return result

    def getTotalFrequentRenterPoints(self):
        result=0

        for each in self._rentals:
            result += each.getFrequentPoints()

        return result

    def statement(self):
        result = "Rental Record for %s\n" % self.getName()

        # determine amounts for each line
        for each in self._rentals:
            # show figures for this rental
            result += "\t%s\t%s\n" % (each.getMovie().getTitle(), each.getCharge())

        # add footer lines
        result += "Amount owed is %s\n" % self.getTotalCharge()
        result += "You earned %s frequent renter points" % self.getTotalFrequentRenterPoints()

        return result

    def htmlStatement(self):
        result = "<h1>Rentals for <em>%s</em></h1><p>\n" % self.getName()

        for each in self._rentals:
            # show figures for this rental
            result += "%s: %s</br>\n" % (each.getMovie().getTitle(), each.getCharge())

        # add footer lines
        result += "<p>You owe <em>%s</em></p>\n" % self.getTotalCharge()
        result += "On this rental you earned <em>%s</em> frequent renter points</p>" % self.getTotalFrequentRenterPoints()

        return result
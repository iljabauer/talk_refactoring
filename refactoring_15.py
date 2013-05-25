class Movie:
    CHILDRENS = 2
    REGULAR = 0
    NEW_RELEASE = 1

    _title = None
    _price = None

    def __init__(self, title, priceCode):
        self._title = title
        self.setPriceCode(priceCode)

    def getPriceCode(self):
        return self._price.getPriceCode()

    def setPriceCode(self, arg):
        if arg == Movie.REGULAR:
            self._price = RegularPrice()
        elif arg == Movie.NEW_RELEASE:
            self._price = NewReleasePrice()
        elif arg == Movie.CHILDRENS:
            self._price = ChildrensPrice()

    def getTitle(self):
        return self._title

    def getCharge(self, daysRented):
        return self._price.getCharge(daysRented)

    def getFrequentPoints(self, daysRented):
        if (self.getPriceCode() == Movie.NEW_RELEASE) & (daysRented > 1):
            return 2
        else:
            return 1


class Price:
    def getPriceCode(self):
        pass

    def getCharge(self, daysRented):
        result = 0
        priceCode = self.getPriceCode()
        if priceCode == Movie.REGULAR:
            result += 2
            if daysRented > 2:
                result += (daysRented - 2) * 1.5
        elif priceCode == Movie.NEW_RELEASE:
            result += daysRented * 3
        elif priceCode == Movie.CHILDRENS:
            result += 1.5
            if daysRented > 3:
                result += (daysRented - 3) * 1.5
        return result


class ChildrensPrice(Price):
    def getPriceCode(self):
        return Movie.CHILDRENS


class NewReleasePrice(Price):
    def getPriceCode(self):
        return Movie.NEW_RELEASE


class RegularPrice(Price):
    def getPriceCode(self):
        return Movie.REGULAR


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
        return self._movie.getCharge(self._daysRented)

    def getFrequentPoints(self):
        return self._movie.getFrequentPoints()


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